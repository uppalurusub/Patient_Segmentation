"""
routers/patient_router.py
"""

from fastapi import APIRouter
from services.patient_service import PatientService

router = APIRouter(
    prefix="/patients",
    tags=["Patient Analytics"]
)

patient_service = PatientService()

# --------------------------------------------------
# Population Health KPIs
# --------------------------------------------------

@router.get("/kpis")
def population_kpis():

    

    return patient_service.population_kpis()

# --------------------------------------------------
# Dashboard Summary
# --------------------------------------------------

@router.get("/summary")
def get_patient_summary():

    return patient_service.get_patient_summary()


# --------------------------------------------------
# All Patients
# --------------------------------------------------

@router.get("/")
def get_all_patients():

    return patient_service.get_all_patients()


# --------------------------------------------------
# Patient By ID
# --------------------------------------------------

@router.get("/{patient_id}")
def get_patient_by_id(patient_id: str):

    return patient_service.get_patient_by_id(
        patient_id
    )


# --------------------------------------------------
# Age Distribution
# --------------------------------------------------

@router.get("/analytics/age-distribution")
def age_distribution():

    return patient_service.age_distribution()


# --------------------------------------------------
# Gender Distribution
# --------------------------------------------------

@router.get("/analytics/gender-distribution")
def gender_distribution():

    return patient_service.gender_distribution()


# --------------------------------------------------
# Insurance Distribution
# --------------------------------------------------

@router.get("/analytics/insurance-distribution")
def insurance_distribution():

    return patient_service.insurance_distribution()


# --------------------------------------------------
# Race Distribution
# --------------------------------------------------

@router.get("/analytics/race-distribution")
def race_distribution():

    return patient_service.race_distribution()




# --------------------------------------------------
# Search Patients
# --------------------------------------------------

@router.get("/search/{keyword}")
def search_patient(keyword: str):

    return patient_service.search_patient(
        keyword
    )


# --------------------------------------------------
# High Risk Patients
# --------------------------------------------------

@router.get("/risk/high")
def high_risk_patients():

    return patient_service.high_risk_patients()


# --------------------------------------------------
# High Cost Patients
# --------------------------------------------------

@router.get("/cost/high")
def high_cost_patients():

    return patient_service.high_cost_patients()


# --------------------------------------------------
# Top Utilizers
# --------------------------------------------------

@router.get("/utilization/top")
def top_utilizers():

    return patient_service.top_utilizers()


