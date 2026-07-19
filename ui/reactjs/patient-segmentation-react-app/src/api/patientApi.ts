import { get } from "./baseApi";
import type { Patient } from "../types/api";
const p="/patients";
export const patientApi={
 kpis:()=>get(`${p}/kpis`), summary:()=>get(`${p}/summary`), all:()=>get<Patient[]>(`${p}/`),
 byId:(id:string)=>get<Patient>(`${p}/${encodeURIComponent(id)}`),
 ageDistribution:()=>get(`${p}/analytics/age-distribution`),
 genderDistribution:()=>get(`${p}/analytics/gender-distribution`),
 insuranceDistribution:()=>get(`${p}/analytics/insurance-distribution`),
 raceDistribution:()=>get(`${p}/analytics/race-distribution`),
 search:(keyword:string)=>get(`${p}/search/${encodeURIComponent(keyword)}`),
 highRisk:()=>get(`${p}/risk/high`), highCost:()=>get(`${p}/cost/high`),
 topUtilizers:()=>get(`${p}/utilization/top`)
};
