"""
implementations/clinical_impl.py
"""

import pandas as pd

from utils.loader import DataLoader
from utils.preprocessing import DataPreprocessor


class ClinicalImplementation:

    def __init__(self):

        loader = DataLoader()

        data = loader.load_all()

        self.patients = data["patients"]
        self.encounters = data["encounters"]
        self.diagnoses = data["diagnoses"]
        self.claims = data["claims"]
        self.labs = data["labs"]

        preprocessor = DataPreprocessor()

        self.master_df = (
            preprocessor.create_master_dataset(
                self.patients,
                self.encounters,
                self.diagnoses,
                self.claims,
                self.labs
            )
        )

    # --------------------------------------------------
    # Clinical Summary
    # --------------------------------------------------

    def clinical_summary(self):

        total_patients = (
            self.master_df["patient_id"]
            .nunique()
        )

        chronic_patients = len(
            self.chronic_patients()
        )

        abnormal_patients = (
            self.labs[
                self.labs["abnormal_flag"] == 1
            ]["patient_id"]
            .nunique()
        )

        return {

            "total_patients":
                int(total_patients),

            "chronic_patients":
                int(chronic_patients),

            "abnormal_lab_patients":
                int(abnormal_patients)
        }

    # --------------------------------------------------
    # Top Diagnoses
    # --------------------------------------------------

    def top_diagnoses(self):

        result = (

            self.diagnoses[
                "primary_diagnosis"
            ]

            .value_counts()

            .head(10)

            .reset_index()
        )

        result.columns = [
            "diagnosis",
            "count"
        ]

        return result.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Disease Prevalence
    # --------------------------------------------------

    def disease_prevalence(self):

        total_patients = (
            self.master_df["patient_id"]
            .nunique()
        )

        prevalence = (

            self.diagnoses

            .groupby(
                "primary_diagnosis"
            )["patient_id"]

            .nunique()

            .reset_index()
        )

        prevalence["prevalence_pct"] = (

            prevalence["patient_id"]

            / total_patients

            * 100

        ).round(2)

        prevalence.rename(
            columns={
                "primary_diagnosis":
                    "diagnosis",
                "patient_id":
                    "patient_count"
            },
            inplace=True
        )

        prevalence = (
            prevalence
            .sort_values(
                "patient_count",
                ascending=False
            )
            .head(20)
        )

        return prevalence.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Chronic Disease Patients
    # --------------------------------------------------

    def chronic_patients(self):

        df = self.master_df[
            self.master_df[
                "diagnosis_count"
            ] >= 3
        ]

        return df.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Comorbidity Distribution
    # --------------------------------------------------

    def comorbidity_distribution(self):

        patient_dx = (

            self.diagnoses

            .groupby("patient_id")

            .size()

            .reset_index(
                name="comorbidity_count"
            )
        )

        result = (

            patient_dx

            .groupby(
                "comorbidity_count"
            )

            .size()

            .reset_index(
                name="patients"
            )
        )

        return result.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Abnormal Labs
    # --------------------------------------------------

    def abnormal_labs(self):

        total_labs = len(self.labs)

        abnormal_labs = len(

            self.labs[
                self.labs[
                    "abnormal_flag"
                ] == 1
            ]
        )

        abnormal_pct = round(
            abnormal_labs
            / total_labs * 100,
            2
        )

        return {

            "total_lab_results":
                int(total_labs),

            "abnormal_lab_results":
                int(abnormal_labs),

            "abnormal_lab_percentage":
                abnormal_pct
        }

    # --------------------------------------------------
    # Diabetes Prevalence
    # --------------------------------------------------

    def diabetes_prevalence(self):

        return self._disease_metric(
            "diabetes"
        )

    # --------------------------------------------------
    # Hypertension Prevalence
    # --------------------------------------------------

    def hypertension_prevalence(self):

        return self._disease_metric(
            "hypertension"
        )

    # --------------------------------------------------
    # CKD Prevalence
    # --------------------------------------------------

    def ckd_prevalence(self):

        return self._disease_metric(
            "ckd"
        )

    # --------------------------------------------------
    # Heart Failure Prevalence
    # --------------------------------------------------

    def heart_failure_prevalence(self):

        return self._disease_metric(
            "heart failure"
        )

    # --------------------------------------------------
    # Generic Disease Metric
    # --------------------------------------------------

    def _disease_metric(
            self,
            disease_name
    ):

        total_patients = (
            self.master_df["patient_id"]
            .nunique()
        )

        disease_patients = (

            self.diagnoses[

                self.diagnoses[
                    "primary_diagnosis"
                ]

                .str.contains(
                    disease_name,
                    case=False,
                    na=False
                )
            ]

            ["patient_id"]

            .nunique()
        )

        prevalence_pct = round(

            disease_patients

            / total_patients

            * 100,

            2
        )

        return {

            "disease":
                disease_name.title(),

            "patient_count":
                int(disease_patients),

            "prevalence_pct":
                prevalence_pct
        }

    # --------------------------------------------------
    # Clinical Risk Indicators
    # --------------------------------------------------

    def clinical_risk_indicators(self):

        return {

            "chronic_patients":
                len(
                    self.chronic_patients()
                ),

            "abnormal_lab_patients":

                int(
                    self.labs[
                        self.labs[
                            "abnormal_flag"
                        ] == 1
                    ]
                    ["patient_id"]
                    .nunique()
                ),

            "multi_morbidity_patients":

                int(
                    len(
                        self.master_df[
                            self.master_df[
                                "diagnosis_count"
                            ] >= 3
                        ]
                    )
                )
        }

    # --------------------------------------------------
    # Clinical Dashboard
    # --------------------------------------------------

    def clinical_dashboard(self):

        return {

            "clinical_summary":
                self.clinical_summary(),

            "top_diagnoses":
                self.top_diagnoses(),

            "clinical_risk_indicators":
                self.clinical_risk_indicators(),

            "abnormal_labs":
                self.abnormal_labs(),

            "diabetes":
                self.diabetes_prevalence(),

            "hypertension":
                self.hypertension_prevalence(),

            "ckd":
                self.ckd_prevalence()
        }