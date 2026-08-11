# Pocket TTS Voice Metadata — Master List

> **Sources:**
> - [x] Kyutai official page (kyutai.org/blog/2026-01-13-pocket-tts) — cached 2026-08-11 — **authoritative for conversation/reading**
> - [x] User-tested British English (non-rhotic) benchmark — vlist1.txt
> - [x] Embedding availability confirmed (models/embeddings/*.safetensors)
> - [x] Pocket TTS built-in voice registry (utils.py `_ORIGINS_OF_PREDEFINED_VOICES`)

---

## Voice Metadata Table

| # | Voice ID | Language | Gender | Conv / Read | 🇬🇧 Non-Rhotic | Notes |
|---|----------|----------|--------|-------------|---------------|-------|
| 1 | `jane` | 🇬🇧 English | 🚺 Female | 💬 Conversation | — | |
| 2 | `alba` | 🇬🇧 English | 🚹 Male | 📖 Reading | — | Pocket TTS default voice; user-tested: male |
| 3 | `bill-boerst` | 🇬🇧 English | 🚹 Male | 📖 Reading | — | |
| 4 | `caro-davy` | 🇬🇧 English | 🚺 Female | 📖 Reading | ✅ Tested (0.560s) | |
| 5 | `peter-yearsley` | 🇬🇧 English | 🚹 Male | 📖 Reading | ✅ Tested (0.699s) 🏆 | Fastest in user benchmark |
| 6 | `stuart-bell` | 🇬🇧 English | 🚹 Male | 📖 Reading | ✅ Tested (0.595s) | |
| 7 | `anna` | 🇬🇧 English | 🚺 Female | 💬 Conversation | ✅ Tested (0.540s) | |
| 8 | `azelma` | 🇬🇧 English | 🚺 Female | 📖 Reading | — | Les Misérables character |
| 9 | `charles` | 🇬🇧 English | 🚹 Male | 💬 Conversation | ✅ Tested (0.583s) | |
| 10 | `eponine` | 🇬🇧 English | 🚺 Female | 📖 Reading | — | Les Misérables character |
| 11 | `eve` | 🇬🇧 English | 🚺 Female | 💬 Conversation | — | |
| 12 | `fantine` | 🇬🇧 English | 🚺 Female | 📖 Reading | ✅ Tested (0.645s) | Les Misérables character |
| 13 | `george` | 🇬🇧 English | 🚹 Male | 💬 Conversation | — | |
| 14 | `mary` | 🇬🇧 English | 🚺 Female | 💬 Conversation | — | |
| 15 | `michael` | 🇬🇧 English | 🚹 Male | 💬 Conversation | — | |
| 16 | `paul` | 🇬🇧 English | 🚹 Male | 💬 Conversation | ✅ Tested (0.588s) | |
| 17 | `vera` | 🇬🇧 English | 🚺 Female | 💬 Conversation | ✅ Tested (0.668s) | |
| 18 | `jean` | 🇬🇧 English | 🚹 Male | 💬 Conversation | — | Les Misérables character |
| 19 | `estelle` | 🇫🇷 French | 🚺 Female | — | — | Non-English; conversation/reading not classified |
| 20 | `giovanni` | 🇮🇹 Italian | 🚹 Male | — | — | Non-English; conversation/reading not classified |
| 21 | `juergen` | 🇩🇪 German | 🚹 Male | — | — | Non-English; conversation/reading not classified |
| 22 | `lola` | 🇪🇸 Spanish | 🚺 Female | — | — | Non-English; conversation/reading not classified |
| 23 | `rafael` | 🇵🇹 Portuguese (BR) | 🚹 Male | — | — | Non-English; conversation/reading not classified |
| 24 | `cosette` | 🇬🇧 English | 🚺 Female | 📖 Reading* | — | Les Misérables; not on Kyutai page; embedding exists |
| 25 | `javert` | 🇬🇧 English | 🚹 Male | 📖 Reading* | — | Les Misérables; not on Kyutai page; embedding exists |
| 26 | `marius` | 🇬🇧 English | 🚹 Male | 📖 Reading* | — | Les Misérables; not on Kyutai page; embedding exists |

> \* = inferred (not on official Kyutai page; all Les Misérables voices with known classification are Reading)

---

## Key

| Column | Meaning |
|--------|---------|
| **Voice ID** | API `voice_id` (hyphenated lowercase) |
| **Language** | Native language of the voice |
| **Gender** | 🚹 Male / 🚺 Female |
| **Conv / Read** | 💬 Conversation (casual/dialogue style) / 📖 Reading (narration/TTS style) — from Kyutai official page |
| **🇬🇧 Non-Rhotic** | ✅ = user-tested British English without rhotic 'r' accent, with speed benchmark (seconds per 20-sentence batch) |

---

## Summary Counts

| Category | Count |
|----------|-------|
| **Total voices** | 26 |
| **English** | 21 |
| **Non-English** | 5 (fr/de/it/es/pt) |
| **Conversation** | 10 (jane, anna, charles, eve, george, mary, michael, paul, vera, jean) |
| **Reading** | 10 confirmed (alba, bill-boerst, caro-davy, peter-yearsley, stuart-bell, azelma, eponine, fantine + cosette*, javert*, marius*) |
| **🇬🇧 Non-Rhotic tested** | 8 (caro-davy, peter-yearsley, stuart-bell, anna, charles, fantine, paul, vera) |
| **Custom WAV voices** | 2 (donald-trump, joe-original) — not in this table |

---

## Design Notes for WebUI

The voice selector in the web UI should display these columns as tags/badges:

```
┌─────────────────────────────────────────────┐
│ 🎤 Anna                                      │
│   🇬🇧 English  🚺 Female  💬 Conversation     │
│   🇬🇧 Non-Rhotic British English             │
├─────────────────────────────────────────────┤
│ 🎤 Peter Yearsley                             │
│   🇬🇧 English  🚹 Male  📖 Reading            │
│   🇬🇧 Non-Rhotic British English  ⚡ Fastest  │
├─────────────────────────────────────────────┤
│ 🎤 Juergen                                    │
│   🇩🇪 German  🚹 Male                         │
├─────────────────────────────────────────────┤
│ 🎤 Giovanni                                   │
│   🇮🇹 Italian  🚹 Male                        │
└─────────────────────────────────────────────┘
```

### CSS class mapping for programmatic use

```json
{
  "voice_id": "anna",
  "language": {"code": "en", "label": "English", "flag": "🇬🇧"},
  "gender": {"code": "f", "label": "Female", "emoji": "🚺"},
  "style": {"code": "conversation", "label": "Conversation", "emoji": "💬"},
  "accent": {"code": "non-rhotic", "label": "Non-Rhotic British", "emoji": "🇬🇧", "tested": true},
  "tags": ["english", "female", "conversation", "non-rhotic", "tested"]
}
```
