"""
routers/cost_router.py
"""

from fastapi import APIRouter

from services.cost_service import CostService

router = APIRouter(
    prefix="/cost",
    tags=["Cost Analytics"]
)

cost_service = CostService()

# --------------------------------------------------
# Cost Summary
# --------------------------------------------------

@router.get("/summary")
def cost_summary():

    return cost_service.cost_summary()


# --------------------------------------------------
# Cost Distribution
# --------------------------------------------------

@router.get("/distribution")
def cost_distribution():

    return cost_service.cost_distribution()


# --------------------------------------------------
# High Cost Patients
# --------------------------------------------------

@router.get("/high-cost-patients")
def high_cost_patients():

    return cost_service.high_cost_patients()


# --------------------------------------------------
# Top Cost Patients
# --------------------------------------------------

@router.get("/top-patients")
def top_cost_patients():

    return cost_service.top_cost_patients()


# --------------------------------------------------
# Cost By Age Group
# --------------------------------------------------

@router.get("/age-group")
def cost_by_age_group():

    return cost_service.cost_by_age_group()


# --------------------------------------------------
# Cost By Gender
# --------------------------------------------------

@router.get("/gender")
def cost_by_gender():

    return cost_service.cost_by_gender()


# --------------------------------------------------
# Cost By Insurance
# --------------------------------------------------

@router.get("/insurance")
def cost_by_insurance():

    return cost_service.cost_by_insurance()


# --------------------------------------------------
# Cost By Risk Category
# --------------------------------------------------

@router.get("/risk-category")
def cost_by_risk_category():

    return cost_service.cost_by_risk_category()





# --------------------------------------------------
# Monthly Cost Trend
# --------------------------------------------------

@router.get("/monthly-trend")
def monthly_cost_trend():

    return cost_service.monthly_cost_trend()


# --------------------------------------------------
# Payer Mix Cost Analysis
# --------------------------------------------------

@router.get("/payer-analysis")
def payer_analysis():

    return cost_service.payer_analysis()


# --------------------------------------------------
# Executive Dashboard
# --------------------------------------------------

@router.get("/dashboard")
def executive_dashboard():

    return cost_service.executive_dashboard()