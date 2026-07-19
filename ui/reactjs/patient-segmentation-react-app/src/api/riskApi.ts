import { get } from "./baseApi";
const p="/risk";
export const riskApi={
 distribution:()=>get(`${p}/distribution`), summary:()=>get(`${p}/summary`), high:()=>get(`${p}/high`),
 medium:()=>get(`${p}/medium`), low:()=>get(`${p}/low`), top:()=>get(`${p}/top`),
 ageGroup:()=>get(`${p}/age-group`), gender:()=>get(`${p}/gender`), insurance:()=>get(`${p}/insurance`),
 dashboard:()=>get(`${p}/dashboard`)
};
