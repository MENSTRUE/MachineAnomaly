import type { Kind, Models, PredictionResponse } from '../types';
async function decode<T>(response: Response): Promise<T> {
  if (!response.ok) {
    const payload = await response.json().catch(() => ({detail: response.statusText}));
    throw new Error(typeof payload.detail === 'string' ? payload.detail : JSON.stringify(payload.detail ?? payload));
  }
  return response.json() as Promise<T>;
}
export async function health(): Promise<{status:string}> { return decode(await fetch('/api/v1/health')); }
export async function models(): Promise<Models> { return decode(await fetch('/api/v1/models')); }
export async function uploadCSV(file: File, kind: Kind, target: string): Promise<PredictionResponse> {
  const data = new FormData(); data.append('file', file);
  return decode(await fetch(`/api/v1/predict/csv?kind=${encodeURIComponent(kind)}&target=${encodeURIComponent(target)}`, {method:'POST',body:data}));
}
