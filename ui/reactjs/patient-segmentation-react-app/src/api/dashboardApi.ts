import { get } from "./baseApi";
const p="/dashboard";
export const dashboardApi={
 executive:()=>get(`${p}/`), population:()=>get(`${p}/population`), clinical:()=>get(`${p}/clinical`),
 risk:()=>get(`${p}/risk`), cost:()=>get(`${p}/cost`), utilization:()=>get(`${p}/utilization`),
 segments:()=>get(`${p}/segments`), kpis:()=>get(`${p}/kpis`), ceoSummary:()=>get(`${p}/ceo-summary`)
};
