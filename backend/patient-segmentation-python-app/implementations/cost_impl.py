"""
implementations/cost_impl.py
"""

import pandas as pd

from utils.loader import DataLoader
from utils.preprocessing import DataPreprocessor


class CostImplementation:

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

        self._create_risk_category()

    # --------------------------------------------------
    # Risk Category
    # --------------------------------------------------

    def _create_risk_category(self):

        self.master_df["risk_score"] = (

            self.master_df["visit_count"] * 2 +

            self.master_df["diagnosis_count"] * 3 +

            self.master_df["abnormal_lab_count"] * 2
        )

        self.master_df["risk_category"] = pd.cut(

            self.master_df["risk_score"],

            bins=[-1, 10, 25, 9999],

            labels=[
                "Low",
                "Medium",
                "High"
            ]
        )

    # --------------------------------------------------
    # Cost Summary
    # --------------------------------------------------

    def cost_summary(self):

        return {

            "total_cost":
                round(
                    self.master_df["total_cost"]
                    .sum(),
                    2
                ),

            "average_cost":
                round(
                    self.master_df["total_cost"]
                    .mean(),
                    2
                ),

            "maximum_cost":
                round(
                    self.master_df["total_cost"]
                    .max(),
                    2
                ),

            "minimum_cost":
                round(
                    self.master_df["total_cost"]
                    .min(),
                    2
                )
        }

    # --------------------------------------------------
    # Cost Distribution
    # --------------------------------------------------

    def cost_distribution(self):

        bins = [
            0,
            5000,
            10000,
            25000,
            50000,
            1000000
        ]

        labels = [
            "0-5K",
            "5K-10K",
            "10K-25K",
            "25K-50K",
            "50K+"
        ]

        cost_group = pd.cut(
            self.master_df["total_cost"],
            bins=bins,
            labels=labels,
            include_lowest=True
        )

        result = (
            cost_group
            .value_counts()
            .sort_index()
            .reset_index()
        )

        result.columns = [
            "cost_range",
            "count"
        ]

        return result.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # High Cost Patients
    # --------------------------------------------------

    def high_cost_patients(self):

        threshold = (
            self.master_df["total_cost"]
            .quantile(0.95)
        )

        df = self.master_df[
            self.master_df["total_cost"]
            >= threshold
        ]

        return df.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Top Cost Patients
    # --------------------------------------------------

    def top_cost_patients(self):

        df = (
            self.master_df
            .sort_values(
                "total_cost",
                ascending=False
            )
            .head(20)
        )

        return df.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Cost By Age Group
    # --------------------------------------------------

    def cost_by_age_group(self):

        age_groups = pd.cut(

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

        self.master_df["age_group"] = age_groups

        result = (
            self.master_df
            .groupby("age_group")
            ["total_cost"]
            .mean()
            .round(2)
            .reset_index()
        )

        result.columns = [
            "age_group",
            "average_cost"
        ]

        return result.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Cost By Gender
    # --------------------------------------------------

    def cost_by_gender(self):

        result = (
            self.master_df
            .groupby("gender")
            ["total_cost"]
            .mean()
            .round(2)
            .reset_index()
        )

        result.columns = [
            "gender",
            "average_cost"
        ]

        return result.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Cost By Insurance
    # --------------------------------------------------

    def cost_by_insurance(self):

        result = (
            self.master_df
            .groupby("insurance_type")
            ["total_cost"]
            .mean()
            .round(2)
            .reset_index()
        )

        result.columns = [
            "insurance_type",
            "average_cost"
        ]

        return result.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Cost By Risk Category
    # --------------------------------------------------

    def cost_by_risk_category(self):

        result = (
            self.master_df
            .groupby("risk_category")
            ["total_cost"]
            .mean()
            .round(2)
            .reset_index()
        )

        result.columns = [
            "risk_category",
            "average_cost"
        ]

        return result.to_dict(
            orient="records"
        )

    

    # --------------------------------------------------
    # Monthly Cost Trend
    # --------------------------------------------------

    def monthly_cost_trend(self):

        self.claims["claim_date"] = pd.to_datetime(
            self.claims["claim_date"]
        )

        self.claims["month"] = (
            self.claims["claim_date"]
            .dt.to_period("M")
            .astype(str)
        )

        trend = (
            self.claims
            .groupby("month")
            ["paid_amount"]
            .sum()
            .round(2)
            .reset_index()
        )

        trend.columns = [
            "month",
            "total_cost"
        ]

        return trend.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Payer Analysis
    # --------------------------------------------------

    def payer_analysis(self):

        result = (
            self.claims
            .groupby("payer")
            ["paid_amount"]
            .agg(
                ["sum", "mean", "count"]
            )
            .round(2)
            .reset_index()
        )

        result.columns = [
            "payer",
            "total_paid",
            "average_paid",
            "claim_count"
        ]

        return result.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Executive Dashboard
    # --------------------------------------------------

    def executive_dashboard(self):

        return {

            "cost_summary":
                self.cost_summary(),

            "high_cost_patients":
                len(
                    self.high_cost_patients()
                ),

            "top_patient_cost":
                round(
                    self.master_df[
                        "total_cost"
                    ].max(),
                    2
                ),

            "payer_analysis":
                self.payer_analysis()
        }