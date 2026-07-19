"""
services/utilization_service.py
"""

import logging

from implementations.utilization_impl import UtilizationImplementation

logger = logging.getLogger(__name__)


class UtilizationService:

    def __init__(self):

        self.utilization_impl = UtilizationImplementation()

    # --------------------------------------------------
    # Utilization Summary
    # --------------------------------------------------

    def utilization_summary(self):

        try:

            return self.utilization_impl.utilization_summary()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}

    # --------------------------------------------------
    # Visit Distribution
    # --------------------------------------------------

    def visit_distribution(self):

        try:

            return self.utilization_impl.visit_distribution()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}

    # --------------------------------------------------
    # Top Utilizers
    # --------------------------------------------------

    def top_utilizers(self):

        try:

            return self.utilization_impl.top_utilizers()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}

    # --------------------------------------------------
    # Readmission Rate
    # --------------------------------------------------

    def readmission_rate(self):

        try:

            return self.utilization_impl.readmission_rate()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}

    # --------------------------------------------------
    # Readmitted Patients
    # --------------------------------------------------

    def readmitted_patients(self):

        try:

            return self.utilization_impl.readmitted_patients()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}

    # --------------------------------------------------
    # LOS Summary
    # --------------------------------------------------

    def los_summary(self):

        try:

            return self.utilization_impl.los_summary()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}

    # --------------------------------------------------
    # LOS Distribution
    # --------------------------------------------------

    def los_distribution(self):

        try:

            return self.utilization_impl.los_distribution()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}

    # --------------------------------------------------
    # Utilization By Age Group
    # --------------------------------------------------

    def utilization_by_age_group(self):

        try:

            return self.utilization_impl.utilization_by_age_group()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}

    # --------------------------------------------------
    # Utilization By Gender
    # --------------------------------------------------

    def utilization_by_gender(self):

        try:

            return self.utilization_impl.utilization_by_gender()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}

    # --------------------------------------------------
    # Utilization By Insurance
    # --------------------------------------------------

    def utilization_by_insurance(self):

        try:

            return self.utilization_impl.utilization_by_insurance()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}

    # --------------------------------------------------
    # Utilization By Risk Category
    # --------------------------------------------------

    def utilization_by_risk_category(self):

        try:

            return self.utilization_impl.utilization_by_risk_category()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}

    # --------------------------------------------------
    # Utilization By Segment
    # --------------------------------------------------

    def utilization_by_segment(self):

        try:

            return self.utilization_impl.utilization_by_segment()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}

    # --------------------------------------------------
    # Executive Dashboard
    # --------------------------------------------------

    def utilization_dashboard(self):

        try:

            return self.utilization_impl.utilization_dashboard()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}