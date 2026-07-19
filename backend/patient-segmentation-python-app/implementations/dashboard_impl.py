"""
implementations/dashboard_impl.py
"""

from implementations.patient_impl import (
    PatientImplementation
)

from implementations.clinical_impl import (
    ClinicalImplementation
)

from implementations.risk_impl import (
    RiskImplementation
)

from implementations.cost_impl import (
    CostImplementation
)

from implementations.utilization_impl import (
    UtilizationImplementation
)

from implementations.segment_impl import (
    SegmentImplementation
)


class DashboardImplementation:

    def __init__(self):

        self.patient_impl = (
            PatientImplementation()
        )

        self.clinical_impl = (
            ClinicalImplementation()
        )

        self.risk_impl = (
            RiskImplementation()
        )

        self.cost_impl = (
            CostImplementation()
        )

        self.utilization_impl = (
            UtilizationImplementation()
        )

        self.segment_impl = (
            SegmentImplementation()
        )

        # Ensure segmentation exists
        self.segment_impl.run_segmentation()

    # --------------------------------------------------
    # Enterprise Dashboard
    # --------------------------------------------------

    def executive_dashboard(self):

        return {

            "population":
                self.population_dashboard(),

            "clinical":
                self.clinical_dashboard(),

            "risk":
                self.risk_dashboard(),

            "cost":
                self.cost_dashboard(),

            "utilization":
                self.utilization_dashboard(),

            "segmentation":
                self.segmentation_dashboard()
        }

    # --------------------------------------------------
    # Population Dashboard
    # --------------------------------------------------

    def population_dashboard(self):

        return {

            "patient_summary":
                self.patient_impl
                .get_patient_summary(),

            "population_kpis":
                self.patient_impl
                .population_kpis(),

            "age_distribution":
                self.patient_impl
                .age_distribution(),

            "gender_distribution":
                self.patient_impl
                .gender_distribution()
        }

    # --------------------------------------------------
    # Clinical Dashboard
    # --------------------------------------------------

    def clinical_dashboard(self):

        return {

            "clinical_summary":
                self.clinical_impl
                .clinical_summary(),

            "top_diagnoses":
                self.clinical_impl
                .top_diagnoses(),

            "abnormal_labs":
                self.clinical_impl
                .abnormal_labs(),

            "clinical_risk_indicators":
                self.clinical_impl
                .clinical_risk_indicators()
        }

    # --------------------------------------------------
    # Risk Dashboard
    # --------------------------------------------------

    def risk_dashboard(self):

        return {

            "risk_summary":
                self.risk_impl
                .risk_summary(),

            "risk_distribution":
                self.risk_impl
                .risk_distribution(),

            "high_risk_patients":
                len(
                    self.risk_impl
                    .high_risk_patients()
                )
        }

    # --------------------------------------------------
    # Cost Dashboard
    # --------------------------------------------------

    def cost_dashboard(self):

        return {

            "cost_summary":
                self.cost_impl
                .cost_summary(),

            "high_cost_patients":
                len(
                    self.cost_impl
                    .high_cost_patients()
                ),

            "payer_analysis":
                self.cost_impl
                .payer_analysis()
        }

    # --------------------------------------------------
    # Utilization Dashboard
    # --------------------------------------------------

    def utilization_dashboard(self):

        return {

            "utilization_summary":
                self.utilization_impl
                .utilization_summary(),

            "readmission_rate":
                self.utilization_impl
                .readmission_rate(),

            "los_summary":
                self.utilization_impl
                .los_summary()
        }

    # --------------------------------------------------
    # Segmentation Dashboard
    # --------------------------------------------------

    def segmentation_dashboard(self):

        return {

            "segment_distribution":
                self.segment_impl
                .segment_distribution(),

            "segment_summary":
                self.segment_impl
                .segment_summary(),

            "high_value_segment":
                self.segment_impl
                .high_value_segment(),

            "high_risk_segment":
                self.segment_impl
                .high_risk_segment()
        }

    # --------------------------------------------------
    # Executive KPI Summary
    # --------------------------------------------------

    def executive_kpis(self):

        population = (
            self.patient_impl.population_kpis()
        )

        cost = (
            self.cost_impl.cost_summary()
        )

        risk = (
            self.risk_impl.risk_distribution()
        )

        utilization = (
            self.utilization_impl
            .utilization_summary()
        )

        return {

            "total_patients":
                population.get(
                    "total_patients", 0
                ),

            "avg_age":
                population.get(
                    "avg_age", 0
                ),

            "total_cost":
                cost.get(
                    "total_cost", 0
                ),

            "average_cost":
                cost.get(
                    "average_cost", 0
                ),

            "average_visits":
                population.get(
                    "avg_visits", 0
                ),

            "readmission_rate_pct":
                utilization.get(
                    "readmission_rate_pct",
                    0
                ),

            "risk_distribution":
                risk
        }

    # --------------------------------------------------
    # CEO Summary
    # --------------------------------------------------

    def ceo_summary(self):

        cost = (
            self.cost_impl.cost_summary()
        )

        utilization = (
            self.utilization_impl
            .utilization_summary()
        )

        risk = (
            self.risk_impl
            .high_risk_patients()
        )

        return {

            "total_patients":

                self.patient_impl
                .population_kpis()
                .get(
                    "total_patients",
                    0
                ),

            "high_risk_patients":
                len(risk),

            "total_cost":
                cost.get(
                    "total_cost",
                    0
                ),

            "readmission_rate_pct":
                utilization.get(
                    "readmission_rate_pct",
                    0
                ),

            "recommended_actions": [

                "Target high-risk patients",

                "Reduce avoidable readmissions",

                "Expand chronic disease management",

                "Focus on high-cost patient outreach",

                "Implement care coordination"
            ]
        }