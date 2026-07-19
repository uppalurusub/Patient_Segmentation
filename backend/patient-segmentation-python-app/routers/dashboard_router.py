"""
routers/dashboard_router.py
"""

from fastapi import APIRouter

from services.dashboard_service import DashboardService

router = APIRouter(
    prefix="/dashboard",
    tags=["Executive Dashboard"]
)

dashboard_service = DashboardService()

# --------------------------------------------------
# Executive Dashboard
# --------------------------------------------------

@router.get("/")
def executive_dashboard():

    return dashboard_service.executive_dashboard()


# --------------------------------------------------
# Population Dashboard
# --------------------------------------------------

@router.get("/population")
def population_dashboard():

    return dashboard_service.population_dashboard()


# --------------------------------------------------
# Clinical Dashboard
# --------------------------------------------------

@router.get("/clinical")
def clinical_dashboard():

    return dashboard_service.clinical_dashboard()


# --------------------------------------------------
# Risk Dashboard
# --------------------------------------------------

@router.get("/risk")
def risk_dashboard():

    return dashboard_service.risk_dashboard()


# --------------------------------------------------
# Cost Dashboard
# --------------------------------------------------

@router.get("/cost")
def cost_dashboard():

    return dashboard_service.cost_dashboard()


# --------------------------------------------------
# Utilization Dashboard
# --------------------------------------------------

@router.get("/utilization")
def utilization_dashboard():

    return dashboard_service.utilization_dashboard()


# --------------------------------------------------
# Segmentation Dashboard
# --------------------------------------------------

@router.get("/segments")
def segmentation_dashboard():

    return dashboard_service.segmentation_dashboard()


# --------------------------------------------------
# Executive KPI Summary
# --------------------------------------------------

@router.get("/kpis")
def executive_kpis():

    return dashboard_service.executive_kpis()


# --------------------------------------------------
# CEO Summary
# --------------------------------------------------

@router.get("/ceo-summary")
def ceo_summary():

    return dashboard_service.ceo_summary()