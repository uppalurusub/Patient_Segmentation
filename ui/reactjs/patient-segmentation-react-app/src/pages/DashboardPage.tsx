import { AnalyticsPage } from "../components/common/AnalyticsPage"; 
import { dashboardApi } from "../api/dashboardApi";
export function DashboardPage(){
  return <AnalyticsPage title="Executive Dashboard" request={dashboardApi.executive}/>
}
