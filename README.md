# Pocket TTS — Offline Portable Edition with Video Generator

> Pocket TTS is a lightweight, real-time text-to-speech engine by Kyutai Labs.
> This portable pack bundles everything + adds a **text-to-video generator**
> (360p MP4 with waveform visualization and title overlay).

---

## What's New

- 🎬 **Video Generator** — enter text + title + select a voice → get a 360p MP4 video
  with animated audio waveform and title overlay
- 🏷️ **Voice metadata** — every voice now shows language, gender, conversation/reading
  style, and British non-rhotic accent flags
- 🔍 **Voice filters** — filter by English, Non-English, Conversation, Reading, Non-Rhotic

---

## System Requirements

- **Windows 10/11** (64-bit)
- **4 GB RAM** minimum (8 GB recommended)
- **Intel 8th gen+ or AMD Ryzen** (CPU must support AVX2 instructions)
- **No GPU required** — runs entirely on CPU
- **No internet** — works fully air-gapped after extraction

---

## Installation

The release is split into **4 layered ZIPs** to keep downloads manageable.  
Download ALL parts, then extract them to the **same folder** in order:

| # | File | Contents | Size |
|---|------|----------|------|
| 1 | `pocket-tts-core-v1.0.zip` | App, Python runtime, ffmpeg | ~60MB |
| 2 | `pocket-tts-deps-v1.0.zip` | Python libraries (site-packages) | ~960MB |
| 3 | `pocket-tts-models-v1.0.zip` | TTS model + voice embeddings | ~370MB |
| 4 | `pocket-tts-voices-v1.0.zip` | Custom celebrity voices | ~5MB |

### Assembly Steps

```
1. Create a folder:  pocket-tts-portable/
2. Extract ALL ZIPs into that folder (overwrite when prompted)
3. Double-click start.bat
```

After extraction your folder should look like:

```
pocket-tts-portable/
├── start.bat
├── python/            ← Part 1
├── tools/ffmpeg/      ← Part 1
├── site-packages/     ← Part 2
├── models/            ← Part 3
├── voices-celebrities/← Part 4 (optional)
├── pocket_tts_api.py
├── video_generator.py
├── voice_metadata.py
└── templates/
    └── index.html
```

### Quick Start After Assembly

1. **Double-click** `start.bat`
2. Wait for the console to show:
   ```
   Uvicorn running on http://0.0.0.0:8000
   ```
3. **Open your browser** → `http://localhost:8000`

---

## Features

### 🎬 Video Generator
1. Click **🎬 Video Generator** in the sidebar
2. Enter a **title** (displayed on the video)
3. Enter the **script** (text to be spoken)
4. Select a **voice** from the voice library
5. Click **Generate Video**
6. Download the 360p MP4 — dark background, centered title, animated waveform

### 🔊 Text to Speech
- OpenAI-compatible API (`POST /v1/audio/speech`)
- Select any of 26 built-in voices or upload your own
- WAV/MP3 output

### 💬 Voice Chat
- Chat with LLM, hear responses in selected voice
- Streaming SSE endpoint (`POST /v1/chat/completions/stream`)
- Real-time text + audio streaming

### 🎤 Voice Cloning
- Upload 5+ seconds of audio → clone any voice
- Supports WAV, MP3, OGG, FLAC

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/v1/audio/voices` | List all voices with metadata |
| `POST` | `/v1/audio/speech` | Text-to-speech (OpenAI-compatible) |
| `POST` | `/api/video/generate` | **Generate MP4 video** `{text, title, voice}` |
| `POST` | `/v1/chat/completions` | Voice chat with LLM |
| `POST` | `/v1/chat/completions/stream` | Streaming voice chat (SSE) |
| `POST` | `/api/voices/upload` | Upload custom voice |
| `GET` | `/health` | Health check |

### Video generation via curl

```bash
curl -X POST http://localhost:8000/api/video/generate \
  -H "Content-Type: application/json" \
  -d '{"text":"Hello world. This is a test.","title":"My Video","voice":"alba"}' \
  -o output.mp4
