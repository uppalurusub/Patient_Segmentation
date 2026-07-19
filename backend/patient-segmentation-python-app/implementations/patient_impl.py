"""
implementations/patient_impl.py
"""

import pandas as pd

from utils.loader import DataLoader
from utils.preprocessing import DataPreprocessor


class PatientImplementation:

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
    # Patient Summary
    # --------------------------------------------------

    def get_patient_summary(self):

        return {

            "total_patients":
                int(
                    self.master_df["patient_id"]
                    .nunique()
                ),

            "average_age":
                round(
                    self.master_df["age"]
                    .mean(),
                    2
                ),

            "male_patients":
                int(
                    len(
                        self.master_df[
                            self.master_df["gender"]
                            == "Male"
                        ]
                    )
                ),

            "female_patients":
                int(
                    len(
                        self.master_df[
                            self.master_df["gender"]
                            == "Female"
                        ]
                    )
                )
        }

    # --------------------------------------------------
    # All Patients
    # --------------------------------------------------

    def get_all_patients(self):

        return self.master_df.head(
            100
        ).to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Patient By ID
    # --------------------------------------------------

    def get_patient_by_id(
            self,
            patient_id: str
    ):

        patient = self.master_df[
            self.master_df["patient_id"]
            == patient_id
        ]

        if patient.empty:
            return {}

        return patient.iloc[0].to_dict()

    # --------------------------------------------------
    # Search Patient
    # --------------------------------------------------

    def search_patient(
            self,
            keyword: str
    ):

        keyword = str(keyword)

        result = self.master_df[

            self.master_df["patient_id"]
            .astype(str)
            .str.contains(keyword, case=False, na=False)

            |

            self.master_df["gender"]
            .astype(str)
            .str.contains(keyword, case=False, na=False)

            |

            self.master_df["race"]
            .astype(str)
            .str.contains(keyword, case=False, na=False)

            |

            self.master_df["insurance_type"]
            .astype(str)
            .str.contains(keyword, case=False, na=False)
        ]

        return result.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Age Distribution
    # --------------------------------------------------

    def age_distribution(self):

        bins = [0, 18, 35, 50, 65, 120]

        labels = [
            "0-18",
            "19-35",
            "36-50",
            "51-65",
            "65+"
        ]

        age_groups = pd.cut(
            self.master_df["age"],
            bins=bins,
            labels=labels,
            include_lowest=True
        )

        age_distribution = (
            age_groups
            .value_counts()
            .sort_index()
            .reset_index()
        )

        age_distribution.columns = [
            "age_group",
            "count"
        ]

        age_distribution["age_group"] = (
            age_distribution["age_group"]
            .astype(str)
        )

        return age_distribution.to_dict(
            orient="records"
        )

    
    # --------------------------------------------------
    # Gender Distribution
    # --------------------------------------------------

    def gender_distribution(self):

        gender_dist = (
            self.master_df["gender"]
            .value_counts()
            .reset_index()
        )

        gender_dist.columns = [
            "gender",
            "count"
        ]

        return gender_dist.to_dict(
            orient="records"
        )

        

    # --------------------------------------------------
    # Insurance Distribution
    # --------------------------------------------------

    def insurance_distribution(self):

        insurance_dist = (
            self.master_df["insurance_type"]
            .value_counts()
            .reset_index()
        )

        insurance_dist.columns = [
            "insurance_type",
            "count"
        ]

        return insurance_dist.to_dict(
            orient="records"
        )

        
    # --------------------------------------------------
    # Race Distribution
    # --------------------------------------------------

    def race_distribution(self):

        race_dist = (
            self.master_df["race"]
            .value_counts()
            .reset_index()
        )

        race_dist.columns = [
            "race",
            "count"
        ]

        return race_dist.to_dict(
            orient="records"
        )

        

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
    # Population KPIs
    # --------------------------------------------------

    def population_kpis(self):

        try:

            

            return {

                "total_patients":
                    int(
                        self.master_df["patient_id"]
                        .nunique()
                    ),

                "avg_age":
                    round(
                        self.master_df["age"]
                        .mean(),
                        2
                    ),

                "avg_visits":
                    round(
                        self.master_df["visit_count"]
                        .mean(),
                        2
                    ),

                "avg_cost":
                    round(
                        self.master_df["total_cost"]
                        .mean(),
                        2
                    ),

                "total_cost":
                    round(
                        self.master_df["total_cost"]
                        .sum(),
                        2
                    ),

                "high_risk_patients":
                    int(
                        (
                            self.master_df[
                                "risk_category"
                            ] == "High"
                        ).sum()
                    )
            }

        except Exception as e:

            print("ERROR:", str(e))

            return {
                "error": str(e)
            }

    # --------------------------------------------------
    # Segment Distribution
    # --------------------------------------------------

    def segment_distribution(self):

        if "segment" not in self.master_df.columns:

            return {
                "message":
                "Segmentation not executed"
            }

        return (
            self.master_df["segment"]
            .value_counts()
            .reset_index()
            .rename(
                columns={
                    "index": "segment",
                    "segment": "count"
                }
            )
            .to_dict(
                orient="records"
            )
        )

    # --------------------------------------------------
    # Segment Summary
    # --------------------------------------------------

    def segment_summary(self):

        if "segment" not in self.master_df.columns:

            return []

        summary = (

            self.master_df

            .groupby("segment")

            .agg({

                "patient_id": "count",

                "age": "mean",

                "visit_count": "mean",

                "diagnosis_count": "mean",

                "total_cost": "mean"

            })

            .reset_index()
        )

        return summary.to_dict(
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
    # Abnormal Lab Patients
    # --------------------------------------------------

    def abnormal_lab_patients(self):

        df = self.master_df[
            self.master_df[
                "abnormal_lab_count"
            ] > 0
        ]

        return df.to_dict(
            orient="records"
        )

    # --------------------------------------------------
    # Executive Dashboard
    # --------------------------------------------------

    def executive_dashboard(self):

        return {

            "patient_summary":
                self.get_patient_summary(),

            "population_kpis":
                self.population_kpis(),

            "top_utilizers":
                self.top_utilizers()[:10],

            "high_cost_patients":
                len(
                    self.high_cost_patients()
                ),

            "high_risk_patients":
                len(
                    self.high_risk_patients()
                )
        }