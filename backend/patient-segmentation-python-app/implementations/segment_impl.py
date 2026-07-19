"""
implementations/segment_impl.py
"""

import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

from utils.loader import DataLoader
from utils.preprocessing import DataPreprocessor


class SegmentImplementation:

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

        self.segmentation_executed = False

    # --------------------------------------------------
    # Run Segmentation
    # --------------------------------------------------

    def run_segmentation(self):

        features = self.master_df[
            [
                "age",
                "visit_count",
                "diagnosis_count",
                "total_cost",
                "abnormal_lab_count"
            ]
        ].copy()

        scaler = StandardScaler()

        X = scaler.fit_transform(features)

        model = KMeans(
            n_clusters=5,
            random_state=42,
            n_init=10
        )

        self.master_df["segment"] = (
            model.fit_predict(X)
        )

        self.segmentation_executed = True

        return {
            "message":
                "Segmentation completed successfully",
            "segments":
                int(
                    self.master_df["segment"]
                    .nunique()
                )
        }

    # --------------------------------------------------
    # Validate Segmentation
    # --------------------------------------------------

    def _check_segmentation(self):

        if "segment" not in self.master_df.columns:

            self.run_segmentation()

    # --------------------------------------------------
    # Segment Distribution
    # --------------------------------------------------

    def segment_distribution(self):

        self._check_segmentation()

        result = (
            self.master_df["segment"]
            .value_counts()
            .sort_index()
            .reset_index()
        )

        result.columns = [
            "segment",
            "count"
        ]

        return result.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Segment Summary
    # --------------------------------------------------

    def segment_summary(self):

        self._check_segmentation()

        summary = (

            self.master_df

            .groupby("segment")

            .agg({

                "patient_id": "count",

                "age": "mean",

                "visit_count": "mean",

                "diagnosis_count": "mean",

                "total_cost": "mean",

                "abnormal_lab_count": "mean"

            })

            .round(2)

            .reset_index()
        )

        summary.rename(
            columns={
                "patient_id":
                    "patient_count"
            },
            inplace=True
        )

        return summary.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Segment Profiles
    # --------------------------------------------------

    def segment_profiles(self):

        self._check_segmentation()

        profiles = []

        for segment in sorted(
                self.master_df["segment"].unique()):

            df = self.master_df[
                self.master_df["segment"]
                == segment
            ]

            profiles.append({

                "segment":
                    int(segment),

                "patient_count":
                    int(len(df)),

                "average_age":
                    round(
                        df["age"].mean(),
                        2
                    ),

                "average_cost":
                    round(
                        df["total_cost"].mean(),
                        2
                    ),

                "average_visits":
                    round(
                        df["visit_count"].mean(),
                        2
                    ),

                "average_diagnoses":
                    round(
                        df["diagnosis_count"]
                        .mean(),
                        2
                    )
            })

        return profiles

    # --------------------------------------------------
    # Single Segment Profile
    # --------------------------------------------------

    def segment_profile(
            self,
            segment_id: int
    ):

        self._check_segmentation()

        df = self.master_df[
            self.master_df["segment"]
            == segment_id
        ]

        if df.empty:

            return {
                "message":
                    "Segment not found"
            }

        return {

            "segment":
                int(segment_id),

            "patient_count":
                int(len(df)),

            "average_age":
                round(
                    df["age"].mean(),
                    2
                ),

            "average_cost":
                round(
                    df["total_cost"]
                    .mean(),
                    2
                ),

            "average_visits":
                round(
                    df["visit_count"]
                    .mean(),
                    2
                )
        }

    # --------------------------------------------------
    # Cost Analysis
    # --------------------------------------------------

    def segment_cost_analysis(self):

        self._check_segmentation()

        result = (

            self.master_df

            .groupby("segment")

            ["total_cost"]

            .mean()

            .round(2)

            .reset_index()
        )

        result.columns = [
            "segment",
            "average_cost"
        ]

        return result.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Risk Analysis
    # --------------------------------------------------

    def segment_risk_analysis(self):

        self._check_segmentation()

        result = (

            self.master_df

            .groupby("segment")

            ["diagnosis_count"]

            .mean()

            .round(2)

            .reset_index()
        )

        result.columns = [
            "segment",
            "average_risk_score"
        ]

        return result.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Utilization Analysis
    # --------------------------------------------------

    def segment_utilization_analysis(self):

        self._check_segmentation()

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
    # High Value Segment
    # --------------------------------------------------

    def high_value_segment(self):

        self._check_segmentation()

        summary = (
            self.master_df
            .groupby("segment")
            ["total_cost"]
            .mean()
            .reset_index()
        )

        top_segment = summary.loc[
            summary["total_cost"].idxmax()
        ]

        return {

            "segment":
                int(
                    top_segment["segment"]
                ),

            "average_cost":
                round(
                    top_segment["total_cost"],
                    2
                )
        }

    # --------------------------------------------------
    # High Risk Segment
    # --------------------------------------------------

    def high_risk_segment(self):

        self._check_segmentation()

        summary = (
            self.master_df
            .groupby("segment")
            ["diagnosis_count"]
            .mean()
            .reset_index()
        )

        top_segment = summary.loc[
            summary["diagnosis_count"]
            .idxmax()
        ]

        return {

            "segment":
                int(
                    top_segment["segment"]
                ),

            "average_risk":
                round(
                    top_segment[
                        "diagnosis_count"
                    ],
                    2
                )
        }

    # --------------------------------------------------
    # Executive Summary
    # --------------------------------------------------

    def executive_summary(self):

        self._check_segmentation()

        return {

            "total_segments":
                int(
                    self.master_df["segment"]
                    .nunique()
                ),

            "largest_segment":

                int(

                    self.master_df["segment"]

                    .value_counts()

                    .idxmax()
                ),

            "high_value_segment":

                self.high_value_segment(),

            "high_risk_segment":

                self.high_risk_segment()
        }