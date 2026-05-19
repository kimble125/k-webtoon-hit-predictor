SHORTFORM_RULES = {
    "visual_hook_power": "첫 1.5초에 표정, 액션, 강한 구도의 컷을 배치한다.",
    "narrative_engine": "갈등이 시작되는 순간이나 회차 말미 클리프행어를 중심으로 구성한다.",
    "character_attachment": "캐릭터 관계성, 팬덤형 대사, 감정 반응을 전면에 둔다.",
    "emotion_theme_fit": "공감, 위로, 통쾌함, 긴장감 중 가장 강한 정서를 카피로 만든다.",
    "creator_power": "작가 전작이나 작가 브랜드를 추천 카피에 활용한다.",
    "platform_serialization_power": "연재 요일, 회차 누적, 정주행 가능성을 CTA로 활용한다.",
    "social_proof_buzz": "댓글 반응, 별점, 독자 반응을 숏폼 카피의 신뢰 근거로 사용한다.",
    "transmedia_shortform_fit": "드라마화, 애니화, 컷츠 전환 가능 장면을 중심으로 홍보한다.",
}


def recommend_shortform_points(row, top_n: int = 3) -> list[str]:
    axis_scores = {
        axis: row.get(axis, 0)
        for axis in SHORTFORM_RULES.keys()
    }

    top_axes = sorted(axis_scores, key=axis_scores.get, reverse=True)[:top_n]

    return [
        f"{axis}: {SHORTFORM_RULES[axis]}"
        for axis in top_axes
    ]