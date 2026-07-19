import type { ApiValue } from "../../types/api";
import { formatValue, label } from "../../utils/formatters";

export function DataView({data}:{data:ApiValue}) {
 if(Array.isArray(data)){
   if(data.length===0) return <p>No data available.</p>;
   const objects=data.filter((v):v is Record<string,ApiValue>=>typeof v==="object"&&v!==null&&!Array.isArray(v));
   if(objects.length===data.length){
     const keys=Array.from(new Set(objects.flatMap(Object.keys)));
     return <div className="table-wrap"><table><thead><tr>{keys.map(k=><th key={k}>{label(k)}</th>)}</tr></thead>
       <tbody>{objects.map((row,i)=><tr key={i}>{keys.map(k=><td key={k}>{typeof row[k]==="object" ? JSON.stringify(row[k]) : formatValue(row[k])}</td>)}</tr>)}</tbody></table></div>;
   }
   return <ul>{data.map((v,i)=><li key={i}>{typeof v==="object" ? JSON.stringify(v) : formatValue(v)}</li>)}</ul>;
 }
 if(typeof data==="object"&&data!==null){
   return <div className="grid">{Object.entries(data).map(([k,v])=><article className="card" key={k}><span>{label(k)}</span><strong>{typeof v==="object" ? <DataView data={v}/> : formatValue(v)}</strong></article>)}</div>;
 }
 return <strong>{formatValue(data)}</strong>;
}
