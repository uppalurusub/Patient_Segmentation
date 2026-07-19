"""
implementations/risk_impl.py
"""

import pandas as pd

from utils.loader import DataLoader
from utils.preprocessing import DataPreprocessor


class RiskImplementation:

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

        self.calculate_risk_score()

    # --------------------------------------------------
    # Risk Score
    # --------------------------------------------------

    def calculate_risk_score(self):

        self.master_df["risk_score"] = (

            self.master_df["age"] * 0.20 +

            self.master_df["visit_count"] * 5 +

            self.master_df["diagnosis_count"] * 10 +

            self.master_df["abnormal_lab_count"] * 8
        )

        self.master_df["risk_category"] = pd.cut(

            self.master_df["risk_score"],

            bins=[
                -1,
                30,
                60,
                9999
            ],

            labels=[
                "Low",
                "Medium",
                "High"
            ]
        )

    # --------------------------------------------------
    # Risk Distribution
    # --------------------------------------------------

    def risk_distribution(self):

        risk_df = (

            self.master_df["risk_category"]

            .value_counts()

            .sort_index()

            .reset_index()
        )

        risk_df.columns = [
            "risk_category",
            "count"
        ]

        return risk_df.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Risk Score Summary
    # --------------------------------------------------

    def risk_summary(self):

        return {

            "average_risk_score":
                round(
                    self.master_df[
                        "risk_score"
                    ].mean(),
                    2
                ),

            "maximum_risk_score":
                round(
                    self.master_df[
                        "risk_score"
                    ].max(),
                    2
                ),

            "minimum_risk_score":
                round(
                    self.master_df[
                        "risk_score"
                    ].min(),
                    2
                )
        }

    # --------------------------------------------------
    # High Risk Patients
    # --------------------------------------------------

    def high_risk_patients(self):

        df = self.master_df[

            self.master_df[
                "risk_category"
            ] == "High"
        ]

        return df.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Medium Risk Patients
    # --------------------------------------------------

    def medium_risk_patients(self):

        df = self.master_df[

            self.master_df[
                "risk_category"
            ] == "Medium"
        ]

        return df.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Low Risk Patients
    # --------------------------------------------------

    def low_risk_patients(self):

        df = self.master_df[

            self.master_df[
                "risk_category"
            ] == "Low"
        ]

        return df.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Top Risk Patients
    # --------------------------------------------------

    def top_risk_patients(self):

        df = (

            self.master_df

            .sort_values(
                "risk_score",
                ascending=False
            )

            .head(20)
        )

        return df.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Risk by Age Group
    # --------------------------------------------------

    def risk_by_age_group(self):

        age_group = pd.cut(

            self.master_df["age"],

            bins=[0, 18, 35, 50, 65, 120],

            labels=[
                "0-18",
                "19-35",
                "36-50",
                "51-65",
                "65+"
            ]
        )

        self.master_df["age_group"] = age_group

        result = (

            self.master_df

            .groupby("age_group")

            ["risk_score"]

            .mean()

            .round(2)

            .reset_index()
        )

        result.columns = [
            "age_group",
            "average_risk_score"
        ]

        return result.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Risk by Gender
    # --------------------------------------------------

    def risk_by_gender(self):

        result = (

            self.master_df

            .groupby("gender")

            ["risk_score"]

            .mean()

            .round(2)

            .reset_index()
        )

        result.columns = [
            "gender",
            "average_risk_score"
        ]

        return result.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Risk by Insurance
    # --------------------------------------------------

    def risk_by_insurance(self):

        result = (

            self.master_df

            .groupby("insurance_type")

            ["risk_score"]

            .mean()

            .round(2)

            .reset_index()
        )

        result.columns = [
            "insurance_type",
            "average_risk_score"
        ]

        return result.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Executive Risk Dashboard
    # --------------------------------------------------

    def executive_dashboard(self):

        return {

            "risk_summary":
                self.risk_summary(),

            "risk_distribution":
                self.risk_distribution(),

            "high_risk_count":

                len(
                    self.high_risk_patients()
                ),

            "medium_risk_count":

                len(
                    self.medium_risk_patients()
                ),

            "low_risk_count":

                len(
                    self.low_risk_patients()
                )
        }