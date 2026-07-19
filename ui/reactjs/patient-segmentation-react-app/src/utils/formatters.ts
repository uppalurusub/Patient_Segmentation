export const label=(value:string)=>value.replaceAll("_"," ").replace(/\b\w/g,c=>c.toUpperCase());
export const formatValue=(value:unknown):string=>{
 if(value===null||value===undefined) return "—";
 if(typeof value==="number") return value.toLocaleString();
 if(typeof value==="boolean") return value ? "Yes" : "No";
 return String(value);
};
