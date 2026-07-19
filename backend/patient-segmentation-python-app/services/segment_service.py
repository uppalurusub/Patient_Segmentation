"""
services/segment_service.py
"""

from implementations.segment_impl import SegmentImplementation


class SegmentService:

    def __init__(self):

        self.segment_impl = SegmentImplementation()

    # --------------------------------------------------
    # Run Segmentation
    # --------------------------------------------------

    def run_segmentation(self):

        return self.segment_impl.run_segmentation()

    # --------------------------------------------------
    # Segment Distribution
    # --------------------------------------------------

    def segment_distribution(self):

        return self.segment_impl.segment_distribution()

    # --------------------------------------------------
    # Segment Summary
    # --------------------------------------------------

    def segment_summary(self):

        return self.segment_impl.segment_summary()

    # --------------------------------------------------
    # Segment Profiles
    # --------------------------------------------------

    def segment_profiles(self):

        return self.segment_impl.segment_profiles()

    # --------------------------------------------------
    # Single Segment Profile
    # --------------------------------------------------

    def segment_profile(
            self,
            segment_id: int
    ):

        return self.segment_impl.segment_profile(
            segment_id
        )

    # --------------------------------------------------
    # Cost Analysis
    # --------------------------------------------------

    def segment_cost_analysis(self):

        return self.segment_impl.segment_cost_analysis()

    # --------------------------------------------------
    # Risk Analysis
    # --------------------------------------------------

    def segment_risk_analysis(self):

        return self.segment_impl.segment_risk_analysis()

    # --------------------------------------------------
    # Utilization Analysis
    # --------------------------------------------------

    def segment_utilization_analysis(self):

        return self.segment_impl.segment_utilization_analysis()

    # --------------------------------------------------
    # High Value Segment
    # --------------------------------------------------

    def high_value_segment(self):

        return self.segment_impl.high_value_segment()

    # --------------------------------------------------
    # High Risk Segment
    # --------------------------------------------------

    def high_risk_segment(self):

        return self.segment_impl.high_risk_segment()

    # --------------------------------------------------
    # Executive Summary
    # --------------------------------------------------

    def executive_summary(self):

        return self.segment_impl.executive_summary()