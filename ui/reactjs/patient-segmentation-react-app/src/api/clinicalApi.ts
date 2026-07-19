import { get } from "./baseApi";
const p="/clinical";
export const clinicalApi={
 summary:()=>get(`${p}/summary`), topDiagnoses:()=>get(`${p}/top-diagnoses`),
 diseasePrevalence:()=>get(`${p}/disease-prevalence`), chronicPatients:()=>get(`${p}/chronic-patients`),
 comorbidity:()=>get(`${p}/comorbidity`), abnormalLabs:()=>get(`${p}/abnormal-labs`),
 diabetes:()=>get(`${p}/diabetes`), hypertension:()=>get(`${p}/hypertension`), ckd:()=>get(`${p}/ckd`),
 heartFailure:()=>get(`${p}/heart-failure`), riskIndicators:()=>get(`${p}/risk-indicators`),
 dashboard:()=>get(`${p}/dashboard`)
};
