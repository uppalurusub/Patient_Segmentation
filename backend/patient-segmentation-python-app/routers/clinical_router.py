"""
routers/clinical_router.py
"""

from fastapi import APIRouter

from services.clinical_service import ClinicalService

router = APIRouter(
    prefix="/clinical",
    tags=["Clinical Analytics"]
)



clinical_service = ClinicalService()

# --------------------------------------------------
# Clinical Summary
# --------------------------------------------------

@router.get("/summary")
def clinical_summary():

    
    return clinical_service.clinical_summary()


# --------------------------------------------------
# Top Diagnoses
# --------------------------------------------------

@router.get("/top-diagnoses")
def top_diagnoses():

    
    return clinical_service.top_diagnoses()


# --------------------------------------------------
# Disease Prevalence
# --------------------------------------------------

@router.get("/disease-prevalence")
def disease_prevalence():
    

    return clinical_service.disease_prevalence()


# --------------------------------------------------
# Chronic Disease Patients
# --------------------------------------------------

@router.get("/chronic-patients")
def chronic_patients():

    return clinical_service.chronic_patients()


# --------------------------------------------------
# Comorbidity Distribution
# --------------------------------------------------

@router.get("/comorbidity")
def comorbidity_distribution():

    return clinical_service.comorbidity_distribution()


# --------------------------------------------------
# Abnormal Lab Summary
# --------------------------------------------------

@router.get("/abnormal-labs")
def abnormal_labs():

    return clinical_service.abnormal_labs()


# --------------------------------------------------
# Diabetes Prevalence
# --------------------------------------------------

@router.get("/diabetes")
def diabetes_prevalence():

    return clinical_service.diabetes_prevalence()


# --------------------------------------------------
# Hypertension Prevalence
# --------------------------------------------------

@router.get("/hypertension")
def hypertension_prevalence():

    return clinical_service.hypertension_prevalence()


# --------------------------------------------------
# CKD Prevalence
# --------------------------------------------------

@router.get("/ckd")
def ckd_prevalence():

    return clinical_service.ckd_prevalence()


# --------------------------------------------------
# Heart Failure Prevalence
# --------------------------------------------------

@router.get("/heart-failure")
def heart_failure_prevalence():

    return clinical_service.heart_failure_prevalence()


# --------------------------------------------------
# Clinical Risk Indicators
# --------------------------------------------------

@router.get("/risk-indicators")
def clinical_risk_indicators():

    return clinical_service.clinical_risk_indicators()


# --------------------------------------------------
# Clinical Dashboard
# --------------------------------------------------

@router.get("/dashboard")
def clinical_dashboard():

    return clinical_service.clinical_dashboard()