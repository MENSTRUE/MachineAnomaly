import type { Prediction } from '../types';
export function ScoreChart({items}:{items:Prediction[]}) {
  const nums = items.slice(0,80).map(x=>x.anomaly_score ?? x.confidence_proxy ?? 0);
  if(!nums.length) return <div className="empty">Upload CSV to visualize model output.</div>;
  const lo=Math.min(...nums), hi=Math.max(...nums), span=Math.max(hi-lo, 0.00001);
  const points=nums.map((v,i)=>`${18+(i/Math.max(nums.length-1,1))*744},${182-(v-lo)/span*145}`).join(' ');
  return <svg className="chart" viewBox="0 0 780 210" role="img" aria-label="Prediction scores over uploaded rows"><line x1="18" x2="764" y1="182" y2="182" stroke="#415069"/><line x1="18" x2="18" y1="22" y2="182" stroke="#415069"/><polyline fill="none" stroke="#84efcf" strokeWidth="2.5" strokeLinejoin="round" points={points}/><text x="20" y="205" fill="#93a4b8" fontSize="12">Row 1</text><text x="680" y="205" fill="#93a4b8" fontSize="12">Row {nums.length}</text></svg>;
}
