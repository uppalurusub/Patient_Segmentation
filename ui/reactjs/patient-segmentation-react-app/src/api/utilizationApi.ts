import { get } from "./baseApi";
const p="/utilization";
export const utilizationApi={
 summary:()=>get(`${p}/summary`), visitDistribution:()=>get(`${p}/visit-distribution`),
 topUtilizers:()=>get(`${p}/top-utilizers`), readmissionRate:()=>get(`${p}/readmission-rate`),
 readmittedPatients:()=>get(`${p}/readmitted-patients`), losSummary:()=>get(`${p}/los-summary`),
 losDistribution:()=>get(`${p}/los-distribution`), ageGroup:()=>get(`${p}/age-group`),
 gender:()=>get(`${p}/gender`), insurance:()=>get(`${p}/insurance`),
 riskCategory:()=>get(`${p}/risk-category`), segment:()=>get(`${p}/segment`),
 dashboard:()=>get(`${p}/dashboard`)
};
