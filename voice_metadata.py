"""
Voice Metadata Registry
Maps voice_id → language, gender, conversation/reading style, accent info.
Source: Kyutai official page (kyutai.org/blog/2026-01-13-pocket-tts) + user testing.
"""

# ── Language codes & display ──────────────────────────────────────────
LANG = {
    "en": {"flag": "", "label": "English"},
    "de": {"flag": "🇩🇪", "label": "German"},
    "it": {"flag": "🇮🇹", "label": "Italian"},
    "fr": {"flag": "🇫🇷", "label": "French"},
    "es": {"flag": "🇪🇸", "label": "Spanish"},
    "pt": {"flag": "🇵🇹", "label": "Portuguese (BR)"},
}

# ── Gender display ─────────────────────────────────────────────────────
GENDER = {
    "m": {"emoji": "🚹", "label": "Male"},
    "f": {"emoji": "🚺", "label": "Female"},
}

# ── Style display ──────────────────────────────────────────────────────
STYLE = {
    "conversation": {"emoji": "💬", "label": "Conversation"},
    "reading": {"emoji": "📖", "label": "Reading"},
}

# ── Master voice metadata ──────────────────────────────────────────────
# Format: voice_id → {language, gender, style, non_rhotic, notes}
#   language:    "en"|"de"|"it"|"fr"|"es"|"pt"
#   gender:      "m"|"f"
#   style:       "conversation"|"reading"|None (non-English: unclassified)
#   non_rhotic:  True if user-tested British English without rhotic 'r'
#   notes:       free-text (character origin, speed benchmark, etc.)

VOICE_META = {
    # ── English — Conversation (10) ────────────────────────────────
    "jane": {
        "language": "en", "gender": "f", "style": "conversation",
        "non_rhotic": False, "notes": "",
    },
    "anna": {
        "language": "en", "gender": "f", "style": "conversation",
        "non_rhotic": True, "notes": "Non-rhotic British (0.540s)",
    },
    "charles": {
        "language": "en", "gender": "m", "style": "conversation",
        "non_rhotic": True, "notes": "Non-rhotic British (0.583s)",
    },
    "eve": {
        "language": "en", "gender": "f", "style": "conversation",
        "non_rhotic": False, "notes": "",
    },
    "george": {
        "language": "en", "gender": "m", "style": "conversation",
        "non_rhotic": False, "notes": "",
    },
    "mary": {
        "language": "en", "gender": "f", "style": "conversation",
        "non_rhotic": False, "notes": "",
    },
    "michael": {
        "language": "en", "gender": "m", "style": "conversation",
        "non_rhotic": False, "notes": "",
    },
    "paul": {
        "language": "en", "gender": "m", "style": "conversation",
        "non_rhotic": True, "notes": "Non-rhotic British (0.588s)",
    },
    "vera": {
        "language": "en", "gender": "f", "style": "conversation",
        "non_rhotic": True, "notes": "Non-rhotic British (0.668s)",
    },
    "jean": {
        "language": "en", "gender": "m", "style": "conversation",
        "non_rhotic": False, "notes": "Les Misérables character",
    },

    # ── English — Reading (10) ────────────────────────────────────
    "alba": {
        "language": "en", "gender": "m", "style": "reading",
        "non_rhotic": False, "notes": "Default voice; user-tested: male",
    },
    "bill-boerst": {
        "language": "en", "gender": "m", "style": "reading",
        "non_rhotic": False, "notes": "",
    },
    "caro-davy": {
        "language": "en", "gender": "f", "style": "reading",
        "non_rhotic": True, "notes": "Non-rhotic British (0.560s)",
    },
    "peter-yearsley": {
        "language": "en", "gender": "m", "style": "reading",
        "non_rhotic": True, "notes": "Non-rhotic British; fastest (0.699s)",
    },
    "stuart-bell": {
        "language": "en", "gender": "m", "style": "reading",
        "non_rhotic": True, "notes": "Non-rhotic British (0.595s)",
    },
    "azelma": {
        "language": "en", "gender": "f", "style": "reading",
        "non_rhotic": False, "notes": "Les Misérables character",
    },
    "eponine": {
        "language": "en", "gender": "f", "style": "reading",
        "non_rhotic": False, "notes": "Les Misérables character",
    },
    "fantine": {
        "language": "en", "gender": "f", "style": "reading",
        "non_rhotic": True, "notes": "Non-rhotic British (0.645s); Les Misérables",
    },
    "cosette": {
        "language": "en", "gender": "f", "style": "reading",
        "non_rhotic": False, "notes": "Les Misérables; not on Kyutai page; embedding exists",
    },
    "javert": {
        "language": "en", "gender": "m", "style": "reading",
        "non_rhotic": False, "notes": "Les Misérables; not on Kyutai page; embedding exists",
    },
    "marius": {
        "language": "en", "gender": "m", "style": "reading",
        "non_rhotic": False, "notes": "Les Misérables; not on Kyutai page; embedding exists",
    },

    # ── Non-English (5) — style unclassified ───────────────────────
    "estelle": {
        "language": "fr", "gender": "f", "style": None,
        "non_rhotic": False, "notes": "Native French",
    },
    "giovanni": {
        "language": "it", "gender": "m", "style": None,
        "non_rhotic": False, "notes": "Native Italian",
    },
    "juergen": {
        "language": "de", "gender": "m", "style": None,
        "non_rhotic": False, "notes": "Native German",
    },
    "lola": {
        "language": "es", "gender": "f", "style": None,
        "non_rhotic": False, "notes": "Native Spanish",
    },
    "rafael": {
        "language": "pt", "gender": "m", "style": None,
        "non_rhotic": False, "notes": "Native Brazilian Portuguese",
    },
}


def enrich_voice(voice: dict) -> dict:
    """
    Enrich a single voice dict from the API with metadata fields.
    Modifies the dict in-place and also returns it.
    """
    voice_id = voice.get("voice_id", "")
    meta = VOICE_META.get(voice_id, {})

    lang_code = meta.get("language", "en")
    gender_code = meta.get("gender", "m")
    style_code = meta.get("style")

    lang_info = LANG.get(lang_code, LANG["en"])
    gender_info = GENDER.get(gender_code, GENDER["m"])
    style_info = STYLE.get(style_code, {}) if style_code else {}

    voice["language_code"] = lang_code
    voice["language_flag"] = lang_info["flag"]
    voice["language_label"] = lang_info["label"]
    voice["gender"] = gender_code
    voice["gender_emoji"] = gender_info["emoji"]
    voice["gender_label"] = gender_info["label"]
    voice["style"] = style_code
    voice["style_emoji"] = style_info.get("emoji", "")
    voice["style_label"] = style_info.get("label", "")
    voice["non_rhotic"] = meta.get("non_rhotic", False)
    voice["notes"] = meta.get("notes", "")

    # Build tags array for filter UI
    tags = [lang_code]
    if style_code:
        tags.append(style_code)
    if voice["non_rhotic"]:
        tags.append("non-rhotic")
    elif lang_code == "en":
        tags.append("rhotic")
    tags.append(gender_code)
    voice["tags"] = tags

    return voice


def enrich_voice_list(voices: list) -> list:
    """Enrich a list of voice dicts with metadata."""
    return [enrich_voice(v) for v in voices]
