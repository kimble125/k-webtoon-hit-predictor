# k-webtoon-hit-predictor

웹툰 강점을 8축으로 점수화하고, 강한 축을 **AI 웹툰 숏폼 생성 입력·템플릿 추천·프롬프트·QA 기준**으로 변환하는 서비스 기획형 PoC입니다.

## Why this repo exists
좋은 AI 숏폼은 단순히 “예쁘게 생성된 영상”이 아닙니다.  
원작의 정체성을 보존하면서도, 플랫폼 문법에 맞게 후킹되고, 사람이 다시 편집할 수 있어야 합니다.

이 리포지토리는 그 판단을 감이 아니라 구조로 바꾸기 위해 만들었습니다.

## Core question
AI가 좋은 웹툰 숏폼을 만들거나 보조하려면,
어떤 기준을 입력·템플릿·프롬프트·QA로 구조화해야 하는가?

## Current scope
- 웹툰 강점 8축 점수화
- discovery / retention / expansion score 계산
- 템플릿 추천
- 프롬프트 스켈레톤 생성
- QA 루브릭 기반 평가
- Evidence Bank 문서화

## Eight axes
- visual_hook_power
- narrative_engine
- character_attachment
- emotion_theme_fit
- creator_power
- platform_serialization_power
- social_proof_buzz
- transmedia_shortform_fit

## Repo philosophy
이 리포는 “영상 생성 엔진”이 아니라 **AI 숏폼 기획 엔진**입니다.

- `k-webtoon-hit-predictor`
  - 웹툰 강점 분석
  - 템플릿 추천
  - 프롬프트 구조화
  - QA 기준 생성

별도의 생성 repo(예: Remotion / CapCut / AI video automation)는 이후 실행 레이어로 분리할 수 있습니다.

## Pipeline
1. 작품별 8축 점수를 입력한다.
2. 상위 축 조합으로 템플릿을 추천한다.
3. 템플릿별 입력 슬롯을 채워 프롬프트를 만든다.
4. AI가 생성한 결과물을 9개 QA 항목으로 검수한다.
5. 결과를 Evidence Bank와 함께 축적한다.

## Folder guide
```text
data/
  sample_webtoons.csv
  template_catalog.csv
  qa_test_cases.csv

src/
  config.py
  scoring.py
  shortform_points.py
  template_recommender.py
  qa_evaluator.py

docs/
  qa_rubric.md
  template_catalog.md
  evidence_bank.md

outputs/
  template_recommendations.csv
  qa_evaluation_sample.csv
