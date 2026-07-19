"""
routers/utilization_router.py
"""

from fastapi import APIRouter

from services.utilization_service import UtilizationService

router = APIRouter(
    prefix="/utilization",
    tags=["Utilization Analytics"]
)

utilization_service = UtilizationService()

# --------------------------------------------------
# Utilization Summary
# --------------------------------------------------

@router.get("/summary")
def utilization_summary():

    return utilization_service.utilization_summary()


# --------------------------------------------------
# Visit Distribution
# --------------------------------------------------

@router.get("/visit-distribution")
def visit_distribution():

    return utilization_service.visit_distribution()


# --------------------------------------------------
# Top Utilizers
# --------------------------------------------------

@router.get("/top-utilizers")
def top_utilizers():

    return utilization_service.top_utilizers()


# --------------------------------------------------
# Readmission Rate
# --------------------------------------------------

@router.get("/readmission-rate")
def readmission_rate():

    return utilization_service.readmission_rate()


# --------------------------------------------------
# Readmitted Patients
# --------------------------------------------------

@router.get("/readmitted-patients")
def readmitted_patients():

    return utilization_service.readmitted_patients()


# --------------------------------------------------
# Length Of Stay Summary
# --------------------------------------------------

@router.get("/los-summary")
def los_summary():

    return utilization_service.los_summary()


# --------------------------------------------------
# LOS Distribution
# --------------------------------------------------

@router.get("/los-distribution")
def los_distribution():

    return utilization_service.los_distribution()


# --------------------------------------------------
# Utilization By Age Group
# --------------------------------------------------

@router.get("/age-group")
def utilization_by_age_group():

    return utilization_service.utilization_by_age_group()


# --------------------------------------------------
# Utilization By Gender
# --------------------------------------------------

@router.get("/gender")
def utilization_by_gender():

    return utilization_service.utilization_by_gender()


# --------------------------------------------------
# Utilization By Insurance
# --------------------------------------------------

@router.get("/insurance")
def utilization_by_insurance():

    return utilization_service.utilization_by_insurance()


# --------------------------------------------------
# Utilization By Risk Category
# --------------------------------------------------

@router.get("/risk-category")
def utilization_by_risk_category():

    return utilization_service.utilization_by_risk_category()


# --------------------------------------------------
# Utilization By Segment
# --------------------------------------------------

@router.get("/segment")
def utilization_by_segment():

    return utilization_service.utilization_by_segment()


# --------------------------------------------------
# Executive Dashboard
# --------------------------------------------------

@router.get("/dashboard")
def utilization_dashboard():

    return utilization_service.utilization_dashboard()