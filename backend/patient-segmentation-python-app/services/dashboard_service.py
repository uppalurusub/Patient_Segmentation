"""
services/dashboard_service.py
"""

import logging

from implementations.dashboard_impl import DashboardImplementation

logger = logging.getLogger(__name__)


class DashboardService:

    def __init__(self):

        self.dashboard_impl = DashboardImplementation()

    # --------------------------------------------------
    # Executive Dashboard
    # --------------------------------------------------

    def executive_dashboard(self):

        try:

            return self.dashboard_impl.executive_dashboard()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}

    # --------------------------------------------------
    # Population Dashboard
    # --------------------------------------------------

    def population_dashboard(self):

        try:

            return self.dashboard_impl.population_dashboard()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}

    # --------------------------------------------------
    # Clinical Dashboard
    # --------------------------------------------------

    def clinical_dashboard(self):

        try:

            return self.dashboard_impl.clinical_dashboard()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}

    # --------------------------------------------------
    # Risk Dashboard
    # --------------------------------------------------

    def risk_dashboard(self):

        try:

            return self.dashboard_impl.risk_dashboard()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}

    # --------------------------------------------------
    # Cost Dashboard
    # --------------------------------------------------

    def cost_dashboard(self):

        try:

            return self.dashboard_impl.cost_dashboard()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}

    # --------------------------------------------------
    # Utilization Dashboard
    # --------------------------------------------------

    def utilization_dashboard(self):

        try:

            return self.dashboard_impl.utilization_dashboard()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}

    # --------------------------------------------------
    # Segmentation Dashboard
    # --------------------------------------------------

    def segmentation_dashboard(self):

        try:

            return self.dashboard_impl.segmentation_dashboard()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}

    # --------------------------------------------------
    # Executive KPIs
    # --------------------------------------------------

    def executive_kpis(self):

        try:

            return self.dashboard_impl.executive_kpis()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}

    # --------------------------------------------------
    # CEO Summary
    # --------------------------------------------------

    def ceo_summary(self):

        try:

            return self.dashboard_impl.ceo_summary()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}