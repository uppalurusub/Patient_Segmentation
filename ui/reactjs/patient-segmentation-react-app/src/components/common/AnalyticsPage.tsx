import { useCallback } from "react";
import type { ApiValue } from "../../types/api";
import { useApi } from "../../hooks/useApi";
import { DataView } from "./DataView";
import { ErrorMessage } from "./ErrorMessage";
import { Loading } from "./Loading";

export function AnalyticsPage({title,request}:{title:string;request:()=>Promise<ApiValue>}){
 const stableRequest=useCallback(request,[request]);
 const {data,loading,error,refetch}=useApi(stableRequest);
 return <section><div className="page-title"><div><h1>{title}</h1><p>Healthcare analytics and population insights</p></div><button onClick={()=>void refetch()}>Refresh</button></div>
 {loading?<Loading/>:error?<ErrorMessage message={error}/>:data!==null?<DataView data={data}/>:null}</section>;
}
