"""
services/patient_service.py
"""

from implementations.patient_impl import PatientImplementation


class PatientService:

    def __init__(self):
        self.patient_impl = PatientImplementation()

    # --------------------------------------------------
    # Dashboard Summary
    # --------------------------------------------------

    def get_patient_summary(self):

        return self.patient_impl.get_patient_summary()

    # --------------------------------------------------
    # Get All Patients
    # --------------------------------------------------

    def get_all_patients(self):

        return self.patient_impl.get_all_patients()

    # --------------------------------------------------
    # Get Patient By ID
    # --------------------------------------------------

    def get_patient_by_id(
            self,
            patient_id: str
    ):

        return self.patient_impl.get_patient_by_id(
            patient_id
        )

    # --------------------------------------------------
    # Age Distribution
    # --------------------------------------------------

    def age_distribution(self):

        return self.patient_impl.age_distribution()

    # --------------------------------------------------
    # Gender Distribution
    # --------------------------------------------------

    def gender_distribution(self):

        return self.patient_impl.gender_distribution()

    # --------------------------------------------------
    # Insurance Distribution
    # --------------------------------------------------

    def insurance_distribution(self):

        return self.patient_impl.insurance_distribution()

    # --------------------------------------------------
    # Race Distribution
    # --------------------------------------------------

    def race_distribution(self):

        return self.patient_impl.race_distribution()

    

    # --------------------------------------------------
    # Search Patient
    # --------------------------------------------------

    def search_patient(
            self,
            keyword: str
    ):

        return self.patient_impl.search_patient(
            keyword
        )

    # --------------------------------------------------
    # High Risk Patients
    # --------------------------------------------------

    def high_risk_patients(self):

        return self.patient_impl.high_risk_patients()

    # --------------------------------------------------
    # High Cost Patients
    # --------------------------------------------------

    def high_cost_patients(self):

        return self.patient_impl.high_cost_patients()

    # --------------------------------------------------
    # Top Utilizers
    # --------------------------------------------------

    def top_utilizers(self):

        return self.patient_impl.top_utilizers()

    # --------------------------------------------------
    # Population Health KPIs
    # --------------------------------------------------

    def population_kpis(self):

        

        return self.patient_impl.population_kpis()

    # --------------------------------------------------
    # Segment Wise Distribution
    # --------------------------------------------------

    def segment_distribution(self):

        return self.patient_impl.segment_distribution()

    # --------------------------------------------------
    # Segment Summary
    # --------------------------------------------------

    def segment_summary(self):

        return self.patient_impl.segment_summary()

    # --------------------------------------------------
    # Chronic Disease Patients
    # --------------------------------------------------

    def chronic_patients(self):

        return self.patient_impl.chronic_patients()

    # --------------------------------------------------
    # Abnormal Labs Patients
    # --------------------------------------------------

    def abnormal_lab_patients(self):

        return self.patient_impl.abnormal_lab_patients()

    # --------------------------------------------------
    # Executive Dashboard
    # --------------------------------------------------

    def executive_dashboard(self):

        return {

            "patient_summary":
                self.get_patient_summary(),

            "population_kpis":
                self.population_kpis(),

            "segment_distribution":
                self.segment_distribution(),

            "high_risk_patients":
                len(
                    self.high_risk_patients()
                ),

            "high_cost_patients":
                len(
                    self.high_cost_patients()
                )
        }