import pandas as pd

from src.scoring import add_hscores
from src.shortform_points import recommend_shortform_points


def main() -> None:
    df = pd.read_csv("data/sample_webtoons.csv", encoding="utf-8")
    scored = add_hscores(df)

    rows = []

    for _, row in scored.iterrows():
        points = recommend_shortform_points(row)

        rows.append({
            "title": row["title"],
            "webtoon_hscore": row["webtoon_hscore"],
            "discovery_score": row["discovery_score"],
            "retention_score": row["retention_score"],
            "expansion_score": row["expansion_score"],
            "shortform_points": " / ".join(points),
        })

    report = pd.DataFrame(rows)
    report.to_csv("outputs/webtoon_hscore_report.csv", index=False)

    with open("outputs/sample_report.md", "w", encoding="utf-8") as f:
        for item in rows:
            f.write(f"# {item['title']}\n\n")
            f.write(f"- Webtoon H-Score: {item['webtoon_hscore']}\n")
            f.write(f"- Discovery: {item['discovery_score']}\n")
            f.write(f"- Retention: {item['retention_score']}\n")
            f.write(f"- Expansion: {item['expansion_score']}\n\n")
            f.write("## Shortform Production Points\n")
            for p in item["shortform_points"].split(" / "):
                f.write(f"- {p}\n")
            f.write("\n---\n\n")


if __name__ == "__main__":
    main()