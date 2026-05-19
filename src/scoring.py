from __future__ import annotations

import pandas as pd

from src.config import DISCOVERY_WEIGHTS, RETENTION_WEIGHTS, EXPANSION_WEIGHTS


def weighted_score(row: pd.Series, weights: dict[str, float]) -> float:
    total_weight = sum(weights.values())
    score = 0.0

    for col, weight in weights.items():
        value = row.get(col, 0)
        if pd.isna(value):
            value = 0
        score += float(value) * weight

    return round(score / total_weight * 10, 2)


def add_hscores(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()

    result["discovery_score"] = result.apply(
        lambda row: weighted_score(row, DISCOVERY_WEIGHTS), axis=1
    )
    result["retention_score"] = result.apply(
        lambda row: weighted_score(row, RETENTION_WEIGHTS), axis=1
    )
    result["expansion_score"] = result.apply(
        lambda row: weighted_score(row, EXPANSION_WEIGHTS), axis=1
    )

    result["webtoon_hscore"] = (
        result["discovery_score"] * 0.40
        + result["retention_score"] * 0.35
        + result["expansion_score"] * 0.25
    ).round(2)

    return result