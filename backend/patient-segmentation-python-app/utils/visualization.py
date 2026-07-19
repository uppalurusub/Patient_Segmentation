"""
utils/visualization.py

Healthcare Analytics Visualization Module
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_style("whitegrid")


class VisualizationService:

    # ---------------------------------------------------
    # Age Distribution
    # ---------------------------------------------------

    @staticmethod
    def age_distribution(df):

        plt.figure(figsize=(10, 6))

        sns.histplot(
            data=df,
            x="age",
            bins=20,
            kde=True
        )

        plt.title("Patient Age Distribution")
        plt.xlabel("Age")
        plt.ylabel("Patients")

        plt.tight_layout()

        return plt

    # ---------------------------------------------------
    # Gender Distribution
    # ---------------------------------------------------

    @staticmethod
    def gender_distribution(df):

        plt.figure(figsize=(8, 5))

        sns.countplot(
            data=df,
            x="gender"
        )

        plt.title("Gender Distribution")

        plt.tight_layout()

        return plt

    # ---------------------------------------------------
    # Insurance Distribution
    # ---------------------------------------------------

    @staticmethod
    def insurance_distribution(df):

        plt.figure(figsize=(10, 5))

        sns.countplot(
            data=df,
            x="insurance_type"
        )

        plt.title("Insurance Mix")

        plt.xticks(rotation=30)

        plt.tight_layout()

        return plt

    # ---------------------------------------------------
    # Top Diagnoses
    # ---------------------------------------------------

    @staticmethod
    def top_diagnoses(diagnoses_df):

        top_dx = (
            diagnoses_df["primary_diagnosis"]
            .value_counts()
            .head(10)
        )

        plt.figure(figsize=(12, 6))

        sns.barplot(
            x=top_dx.values,
            y=top_dx.index
        )

        plt.title("Top 10 Diagnoses")

        plt.tight_layout()

        return plt

    # ---------------------------------------------------
    # Cost Distribution
    # ---------------------------------------------------

    @staticmethod
    def cost_distribution(master_df):

        plt.figure(figsize=(10, 6))

        sns.histplot(
            master_df["total_cost"],
            bins=30,
            kde=True
        )

        plt.title("Patient Cost Distribution")

        plt.tight_layout()

        return plt

    # ---------------------------------------------------
    # High Cost Patients
    # ---------------------------------------------------

    @staticmethod
    def top_cost_patients(master_df):

        top_cost = (
            master_df
            .sort_values(
                "total_cost",
                ascending=False
            )
            .head(20)
        )

        plt.figure(figsize=(12, 8))

        sns.barplot(
            x="total_cost",
            y="patient_id",
            data=top_cost
        )

        plt.title(
            "Top 20 High Cost Patients"
        )

        plt.tight_layout()

        return plt

    # ---------------------------------------------------
    # Visit Count Distribution
    # ---------------------------------------------------

    @staticmethod
    def utilization_distribution(master_df):

        plt.figure(figsize=(10, 6))

        sns.histplot(
            master_df["visit_count"],
            bins=20,
            kde=True
        )

        plt.title(
            "Patient Utilization Distribution"
        )

        plt.tight_layout()

        return plt

    # ---------------------------------------------------
    # Readmission Rate
    # ---------------------------------------------------

    @staticmethod
    def readmission_chart(encounters_df):

        summary = (
            encounters_df["readmission_flag"]
            .value_counts()
        )

        plt.figure(figsize=(6, 6))

        plt.pie(
            summary.values,
            labels=["No", "Yes"],
            autopct="%1.1f%%"
        )

        plt.title("Readmission Rate")

        return plt

    # ---------------------------------------------------
    # Abnormal Lab Distribution
    # ---------------------------------------------------

    @staticmethod
    def abnormal_labs_chart(labs_df):

        summary = (
            labs_df["abnormal_flag"]
            .value_counts()
        )

        plt.figure(figsize=(6, 6))

        plt.pie(
            summary.values,
            labels=["Normal", "Abnormal"],
            autopct="%1.1f%%"
        )

        plt.title(
            "Abnormal Laboratory Results"
        )

        return plt

    # ---------------------------------------------------
    # Correlation Matrix
    # ---------------------------------------------------

    @staticmethod
    def correlation_matrix(master_df):

        numerical_cols = [
            col
            for col in master_df.columns
            if master_df[col].dtype != "object"
        ]

        corr = (
            master_df[numerical_cols]
            .corr()
        )

        plt.figure(figsize=(12, 8))

        sns.heatmap(
            corr,
            annot=True,
            cmap="coolwarm"
        )

        plt.title(
            "Correlation Matrix"
        )

        plt.tight_layout()

        return plt

    # ---------------------------------------------------
    # Segment Distribution
    # ---------------------------------------------------

    @staticmethod
    def segment_distribution(master_df):

        plt.figure(figsize=(10, 6))

        sns.countplot(
            data=master_df,
            x="segment"
        )

        plt.title(
            "Patient Segment Distribution"
        )

        plt.xticks(rotation=25)

        plt.tight_layout()

        return plt

    # ---------------------------------------------------
    # Segment Cost Comparison
    # ---------------------------------------------------

    @staticmethod
    def segment_cost_comparison(master_df):

        plt.figure(figsize=(12, 6))

        sns.boxplot(
            x="segment",
            y="total_cost",
            data=master_df
        )

        plt.title(
            "Cost by Segment"
        )

        plt.xticks(rotation=20)

        plt.tight_layout()

        return plt

    # ---------------------------------------------------
    # Segment Utilization Comparison
    # ---------------------------------------------------

    @staticmethod
    def segment_utilization_comparison(
            master_df):

        plt.figure(figsize=(12, 6))

        sns.boxplot(
            x="segment",
            y="visit_count",
            data=master_df
        )

        plt.title(
            "Visits by Segment"
        )

        plt.xticks(rotation=20)

        plt.tight_layout()

        return plt

    # ---------------------------------------------------
    # Risk Category Distribution
    # ---------------------------------------------------

    @staticmethod
    def risk_distribution(master_df):

        plt.figure(figsize=(10, 6))

        sns.countplot(
            data=master_df,
            x="risk_category"
        )

        plt.title(
            "Risk Category Distribution"
        )

        plt.tight_layout()

        return plt

    # ---------------------------------------------------
    # Monthly Cost Trend
    # ---------------------------------------------------

    @staticmethod
    def monthly_cost_trend(claims_df):

        claims_df["claim_month"] = (
            pd.to_datetime(
                claims_df["claim_date"]
            )
            .dt.to_period("M")
            .astype(str)
        )

        monthly = (
            claims_df
            .groupby("claim_month")
            ["paid_amount"]
            .sum()
            .reset_index()
        )

        plt.figure(figsize=(14, 6))

        sns.lineplot(
            x="claim_month",
            y="paid_amount",
            data=monthly
        )

        plt.title(
            "Monthly Healthcare Cost Trend"
        )

        plt.xticks(rotation=45)

        plt.tight_layout()

        return plt

    # ---------------------------------------------------
    # Dashboard KPI Summary
    # ---------------------------------------------------

    @staticmethod
    def executive_kpis(master_df):

        return {

            "total_patients":
                master_df["patient_id"].nunique(),

            "average_age":
                round(master_df["age"].mean(), 2),

            "average_cost":
                round(
                    master_df["total_cost"].mean(),
                    2
                ),

            "total_cost":
                round(
                    master_df["total_cost"].sum(),
                    2
                ),

            "average_visits":
                round(
                    master_df["visit_count"].mean(),
                    2
                ),

            "high_risk_patients":
                len(
                    master_df[
                        master_df[
                            "risk_category"
                        ] == "High"
                    ]
                )
        }