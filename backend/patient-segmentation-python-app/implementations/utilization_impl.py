"""
implementations/utilization_impl.py
"""

import pandas as pd

from utils.loader import DataLoader
from utils.preprocessing import DataPreprocessor


class UtilizationImplementation:

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
    # Utilization Summary
    # --------------------------------------------------

    def utilization_summary(self):

        total_visits = len(self.encounters)

        avg_visits = round(
            self.master_df["visit_count"].mean(),
            2
        )

        avg_los = round(
            self.encounters["length_of_stay_days"]
            .mean(),
            2
        )

        readmission_rate = self.readmission_rate()

        return {

            "total_visits": int(total_visits),

            "average_visits_per_patient":
                avg_visits,

            "average_los":
                avg_los,

            "readmission_rate_pct":
                readmission_rate[
                    "readmission_rate_pct"
                ]
        }

    # --------------------------------------------------
    # Visit Distribution
    # --------------------------------------------------

    def visit_distribution(self):

        result = (

            self.master_df

            .groupby("visit_count")

            .size()

            .reset_index(
                name="patients"
            )

            .sort_values(
                "visit_count"
            )
        )

        return result.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Top Utilizers
    # --------------------------------------------------

    def top_utilizers(self):

        df = (

            self.master_df

            .sort_values(
                "visit_count",
                ascending=False
            )

            .head(20)
        )

        return df.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Readmission Rate
    # --------------------------------------------------

    def readmission_rate(self):

        if "readmission_flag" not in self.encounters.columns:

            return {
                "message":
                "readmission_flag column not available"
            }

        total = len(self.encounters)

        readmissions = int(
            self.encounters[
                "readmission_flag"
            ].sum()
        )

        rate = round(
            (readmissions / total) * 100,
            2
        )

        return {

            "total_encounters":
                total,

            "readmissions":
                readmissions,

            "readmission_rate_pct":
                rate
        }

    # --------------------------------------------------
    # Readmitted Patients
    # --------------------------------------------------

    def readmitted_patients(self):

        if "readmission_flag" not in self.encounters.columns:

            return []

        patients = self.encounters[
            self.encounters[
                "readmission_flag"
            ] == 1
        ]

        return patients.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # LOS Summary
    # --------------------------------------------------

    def los_summary(self):

        if "length_of_stay_days" not in self.encounters.columns:

            return {
                "message":
                "length_of_stay_days column not found"
            }

        return {

            "average_los":
                float(round(
                    self.encounters[
                        "length_of_stay_days"
                    ].mean(),
                    2
                )
                ),

            "maximum_los":
                float(round(
                    self.encounters[
                        "length_of_stay_days"
                    ].max(),
                    2
                )
                ),

            "minimum_los":
                float(round(
                    self.encounters[
                        "length_of_stay_days"
                    ].min(),
                    2
                )
                )
        }

    # --------------------------------------------------
    # LOS Distribution
    # --------------------------------------------------

    def los_distribution(self):

        if "length_of_stay_days" not in self.encounters.columns:

            return []

        bins = [
            0,
            2,
            5,
            10,
            20,
            100
        ]

        labels = [
            "0-2",
            "3-5",
            "6-10",
            "11-20",
            "20+"
        ]

        los_group = pd.cut(
            self.encounters["length_of_stay_days"],
            bins=bins,
            labels=labels
        )

        result = (
            los_group
            .value_counts()
            .sort_index()
            .reset_index()
        )

        result.columns = [
            "los_group",
            "count"
        ]

        return result.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Utilization By Age Group
    # --------------------------------------------------

    def utilization_by_age_group(self):

        self.master_df["age_group"] = pd.cut(
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

        result = (

            self.master_df

            .groupby("age_group")

            ["visit_count"]

            .mean()

            .round(2)

            .reset_index()
        )

        result.columns = [
            "age_group",
            "average_visits"
        ]

        return result.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Utilization By Gender
    # --------------------------------------------------

    def utilization_by_gender(self):

        result = (

            self.master_df

            .groupby("gender")

            ["visit_count"]

            .mean()

            .round(2)

            .reset_index()
        )

        result.columns = [
            "gender",
            "average_visits"
        ]

        return result.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Utilization By Insurance
    # --------------------------------------------------

    def utilization_by_insurance(self):

        result = (

            self.master_df

            .groupby("insurance_type")

            ["visit_count"]

            .mean()

            .round(2)

            .reset_index()
        )

        result.columns = [
            "insurance_type",
            "average_visits"
        ]

        return result.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Utilization By Risk Category
    # --------------------------------------------------

    def utilization_by_risk_category(self):

        result = (

            self.master_df

            .groupby("risk_category")

            ["visit_count"]

            .mean()

            .round(2)

            .reset_index()
        )

        result.columns = [
            "risk_category",
            "average_visits"
        ]

        return result.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Utilization By Segment
    # --------------------------------------------------

    def utilization_by_segment(self):

        if "segment" not in self.master_df.columns:

            return {
                "message":
                "Segmentation not executed"
            }

        result = (

            self.master_df

            .groupby("segment")

            ["visit_count"]

            .mean()

            .round(2)

            .reset_index()
        )

        result.columns = [
            "segment",
            "average_visits"
        ]

        return result.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Executive Dashboard
    # --------------------------------------------------

    def utilization_dashboard(self):

        result = {

            "utilization_summary":
                self.utilization_summary(),

            "readmission_rate":
                self.readmission_rate(),

            "los_summary":
                self.los_summary(),

            "top_utilizers":
                len(
                    self.top_utilizers()
                )
        }

        print(result)

        return result