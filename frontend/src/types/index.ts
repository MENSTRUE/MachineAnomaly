export type Kind = 'hydraulic' | 'ims';
export type Models = {hydraulic: Record<string,boolean>; ims: Record<string,boolean>; model_directory:string};
export type Prediction = {row_index:number; target?:string; test?:string; predicted_class?:number; confidence_proxy?:number; anomaly_score?:number; threshold?:number; alarm?:boolean; interpretation?:string};
export type PredictionResponse = {kind:Kind;target:string;total:number;results:Prediction[]};
