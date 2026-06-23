# ROI Calculator

## Input Variables

```text
monthly_sessions
baseline_defect_rate
post_defect_rate
cost_per_defect
baseline_incidents
post_incidents
cost_per_incident
reporting_hours_saved
hourly_labor_cost
monthly_subscription_fee
setup_fee_amortized_monthly
```

## Formula

```text
defect_savings = monthly_sessions * (baseline_defect_rate - post_defect_rate) * cost_per_defect
incident_savings = (baseline_incidents - post_incidents) * cost_per_incident
labor_savings = reporting_hours_saved * hourly_labor_cost
monthly_roi = defect_savings + incident_savings + labor_savings - monthly_subscription_fee - setup_fee_amortized_monthly
roi_ratio = monthly_roi / (monthly_subscription_fee + setup_fee_amortized_monthly)
```

## Example

```text
monthly_sessions = 5,000
baseline_defect_rate = 1.5%
post_defect_rate = 1.0%
cost_per_defect = 80,000 KRW
reporting_hours_saved = 80h
hourly_labor_cost = 40,000 KRW
monthly_subscription_fee = 8,000,000 KRW
setup_fee_amortized_monthly = 2,000,000 KRW

결과:
defect_savings = 2,000만원
labor_savings = 320만원
monthly_roi = 1,320만원
```

## Notes

- 실제 가격/비용은 산업별 편차가 크다.
- 안전사고 비용은 직접비보다 간접비가 큰 경우가 많아 고객별 conservative/base/aggressive 시나리오를 분리한다.
- 품질 불량은 lot 폐기, 재작업, 라인 정지, 고객 클레임 비용을 분리해 산정한다.
