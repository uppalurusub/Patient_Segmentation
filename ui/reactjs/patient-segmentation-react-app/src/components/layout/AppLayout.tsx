import { NavLink, Outlet } from "react-router-dom";
const links=[["/","Executive"],["/patients","Patients"],["/clinical","Clinical"],["/risk","Risk"],["/cost","Cost"],["/utilization","Utilization"],["/segments","Segments"]];
export function AppLayout(){return <div className="shell"><aside><h2>Healthcare<br/>Analytics</h2><nav>{links.map(([to,name])=><NavLink key={to} to={to} end={to==="/"}>{name}</NavLink>)}</nav></aside><main><Outlet/></main></div>}
