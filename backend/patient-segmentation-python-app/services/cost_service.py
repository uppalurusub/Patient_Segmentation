"""
services/cost_service.py
"""

import logging

from implementations.cost_impl import CostImplementation

logger = logging.getLogger(__name__)


class CostService:

    def __init__(self):

        self.cost_impl = CostImplementation()

    # --------------------------------------------------
    # Cost Summary
    # --------------------------------------------------

    def cost_summary(self):

        try:

            return self.cost_impl.cost_summary()

        except Exception as e:

            logger.exception(str(e))

            return {
                "error": str(e)
            }

    # --------------------------------------------------
    # Cost Distribution
    # --------------------------------------------------

    def cost_distribution(self):

        try:

            return self.cost_impl.cost_distribution()

        except Exception as e:

            logger.exception(str(e))

            return {
                "error": str(e)
            }

    # --------------------------------------------------
    # High Cost Patients
    # --------------------------------------------------

    def high_cost_patients(self):

        try:

            return self.cost_impl.high_cost_patients()

        except Exception as e:

            logger.exception(str(e))

            return {
                "error": str(e)
            }

    # --------------------------------------------------
    # Top Cost Patients
    # --------------------------------------------------

    def top_cost_patients(self):

        try:

            return self.cost_impl.top_cost_patients()

        except Exception as e:

            logger.exception(str(e))

            return {
                "error": str(e)
            }

    # --------------------------------------------------
    # Cost By Age Group
    # --------------------------------------------------

    def cost_by_age_group(self):

        try:

            return self.cost_impl.cost_by_age_group()

        except Exception as e:

            logger.exception(str(e))

            return {
                "error": str(e)
            }

    # --------------------------------------------------
    # Cost By Gender
    # --------------------------------------------------

    def cost_by_gender(self):

        try:

            return self.cost_impl.cost_by_gender()

        except Exception as e:

            logger.exception(str(e))

            return {
                "error": str(e)
            }

    # --------------------------------------------------
    # Cost By Insurance
    # --------------------------------------------------

    def cost_by_insurance(self):

        try:

            return self.cost_impl.cost_by_insurance()

        except Exception as e:

            logger.exception(str(e))

            return {
                "error": str(e)
            }

    # --------------------------------------------------
    # Cost By Risk Category
    # --------------------------------------------------

    def cost_by_risk_category(self):

        try:

            return self.cost_impl.cost_by_risk_category()

        except Exception as e:

            logger.exception(str(e))

            return {
                "error": str(e)
            }

    

    # --------------------------------------------------
    # Monthly Cost Trend
    # --------------------------------------------------

    def monthly_cost_trend(self):

        try:

            return self.cost_impl.monthly_cost_trend()

        except Exception as e:

            logger.exception(str(e))

            return {
                "error": str(e)
            }

    # --------------------------------------------------
    # Payer Analysis
    # --------------------------------------------------

    def payer_analysis(self):

        try:

            return self.cost_impl.payer_analysis()

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

            return self.cost_impl.executive_dashboard()

        except Exception as e:

            logger.exception(str(e))

            return {
                "error": str(e)
            }