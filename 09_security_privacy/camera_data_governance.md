# Camera Data Governance

## Capture Modes

| Mode | 저장 데이터 | 사용처 |
|---|---|---|
| Metadata Only | 객체/상태/좌표/confidence | 기본 운영 통계 |
| Snapshot Evidence | 이벤트 순간 이미지 | 감사/품질 증적 |
| Short Clip | 사건 전후 짧은 영상 | 중대 사고 조사 |
| Full Video | 전체 영상 | 기본 비권장, 특수 계약 필요 |

## Redaction

- 얼굴 blur
- 명찰/개인정보 blur
- 화면/문서 영역 blur
- 고객 지정 공정기밀 영역 mask

## Customer Controls

- 저장 모드 선택
- 보존기간 설정
- 학습 데이터 사용 opt-in/out
- 테넌트별 암호화 키
- export 제한과 워터마크

## Evidence Integrity

- 원본/마스킹본 hash 별도 저장
- 마스킹 알고리즘 버전 기록
- evidence access log 저장
- 삭제/보존기간 변경 audit event 생성
