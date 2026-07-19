import { useCallback, useEffect, useState } from "react";

export function useApi<T>(request:()=>Promise<T>) {
  const [data,setData]=useState<T|null>(null);
  const [loading,setLoading]=useState(true);
  const [error,setError]=useState<string|null>(null);

  const execute=useCallback(async()=>{
    setLoading(true); setError(null);
    try { setData(await request()); }
    catch(e){ setError(e instanceof Error ? e.message : "Unexpected error"); }
    finally { setLoading(false); }
  },[request]);

  useEffect(()=>{ void execute(); },[execute]);
  return {data,loading,error,refetch:execute};
}
