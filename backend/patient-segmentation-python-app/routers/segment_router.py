"""
routers/segment_router.py
"""

from fastapi import APIRouter
from services.segment_service import SegmentService

router = APIRouter(
    prefix="/segments",
    tags=["Patient Segmentation"]
)

segment_service = SegmentService()


# --------------------------------------------------
# Run Segmentation
# --------------------------------------------------

@router.post("/run")
def run_segmentation():

    return segment_service.run_segmentation()


# --------------------------------------------------
# Segment Distribution
# --------------------------------------------------

@router.get("/distribution")
def segment_distribution():

    return segment_service.segment_distribution()


# --------------------------------------------------
# Segment Summary
# --------------------------------------------------

@router.get("/summary")
def segment_summary():

    return segment_service.segment_summary()


# --------------------------------------------------
# All Segment Profiles
# --------------------------------------------------

@router.get("/profiles")
def segment_profiles():

    return segment_service.segment_profiles()


# --------------------------------------------------
# Single Segment Profile
# --------------------------------------------------

@router.get("/profiles/{segment_id}")
def segment_profile(segment_id: int):

    return segment_service.segment_profile(
        segment_id
    )


# --------------------------------------------------
# Segment Cost Analysis
# --------------------------------------------------

@router.get("/cost-analysis")
def segment_cost_analysis():

    return segment_service.segment_cost_analysis()


# --------------------------------------------------
# Segment Risk Analysis
# --------------------------------------------------

@router.get("/risk-analysis")
def segment_risk_analysis():

    return segment_service.segment_risk_analysis()


# --------------------------------------------------
# Segment Utilization Analysis
# --------------------------------------------------

@router.get("/utilization-analysis")
def segment_utilization_analysis():

    return segment_service.segment_utilization_analysis()


# --------------------------------------------------
# High Value Segment
# --------------------------------------------------

@router.get("/high-value")
def high_value_segment():

    return segment_service.high_value_segment()


# --------------------------------------------------
# High Risk Segment
# --------------------------------------------------

@router.get("/high-risk")
def high_risk_segment():

    return segment_service.high_risk_segment()


# --------------------------------------------------
# Executive Summary
# --------------------------------------------------

@router.get("/executive-summary")
def executive_summary():

    return segment_service.executive_summary()