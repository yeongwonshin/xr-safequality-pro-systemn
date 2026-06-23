# Annotation Guidelines

## 기본 원칙

- 안전·품질 판정에 필요한 최소 단위로 라벨링한다.
- 객체가 일부 가려져도 작업 판정에 의미가 있으면 라벨링한다.
- 확신이 낮은 경우 `uncertain=true`로 표시하고 리뷰 큐로 보낸다.
- 사람 얼굴, 명찰, 민감 문서는 마스킹 후 저장한다.

## Bounding Box

- 객체의 보이는 영역을 tight box로 표시한다.
- 나사처럼 작은 객체는 확대 뷰를 활용한다.
- 같은 클래스가 여러 개 있으면 모두 표시한다.

## Segmentation

- 금지구역, spill, 폐기 구역은 mask로 라벨링한다.
- 영역 경계가 표식/라인/문서 기준일 때 메타데이터에 기준을 적는다.

## State Label

| 상태 | 정의 |
|---|---|
| present | 객체가 존재함 |
| absent | 필수 객체가 없어야 하는 위치에 없음 |
| worn | PPE가 올바르게 착용됨 |
| not_worn | PPE가 없거나 착용 위치가 잘못됨 |
| open | 커버/밸브/후드 등이 열림 |
| closed | 커버/밸브/후드 등이 닫힘 |
| unknown | 이미지상 판단 불가 |

## Critical Review

Critical 클래스 라벨은 2인 검수 또는 reviewer arbitration을 거친다.

- PPE 착용 여부
- 유해화학물질 라벨
- Lockout/Tagout
- 금지구역 진입
- 전원/압력/고온 상태
