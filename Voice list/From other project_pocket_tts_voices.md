# Pocket-TTS 可用声音模型列表

> 来源：Pocket-TTS 2.1.0 README + HuggingFace `kyutai/tts-voices` + CLI 文档
> 任何声音均可跨语言使用（跨语言声音克隆），但可能带原语言口音。

---

## 一、语言模型（`--language` 参数）

| 模型 | 层数 | 速度 | 音质 | 适用场景 |
|------|------|------|------|----------|
| `english` | 6 层 | 快 | 中上 | 英文默认（等同 `english_2026-04`） |
| `english_2026-04` | 6 层 | 快 | 中上 | 英文最新蒸馏版 |
| `english_2026-01` | 6 层 | 快 | 中上 | 英文旧版 |
| `german` | 6 层 | 快 | 中上 | 德文蒸馏版 |
| `german_24l` | 24 层 | 慢 (~2-3×) | 高 | 德文未蒸馏版，音质更高 |
| `italian` | 6 层 | 快 | 中上 | 义文蒸馏版 |
| `italian_24l` | 24 层 | 慢 (~2-3×) | 高 | 义文未蒸馏版，音质更高 |
| `french` / `french_24l` | 6 / 24 层 | — | — | 法文（本次任务不用） |
| `spanish` / `spanish_24l` | 6 / 24 层 | — | — | 西文（本次任务不用） |
| `portuguese` / `portuguese_24l` | 6 / 24 层 | — | — | 葡文（本次任务不用） |

> 本机 i7-8565U（无 GPU）实测：`german` 首次 ~100s，缓存后 ~15s；`german_24l` 首次 ~210s，缓存后 ~30s。

---

## 二、内置声音（`--voice` 参数）

### 🇬🇧 英文（English）

| 声音 | 性别 | 型别 | 备注 |
|------|------|------|------|
| **alba** | 🚺 女 | **交谈** | Pocket-TTS 预设默认声音；Alba MacKenna 录制，CC BY 4.0；casual 对话风格 |
| anna | 🚺 女 | 阅读 | — |
| azelma | 🚺 女 | 阅读 | Les Misérables 角色（年轻明亮） |
| caro_davy | 🚺 女 | 阅读 | — |
| cosette | 🚺 女 | 阅读 | Les Misérables 角色（年轻） |
| eponine | 🚺 女 | 阅读 | Les Misérables 角色（富有表现力） |
| eve | 🚺 女 | 阅读 | — |
| fantine | 🚺 女 | 阅读 | Les Misérables 角色（柔软）；也有法文变体 |
| jane | 🚺 女 | 阅读 | — |
| mary | 🚺 女 | 阅读 | — |
| vera | 🚺 女 | 阅读 | — |
| bill_boerst | 🚹 男 | 阅读 | — |
| charles | 🚹 男 | 阅读 | — |
| george | 🚹 男 | 阅读 | — |
| javert | 🚹 男 | 阅读 | Les Misérables 角色（权威/清晰） |
| jean | 🚹 男 | 阅读 | Les Misérables 角色（温和/自然）；也有法文变体 |
| marius | 🚹 男 | 阅读 | Les Misérables 角色（温暖） |
| michael | 🚹 男 | 阅读 | — |
| paul | 🚹 男 | 阅读 | — |
| peter_yearsley | 🚹 男 | 阅读 | — |
| stuart_bell | 🚹 男 | 阅读 | — |

> 英文共 **21 个内置声音**：11 女 + 10 男。除 alba 明确为「交谈型」外，其余均为通用 TTS（阅读型）。

### 🇮🇹 义大利文（Italian）

| 声音 | 性别 | 型别 | 备注 |
|------|------|------|------|
| **giovanni** | 🚹 男 | 阅读 | 义文唯一内置声音 |

### 🇩🇪 德文（German）

| 声音 | 性别 | 型别 | 备注 |
|------|------|------|------|
| **jürgen** | 🚹 男 | 交谈 | 德文唯一原生内置声音 |

---

## 三、Alba 声音变体（仅 `alba` 有）

`alba` 有 4 个风格变体，位于 HF `kyutai/tts-voices/alba-mackenna/`，需用完整路径调用：

| 变体 | 风格 | 型别 | CLI 用法 |
|------|------|------|----------|
| **casual** | 日常对话 | **交谈** | `--voice "hf://kyutai/tts-voices/alba-mackenna/casual.wav"` |
| merchant | RPG 商人 | 角色 | `--voice "hf://kyutai/tts-voices/alba-mackenna/merchant.wav"` |
| announcer | 竞赛播报 | 角色 | `--voice "hf://kyutai/tts-voices/alba-mackenna/announcer.wav"` |
| a-moment-by | Kinder World 录音 | **交谈** | `--voice "hf://kyutai/tts-voices/alba-mackenna/a-moment-by.wav"` |

> CLI 短名 `--voice alba` 默认映射到 casual 变体。

---

## 四、按语言 × 模型 × 声音的推荐组合

### 德文（本次任务）

| 优先级 | 模型 | 声音 | 性别 | 型别 | 为什么 |
|--------|------|------|------|------|--------|
| ⭐ 首选 | `german` | jürgen | 🚹 男 | 交谈 | 原生德文，速度快，适合批量 2,149 张 |
| ⭐ 高质 | `german_24l` | jürgen | 🚹 男 | 交谈 | 原生德文，音质最高，2,149 张需约 18 小时 |
| 备选 | `german` | alba | 🚺 女 | 交谈 | 女性声音，casual 风格，跨语言可能有口音 |
| 备选 | `german_24l` | alba | 🚺 女 | 交谈 | 女性+高音质，跨语言可能有口音 |

### 义大利文

| 优先级 | 模型 | 声音 | 性别 | 型别 |
|--------|------|------|------|------|
| ⭐ 首选 | `italian` | giovanni | 🚹 男 | 阅读 |
| ⭐ 高质 | `italian_24l` | giovanni | 🚹 男 | 阅读 |
| 备选 | `italian` | alba | 🚺 女 | 交谈 |

### 英文

| 优先级 | 模型 | 声音 | 性别 | 型别 |
|--------|------|------|------|------|
| ⭐ 首选 | `english` | alba | 🚺 女 | 交谈 |
| 备选 | `english` | javert | 🚹 男 | 阅读 |
| 备选 | `english` | jean | 🚹 男 | 阅读 |
| 备选 | `english` | fantine | 🚺 女 | 阅读 |
| … | `english` | (任意 21 个) | — | — |

---

## 五、命令示例

```bash
# 德文 — 原生声音（推荐）
pocket-tts generate --language german --voice juergen --text "Guten Tag." --output-path out.wav

# 德文 — 24 层高质
pocket-tts generate --language german_24l --voice juergen --text "Guten Tag." --output-path out.wav

# 德文 — 跨语言女性声音
pocket-tts generate --language german --voice alba --text "Guten Tag." --output-path out.wav

# 德文 — alba casual 变体（完整 HF 路径）
pocket-tts generate --language german --voice "hf://kyutai/tts-voices/alba-mackenna/casual.wav" --text "Guten Tag." --output-path out.wav

# 义文
pocket-tts generate --language italian_24l --voice giovanni --text "Buongiorno." --output-path out.wav

# 英文
pocket-tts generate --language english --voice alba --text "Hello world." --output-path out.wav
```
