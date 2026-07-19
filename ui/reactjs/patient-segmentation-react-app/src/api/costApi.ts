import { get } from "./baseApi";
const p="/cost";
export const costApi={
 summary:()=>get(`${p}/summary`), distribution:()=>get(`${p}/distribution`),
 highCostPatients:()=>get(`${p}/high-cost-patients`), topPatients:()=>get(`${p}/top-patients`),
 ageGroup:()=>get(`${p}/age-group`), gender:()=>get(`${p}/gender`), insurance:()=>get(`${p}/insurance`),
 riskCategory:()=>get(`${p}/risk-category`), monthlyTrend:()=>get(`${p}/monthly-trend`),
 payerAnalysis:()=>get(`${p}/payer-analysis`), dashboard:()=>get(`${p}/dashboard`)
};
