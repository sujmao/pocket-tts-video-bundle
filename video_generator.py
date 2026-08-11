"""
Video Generator Module
TTS → WAV → ffmpeg filter_complex → 360p MP4.

Reuses pocket_tts model and voice state loading from the API server.
Reference: podcast-video-generator ffmpeg pipeline, adapted for pocket_tts (24kHz).
"""

import io
import subprocess
import tempfile
from pathlib import Path

import scipy.io.wavfile

# ── ffmpeg constants ────────────────────────────────────────────────────

VIDEO_WIDTH = 640
VIDEO_HEIGHT = 360
WAVEFORM_HEIGHT = 120
WAVEFORM_Y = 140
TITLE_Y = 25
TITLE_FONTSIZE = 24
TITLE_FONTCOLOR = "0xffffff"
BG_COLOR = "0x0a0a1a"
WAVE_COLORS = "0x00ffaa|0x00dd88"
WAVE_MODE = "line"  # "line" | "p2p" | "cline" | "point"
WAVE_RATE = 30
VIDEO_CRF = 20
VIDEO_PRESET = "medium"
AUDIO_BITRATE = "192k"

# CJK font on Windows (colon escaped for ffmpeg drawtext filter syntax)
FONT_PATH = "C\\:/Windows/Fonts/msyh.ttc"


def _escape_drawtext(s: str) -> str:
    r"""Escape a string for ffmpeg drawtext filter: \ ' : %"""
    s = s.replace("\\", "\\\\")
    s = s.replace("'", "\\'")
    s = s.replace(":", "\\:")
    s = s.replace("%", "\\%")
    return s


def _build_filter_complex(title: str) -> str:
    """Build the ffmpeg filter_complex string."""
    safe_title = _escape_drawtext(title)

    return (
        # 1. Dark background canvas (640×360)
        f"color=c={BG_COLOR}:s={VIDEO_WIDTH}x{VIDEO_HEIGHT},format=rgba[bg];"
        # 2. Draw title text centered at top
        f"[bg]drawtext=fontfile='{FONT_PATH}':"
        f"text='{safe_title}':"
        f"fontcolor={TITLE_FONTCOLOR}:fontsize={TITLE_FONTSIZE}:"
        f"x=(w-text_w)/2:y={TITLE_Y}[bg_title];"
        # 3. Waveform visualization from audio stream
        f"[0:a]showwaves=s={VIDEO_WIDTH}x{WAVEFORM_HEIGHT}:mode={WAVE_MODE}:"
        f"colors={WAVE_COLORS}:rate={WAVE_RATE}[v_wave];"
        # 4. Overlay waveform on titled background
        f"[bg_title][v_wave]overlay=0:{WAVEFORM_Y}[out]"
    )


def generate_video(
    text: str,
    title: str,
    voice_state,
    tts_model,
    output_dir: Path,
) -> Path:
    """
    Generate a 360p MP4 video with TTS audio and animated waveform.

    Args:
        text: The text to speak.
        title: Title text displayed at top of video.
        voice_state: Loaded pocket_tts voice state.
        tts_model: The loaded pocket_tts TTSModel instance.
        output_dir: Directory to write the output MP4.

    Returns:
        Path to the generated MP4 file.
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # ── 1. Generate audio via pocket_tts ─────────────────────────────
    print(f"[VIDEO] Generating TTS audio ({len(text)} chars)...")
    audio = tts_model.generate_audio(voice_state, text)
    audio_np = audio.numpy()
    sample_rate = tts_model.sample_rate
    duration_s = len(audio_np) / sample_rate
    print(f"[VIDEO] Audio: {duration_s:.1f}s @ {sample_rate}Hz, {len(audio_np)} samples")

    # ── 2. Write WAV to temp file ────────────────────────────────────
    tmp_wav = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    tmp_wav.close()
    wav_path = Path(tmp_wav.name)
    try:
        scipy.io.wavfile.write(str(wav_path), sample_rate, audio_np)
        print(f"[VIDEO] WAV written: {wav_path}")

        # ── 3. ffmpeg: WAV → MP4 ────────────────────────────────────
        # Output filename: first 40 chars of title, sanitized
        safe_name = "".join(c for c in title[:40] if c.isalnum() or c in " -_").strip()
        if not safe_name:
            safe_name = "video"
        output_path = output_dir / f"{safe_name}.mp4"

        # Avoid overwriting; append number if collision
        counter = 1
        while output_path.exists():
            output_path = output_dir / f"{safe_name}_{counter}.mp4"
            counter += 1

        filter_complex = _build_filter_complex(title)

        cmd = [
            "ffmpeg",
            "-i", str(wav_path),
            "-filter_complex", filter_complex,
            "-map", "[out]",
            "-map", "0:a",
            "-c:v", "libx264",
            "-preset", VIDEO_PRESET,
            "-crf", str(VIDEO_CRF),
            "-pix_fmt", "yuv420p",
            "-c:a", "aac",
            "-b:a", AUDIO_BITRATE,
            "-shortest",
            "-y",
            str(output_path),
        ]

        print(f"[VIDEO] Running ffmpeg...")
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=300,  # 5-minute timeout for long audio
        )

        if result.returncode != 0:
            stderr_tail = (
                result.stderr.strip()[-2000:] if result.stderr else "(no output)"
            )
            print(f"[VIDEO] ffmpeg error:\n{stderr_tail}")
            raise RuntimeError(f"ffmpeg exited with code {result.returncode}")

        print(f"[VIDEO] Done: {output_path}")

    finally:
        # Clean up temp WAV
        try:
            wav_path.unlink(missing_ok=True)
        except Exception:
            pass

    return output_path