```

---

## Voice Catalog

### English — Conversation (10)

| Voice | Gender | Non-Rhotic | Notes |
|-------|--------|------------|-------|
| `jane` | 🚺 Female | — | |
| `anna` | 🚺 Female | ✅ Tested | Non-rhotic British (0.540s) |
| `charles` | 🚹 Male | ✅ Tested | Non-rhotic British (0.583s) |
| `eve` | 🚺 Female | — | |
| `george` | 🚹 Male | — | |
| `mary` | 🚺 Female | — | |
| `michael` | 🚹 Male | — | |
| `paul` | 🚹 Male | ✅ Tested | Non-rhotic British (0.588s) |
| `vera` | 🚺 Female | ✅ Tested | Non-rhotic British (0.668s) |
| `jean` | 🚹 Male | — | Les Misérables |

### English — Reading (11)

| Voice | Gender | Non-Rhotic | Notes |
|-------|--------|------------|-------|
| `alba` | 🚹 Male | — | Default voice; user-tested male |
| `bill-boerst` | 🚹 Male | — | |
| `caro-davy` | 🚺 Female | ✅ Tested | Non-rhotic British (0.560s) |
| `peter-yearsley` | 🚹 Male | ✅ Tested | Non-rhotic British; fastest (0.699s) 🏆 |
| `stuart-bell` | 🚹 Male | ✅ Tested | Non-rhotic British (0.595s) |
| `azelma` | 🚺 Female | — | Les Misérables |
| `eponine` | 🚺 Female | — | Les Misérables |
| `fantine` | 🚺 Female | ✅ Tested | Non-rhotic British (0.645s); Les Mis |
| `cosette` | 🚺 Female | — | Les Misérables |
| `javert` | 🚹 Male | — | Les Misérables |
| `marius` | 🚹 Male | — | Les Misérables |

### Non-English (5)

| Voice | Language | Gender | Notes |
|-------|----------|--------|-------|
| `estelle` | 🇫🇷 French | 🚺 Female | Native French |
| `giovanni` | 🇮🇹 Italian | 🚹 Male | Native Italian |
| `juergen` | 🇩🇪 German | 🚹 Male | Native German |
| `lola` | 🇪🇸 Spanish | 🚺 Female | Native Spanish |
| `rafael` | 🇵🇹 Portuguese (BR) | 🚹 Male | Native Brazilian Portuguese |

> **26 voices total** (21 English + 5 non-English). 8 voices confirmed non-rhotic British
> English via user testing. Voice classification from Kyutai official page.
>
> Add custom voices: place WAV files in `voices-celebrities/`.

---

## File Structure

```
pocket-tts-portable/
├── start.bat                  ← Double-click to start
├── README.md
├── .gitignore
├── config.json                ← Server & LLM configuration
├── pocket_tts_api.py          ← FastAPI server (OpenAI-compatible)
├── video_generator.py          ← TTS → ffmpeg → 360p MP4 pipeline
├── voice_metadata.py          ← 26-voice metadata registry
├── audio_utils.py             ← Audio conversion utilities
├── web_client.html            ← Standalone web TTS client
├── python/                    ← Embedded Python 3.11
├── site-packages/             ← All Python dependencies
├── models/                    ← TTS model + 26 voice embeddings
│   ├── model.safetensors
│   ├── tokenizer.model
│   └── embeddings/
├── voices-celebrities/        ← Custom voice WAV files
├── templates/
│   └── index.html             ← Main WebUI
└── output/                    ← Generated audio + video
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `python.exe` fails to start | Install VC Redist: https://aka.ms/vs/17/release/vc_redist.x64.exe |
| "Model not found" | `models/` folder must contain `model.safetensors` + `tokenizer.model` |
| Port 8000 already in use | Edit `config.json` → `server.port` |
| Voice sounds robotic | Try a different voice; non-rhotic British voices tested best for English |
| Video generation fails | Ensure ffmpeg is installed and on PATH |
| CPU usage too high | Normal during TTS/video generation; runs on CPU only |
| Chinese text not rendering | Requires `C:/Windows/Fonts/msyh.ttc` (bundled with Windows) |

---

## Credits

- **TTS Engine:** [Kyutai Labs — Pocket TTS](https://github.com/kyutai-labs/pocket-tts)
- **Video Pipeline:** Adapted from [podcast-video-generator](https://github.com/sujmao/podcast-video-generator)
- **Server:** [ai-joe-git/pocket-tts-server](https://github.com/ai-joe-git/pocket-tts-server)
- **Voices:** Kyutai TTS Voices collection on HuggingFace

## License

This package bundles open-source software. See respective project repositories for license details.
