from __future__ import annotations

from typing import Dict, List, Tuple
import pandas as pd

TEMPLATE_RULES: Dict[str, List[str]] = {
    "Emotion Cell Alert": ["character_attachment", "emotion_theme_fit"],
    "3-Second Cliffhanger": ["narrative_engine", "platform_serialization_power"],
    "Character Chemistry Teaser": ["character_attachment", "social_proof_buzz"],
    "Visual Impact Cut": ["visual_hook_power", "creator_power"],
    "Comment-Bait Question": ["social_proof_buzz", "platform_serialization_power"],
    "OSMU Bridge": ["transmedia_shortform_fit", "creator_power"],
}


def _avg_score(row: pd.Series, axes: List[str]) -> float:
    values = [float(row.get(axis, 0) or 0) for axis in axes]
    return round(sum(values) / len(values), 2)


def recommend_templates(row: pd.Series, top_n: int = 2) -> List[Tuple[str, float]]:
    scored: List[Tuple[str, float]] = []
    for template_name, axes in TEMPLATE_RULES.items():
        scored.append((template_name, _avg_score(row, axes)))
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:top_n]


def build_template_recommendations(df: pd.DataFrame, top_n: int = 2) -> pd.DataFrame:
    results = []
    for _, row in df.iterrows():
        recs = recommend_templates(row, top_n=top_n)
        for rank, (template_name, template_score) in enumerate(recs, start=1):
            results.append(
                {
                    "title": row["title"],
                    "rank": rank,
                    "template_name": template_name,
                    "template_score": template_score,
                }
            )
    return pd.DataFrame(results)


if __name__ == "__main__":
    df = pd.read_csv("data/sample_webtoons.csv")
    result = build_template_recommendations(df, top_n=2)
    result.to_csv("outputs/template_recommendations.csv", index=False, encoding="utf-8-sig")
    print("saved: outputs/template_recommendations.csv")
