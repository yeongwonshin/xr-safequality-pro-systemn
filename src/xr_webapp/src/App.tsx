import React, { useState } from 'react';

const steps = [
  '시약 라벨 확인',
  '보호구 착용 확인',
  '장비 세팅 확인',
  '폐기 절차 확인'
];

export default function App() {
  const [step, setStep] = useState(0);
  const [status, setStatus] = useState<'idle'|'pass'|'blocked'|'uncertain'>('idle');

  const simulateCheck = () => {
    if (step === 1) setStatus('blocked');
    else setStatus('pass');
  };

  return (
    <main style={{ fontFamily: 'system-ui', padding: 24 }}>
      <h1>XR SafeQuality 작업 세션</h1>
      <section style={{ border: '1px solid #ddd', padding: 16, borderRadius: 12 }}>
        <p>현재 단계 {step + 1}/{steps.length}</p>
        <h2>{steps[step]}</h2>
        <div style={{ height: 280, background: '#111', color: '#fff', display: 'grid', placeItems: 'center', borderRadius: 12 }}>
          Camera / XR View
        </div>
        <p>상태: {status}</p>
        {status === 'blocked' && <p>필수 조건이 확인되지 않았습니다. 수정 후 다시 검사하세요.</p>}
        <button onClick={simulateCheck}>AI 검사 실행</button>
        <button disabled={status !== 'pass'} onClick={() => { setStep(Math.min(step + 1, steps.length - 1)); setStatus('idle'); }}>
          다음 단계
        </button>
      </section>
    </main>
  );
}
