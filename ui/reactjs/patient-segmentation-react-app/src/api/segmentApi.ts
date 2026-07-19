import { get, post } from "./baseApi";
import type { SegmentProfile } from "../types/api";
const p="/segments";
export const segmentApi={
 run:()=>post(`${p}/run`), distribution:()=>get(`${p}/distribution`), summary:()=>get(`${p}/summary`),
 profiles:()=>get<SegmentProfile[]>(`${p}/profiles`),
 profile:(id:number)=>get<SegmentProfile>(`${p}/profiles/${id}`),
 costAnalysis:()=>get(`${p}/cost-analysis`), riskAnalysis:()=>get(`${p}/risk-analysis`),
 utilizationAnalysis:()=>get(`${p}/utilization-analysis`), highValue:()=>get(`${p}/high-value`),
 highRisk:()=>get(`${p}/high-risk`), executiveSummary:()=>get(`${p}/executive-summary`)
};
