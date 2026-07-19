"""
routers/risk_router.py
"""

from fastapi import APIRouter

from services.risk_service import RiskService

router = APIRouter(
    prefix="/risk",
    tags=["Risk Analytics"]
)

risk_service = RiskService()

# --------------------------------------------------
# Risk Distribution
# --------------------------------------------------

@router.get("/distribution")
def risk_distribution():

    return risk_service.risk_distribution()


# --------------------------------------------------
# Risk Summary
# --------------------------------------------------

@router.get("/summary")
def risk_summary():

    return risk_service.risk_summary()


# --------------------------------------------------
# High Risk Patients
# --------------------------------------------------

@router.get("/high")
def high_risk_patients():

    return risk_service.high_risk_patients()


# --------------------------------------------------
# Medium Risk Patients
# --------------------------------------------------

@router.get("/medium")
def medium_risk_patients():

    return risk_service.medium_risk_patients()


# --------------------------------------------------
# Low Risk Patients
# --------------------------------------------------

@router.get("/low")
def low_risk_patients():

    return risk_service.low_risk_patients()


# --------------------------------------------------
# Top Risk Patients
# --------------------------------------------------

@router.get("/top")
def top_risk_patients():

    return risk_service.top_risk_patients()


# --------------------------------------------------
# Risk By Age Group
# --------------------------------------------------

@router.get("/age-group")
def risk_by_age_group():

    return risk_service.risk_by_age_group()


# --------------------------------------------------
# Risk By Gender
# --------------------------------------------------

@router.get("/gender")
def risk_by_gender():

    return risk_service.risk_by_gender()


# --------------------------------------------------
# Risk By Insurance
# --------------------------------------------------

@router.get("/insurance")
def risk_by_insurance():

    return risk_service.risk_by_insurance()


# --------------------------------------------------
# Executive Dashboard
# --------------------------------------------------

@router.get("/dashboard")
def executive_dashboard():

    return risk_service.executive_dashboard()