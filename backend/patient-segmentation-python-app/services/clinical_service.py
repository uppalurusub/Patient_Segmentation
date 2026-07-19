"""
services/clinical_service.py
"""

import logging

from implementations.clinical_impl import ClinicalImplementation

logger = logging.getLogger(__name__)


class ClinicalService:

    def __init__(self):

        self.clinical_impl = ClinicalImplementation()

    # --------------------------------------------------
    # Clinical Summary
    # --------------------------------------------------

    def clinical_summary(self):

        try:

            return self.clinical_impl.clinical_summary()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}

    # --------------------------------------------------
    # Top Diagnoses
    # --------------------------------------------------

    def top_diagnoses(self):

        try:

            return self.clinical_impl.top_diagnoses()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}

    # --------------------------------------------------
    # Disease Prevalence
    # --------------------------------------------------

    def disease_prevalence(self):

        try:

            return self.clinical_impl.disease_prevalence()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}

    # --------------------------------------------------
    # Chronic Patients
    # --------------------------------------------------

    def chronic_patients(self):

        try:

            return self.clinical_impl.chronic_patients()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}

    # --------------------------------------------------
    # Comorbidity Distribution
    # --------------------------------------------------

    def comorbidity_distribution(self):

        try:

            return self.clinical_impl.comorbidity_distribution()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}

    # --------------------------------------------------
    # Abnormal Labs
    # --------------------------------------------------

    def abnormal_labs(self):

        try:

            return self.clinical_impl.abnormal_labs()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}

    # --------------------------------------------------
    # Diabetes Prevalence
    # --------------------------------------------------

    def diabetes_prevalence(self):

        try:

            return self.clinical_impl.diabetes_prevalence()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}

    # --------------------------------------------------
    # Hypertension Prevalence
    # --------------------------------------------------

    def hypertension_prevalence(self):

        try:

            return self.clinical_impl.hypertension_prevalence()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}

    # --------------------------------------------------
    # CKD Prevalence
    # --------------------------------------------------

    def ckd_prevalence(self):

        try:

            return self.clinical_impl.ckd_prevalence()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}

    # --------------------------------------------------
    # Heart Failure Prevalence
    # --------------------------------------------------

    def heart_failure_prevalence(self):

        try:

            return self.clinical_impl.heart_failure_prevalence()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}

    # --------------------------------------------------
    # Clinical Risk Indicators
    # --------------------------------------------------

    def clinical_risk_indicators(self):

        try:

            return self.clinical_impl.clinical_risk_indicators()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}

    # --------------------------------------------------
    # Clinical Dashboard
    # --------------------------------------------------

    def clinical_dashboard(self):

        try:

            return self.clinical_impl.clinical_dashboard()

        except Exception as e:

            logger.exception(str(e))

            return {"error": str(e)}