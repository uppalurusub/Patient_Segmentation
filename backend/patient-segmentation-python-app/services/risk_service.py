"""
services/risk_service.py
"""

import logging

from implementations.risk_impl import RiskImplementation

logger = logging.getLogger(__name__)


class RiskService:

    def __init__(self):

        self.risk_impl = RiskImplementation()

    # --------------------------------------------------
    # Risk Distribution
    # --------------------------------------------------

    def risk_distribution(self):

        try:

            return self.risk_impl.risk_distribution()

        except Exception as e:

            logger.exception(str(e))

            return {
                "error": str(e)
            }

    # --------------------------------------------------
    # Risk Summary
    # --------------------------------------------------

    def risk_summary(self):

        try:

            return self.risk_impl.risk_summary()

        except Exception as e:

            logger.exception(str(e))

            return {
                "error": str(e)
            }

    # --------------------------------------------------
    # High Risk Patients
    # --------------------------------------------------

    def high_risk_patients(self):

        try:

            return self.risk_impl.high_risk_patients()

        except Exception as e:

            logger.exception(str(e))

            return {
                "error": str(e)
            }

    # --------------------------------------------------
    # Medium Risk Patients
    # --------------------------------------------------

    def medium_risk_patients(self):

        try:

            return self.risk_impl.medium_risk_patients()

        except Exception as e:

            logger.exception(str(e))

            return {
                "error": str(e)
            }

    # --------------------------------------------------
    # Low Risk Patients
    # --------------------------------------------------

    def low_risk_patients(self):

        try:

            return self.risk_impl.low_risk_patients()

        except Exception as e:

            logger.exception(str(e))

            return {
                "error": str(e)
            }

    # --------------------------------------------------
    # Top Risk Patients
    # --------------------------------------------------

    def top_risk_patients(self):

        try:

            return self.risk_impl.top_risk_patients()

        except Exception as e:

            logger.exception(str(e))

            return {
                "error": str(e)
            }

    # --------------------------------------------------
    # Risk By Age Group
    # --------------------------------------------------

    def risk_by_age_group(self):

        try:

            return self.risk_impl.risk_by_age_group()

        except Exception as e:

            logger.exception(str(e))

            return {
                "error": str(e)
            }

    # --------------------------------------------------
    # Risk By Gender
    # --------------------------------------------------

    def risk_by_gender(self):

        try:

            return self.risk_impl.risk_by_gender()

        except Exception as e:

            logger.exception(str(e))

            return {
                "error": str(e)
            }

    # --------------------------------------------------
    # Risk By Insurance
    # --------------------------------------------------

    def risk_by_insurance(self):

        try:

            return self.risk_impl.risk_by_insurance()

        except Exception as e:

            logger.exception(str(e))

            return {
                "error": str(e)
            }

    # --------------------------------------------------
    # Executive Dashboard
    # --------------------------------------------------

    def executive_dashboard(self):

        try:

            return self.risk_impl.executive_dashboard()

        except Exception as e:

            logger.exception(str(e))

            return {
                "error": str(e)
            }