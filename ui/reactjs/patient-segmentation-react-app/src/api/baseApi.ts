import { httpClient } from "./httpClient";
import type { ApiValue } from "../types/api";

export async function get<T extends ApiValue = ApiValue>(url: string): Promise<T> {
  const { data } = await httpClient.get<T>(url);
  return data;
}
export async function post<T extends ApiValue = ApiValue>(url: string): Promise<T> {
  const { data } = await httpClient.post<T>(url);
  return data;
}
