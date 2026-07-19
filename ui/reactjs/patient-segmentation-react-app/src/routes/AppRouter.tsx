import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { AppLayout } from "../components/layout/AppLayout";
import { DashboardPage } from "../pages/DashboardPage"; import { PatientPage } from "../pages/PatientPage";
import { ClinicalPage } from "../pages/ClinicalPage"; import { RiskPage } from "../pages/RiskPage";
import { CostPage } from "../pages/CostPage"; import { UtilizationPage } from "../pages/UtilizationPage";
import { SegmentPage } from "../pages/SegmentPage";
const router=createBrowserRouter([{path:"/",element:<AppLayout/>,children:[
 {index:true,element:<DashboardPage/>},{path:"patients",element:<PatientPage/>},{path:"clinical",element:<ClinicalPage/>},
 {path:"risk",element:<RiskPage/>},{path:"cost",element:<CostPage/>},{path:"utilization",element:<UtilizationPage/>},
 {path:"segments",element:<SegmentPage/>}
]}]);
export function AppRouter(){return <RouterProvider router={router}/>}
