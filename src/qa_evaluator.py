from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Dict, List
import pandas as pd

QA_WEIGHTS: Dict[str, float] = {
    "hooking": 0.15,
    "story_clarity": 0.15,
    "identity_preservation": 0.15,
    "visual_consistency": 0.10,
    "subtitle_readability": 0.10,
    "platform_fit": 0.10,
    "template_reusability": 0.10,
    "editability": 0.10,
    "risk": 0.05,
}

ESSENTIAL_ITEMS = ["story_clarity", "identity_preservation", "risk"]


@dataclass
class QAEvaluation:
    title: str
    template_name: str
    hooking: int
    story_clarity: int
    identity_preservation: int
    visual_consistency: int
    subtitle_readability: int
    platform_fit: int
    template_reusability: int
    editability: int
    risk: int
    reviewer_note: str = ""

    def to_dict(self) -> Dict[str, object]:
        data = asdict(self)
        data["qa_total_score"] = self.total_score()
        data["decision"] = self.decision()
        return data

    def total_score(self) -> float:
        weighted = 0.0
        for key, weight in QA_WEIGHTS.items():
            value = getattr(self, key)
            weighted += value * weight
        return round(weighted * 20, 2)  # 5점 척도 -> 100점 환산

    def essential_guard_failed(self) -> bool:
        return any(getattr(self, key) <= 2 for key in ESSENTIAL_ITEMS)

    def decision(self) -> str:
        score = self.total_score()

        if self.risk <= 2 or self.story_clarity <= 2:
            return "reject"

        if score >= 85 and not self.essential_guard_failed():
            return "publish"

        if score >= 70:
            return "revise"

        return "reject"


def evaluate_dataframe(evaluations: List[QAEvaluation]) -> pd.DataFrame:
    rows = [item.to_dict() for item in evaluations]
    return pd.DataFrame(rows)


if __name__ == "__main__":
    sample = [
        QAEvaluation(
            title="유미의 세포들",
            template_name="Emotion Cell Alert",
            hooking=4,
            story_clarity=4,
            identity_preservation=5,
            visual_consistency=4,
            subtitle_readability=5,
            platform_fit=4,
            template_reusability=4,
            editability=5,
            risk=4,
            reviewer_note="감정선 전달 우수. 장면 전환은 더 단순화 가능.",
        ),
        QAEvaluation(
            title="전지적 독자 시점",
            template_name="3-Second Cliffhanger",
            hooking=5,
            story_clarity=4,
            identity_preservation=4,
            visual_consistency=4,
            subtitle_readability=4,
            platform_fit=5,
            template_reusability=4,
            editability=4,
            risk=4,
            reviewer_note="후킹 강함. 자막 밀도 약간 높음.",
        ),
    ]

    df = evaluate_dataframe(sample)
    df.to_csv("outputs/qa_evaluation_sample.csv", index=False, encoding="utf-8-sig")
    print("saved: outputs/qa_evaluation_sample.csv")
