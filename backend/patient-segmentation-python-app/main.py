"""
main.py

Patient Segmentation Analytics API
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.patient_router import router as patient_router
from routers.segment_router import router as segment_router
from routers.risk_router import router as risk_router
from routers.cost_router import router as cost_router
from routers.clinical_router import router as clinical_router
from routers.utilization_router import router as utilization_router
from routers.dashboard_router import router as dashboard_router






# --------------------------------------------------
# FastAPI Application
# --------------------------------------------------

app = FastAPI(
    title="Patient Segmentation Analytics API",
    description="""
    Enterprise Healthcare Analytics Platform

    Modules:
    - Patient Analytics
    - Clinical Analytics
    - Cost Analytics
    - Utilization Analytics
    - Risk Stratification
    - Patient Segmentation
    - Predictive Analytics
    """,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)


# --------------------------------------------------
# CORS Configuration
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# --------------------------------------------------
# Register Routers
# --------------------------------------------------

app.include_router(patient_router)
app.include_router(segment_router)
app.include_router(risk_router)
app.include_router(cost_router)
app.include_router(clinical_router)
app.include_router(utilization_router)
app.include_router(dashboard_router)


# --------------------------------------------------
# Root Endpoint
# --------------------------------------------------

@app.get("/")
def home():

    return {
        "application":
            "Patient Segmentation Analytics Platform",

        "version":
            "1.0.0",

        "status":
            "Running",

        "modules": [

            "Patient Analytics",
            "Clinical Analytics",
            "Cost Analytics",
            "Risk Analytics",
            "Utilization Analytics",
            "Patient Segmentation",
            "Predictive Analytics"
        ]
    }


# --------------------------------------------------
# Health Check
# --------------------------------------------------

@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }


# --------------------------------------------------
# API Information
# --------------------------------------------------

@app.get("/info")
def api_info():

    return {

        "project":
            "Patient Segmentation Analytics",

        "environment":
            "Development",

        "author":
            "Healthcare Analytics Team",

        "api_version":
            "v1"
    }


