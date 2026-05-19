AXIS_COLS = [
    "visual_hook_power",
    "narrative_engine",
    "character_attachment",
    "emotion_theme_fit",
    "creator_power",
    "platform_serialization_power",
    "social_proof_buzz",
    "transmedia_shortform_fit",
]

DISCOVERY_WEIGHTS = {
    "visual_hook_power": 25,
    "narrative_engine": 20,
    "social_proof_buzz": 20,
    "platform_serialization_power": 15,
    "emotion_theme_fit": 10,
    "creator_power": 10,
}

RETENTION_WEIGHTS = {
    "narrative_engine": 25,
    "character_attachment": 25,
    "emotion_theme_fit": 15,
    "creator_power": 15,
    "platform_serialization_power": 10,
    "social_proof_buzz": 10,
}

EXPANSION_WEIGHTS = {
    "transmedia_shortform_fit": 30,
    "visual_hook_power": 20,
    "character_attachment": 15,
    "narrative_engine": 15,
    "social_proof_buzz": 10,
    "emotion_theme_fit": 10,
}