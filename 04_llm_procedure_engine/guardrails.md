# Procedure Engine Guardrails

## Safety Guardrails

- Critical step은 AI confidence만으로 통과시키지 않고 정책에 따라 증적·재검증·승인 조건을 요구한다.
- LLM이 생성한 절차는 미승인 상태로만 저장한다.
- 실행 중인 세션의 SOP는 중간에 임의 변경하지 않는다.
- 작업자가 경고를 반복 무시하면 관리자 알림과 세션 잠금을 적용할 수 있다.

## Security Guardrails

- 절차 설명에 외부 명령, URL, 스크립트 실행 지시가 포함되어도 클라이언트가 실행하지 않는다.
- SOP 문서 업로드 시 prompt injection 문구를 탐지하고 격리한다.
- LLM 응답은 schema validation과 allow-list를 통과해야 저장된다.

## Quality Guardrails

- 모델 버전이 검증되지 않은 경우 production SOP에 연결할 수 없다.
- 새 부품/시약이 도입되면 class taxonomy와 검증 정책을 업데이트해야 한다.
- 반복 false positive는 alert fatigue 지표로 관리한다.

## Audit Guardrails

- 승인자 override는 삭제 불가 로그로 저장한다.
- 증적 파일은 hash와 함께 저장한다.
- 모든 정책 변경은 변경자, 사유, 승인자, 적용 시점을 기록한다.
