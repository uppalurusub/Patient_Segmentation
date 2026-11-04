"""
utils/preprocessing.py

Healthcare Data Preprocessing Module
"""

import pandas as pd
import numpy as np

from sklearn.preprocessing import (
    LabelEncoder,
    StandardScaler,
    MinMaxScaler
)


class DataPreprocessor:

    def __init__(self):
        pass

    # --------------------------------------------------
    # Missing Value Handling
    # --------------------------------------------------

    @staticmethod
    def handle_missing_values(df):

        for col in df.columns:

            if df[col].dtype in ["int64", "float64"]:

                df[col] = df[col].fillna(
                    df[col].median()
                )

            else:

                df[col] = df[col].fillna(
                    "Unknown"
                )

        return df

    # --------------------------------------------------
    # Duplicate Removal
    # --------------------------------------------------

    @staticmethod
    def remove_duplicates(df):

        return df.drop_duplicates()

    # --------------------------------------------------
    # Date Conversion
    # --------------------------------------------------

    @staticmethod
    def convert_dates(df, date_columns):

        for col in date_columns:

            df[col] = pd.to_datetime(
                df[col],
                errors="coerce"
            )

        return df

    # --------------------------------------------------
    # Age Group Creation
    # --------------------------------------------------

    @staticmethod
    def create_age_groups(df):

        df["age_group"] = pd.cut(
            df["age"],
            bins=[0, 18, 35, 50, 65, 120],
            labels=[
                "0-18",
                "19-35",
                "36-50",
                "51-65",
                "65+"
            ]
        )

        return df

    # --------------------------------------------------
    # Outlier Detection
    # --------------------------------------------------

    @staticmethod
    def detect_outliers_iqr(df, column):

        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)

        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        return df[
            (df[column] < lower)
            |
            (df[column] > upper)
        ]

    # --------------------------------------------------
    # Outlier Capping
    # --------------------------------------------------

    @staticmethod
    def cap_outliers(df, column):

        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)

        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        df[column] = np.where(
            df[column] < lower,
            lower,
            df[column]
        )

        df[column] = np.where(
            df[column] > upper,
            upper,
            df[column]
        )

        return df

    # --------------------------------------------------
    # Label Encoding
    # --------------------------------------------------

    @staticmethod
    def encode_categorical(df, columns):

        encoder_dict = {}

        for col in columns:

            encoder = LabelEncoder()

            df[col] = encoder.fit_transform(
                df[col].astype(str)
            )

            encoder_dict[col] = encoder

        return df, encoder_dict

    # --------------------------------------------------
    # Standard Scaling
    # --------------------------------------------------

    @staticmethod
    def standard_scale(df, columns):

        scaler = StandardScaler()

        df[columns] = scaler.fit_transform(
            df[columns]
        )

        return df, scaler

    # --------------------------------------------------
    # MinMax Scaling
    # --------------------------------------------------

    @staticmethod
    def minmax_scale(df, columns):

        scaler = MinMaxScaler()

        df[columns] = scaler.fit_transform(
            df[columns]
        )

        return df, scaler

    # --------------------------------------------------
    # Data Quality Summary
    # --------------------------------------------------

    @staticmethod
    def data_quality_report(df):

        report = pd.DataFrame({

            "column": df.columns,

            "dtype": df.dtypes.values,

            "missing_count": df.isnull().sum().values,

            "missing_pct":
                (
                    df.isnull().sum()
                    /
                    len(df)
                ) * 100,

            "unique_values":
                df.nunique().values
        })

        return report

    # --------------------------------------------------
    # Build Master Patient Dataset
    # --------------------------------------------------

    @staticmethod
    def create_master_dataset(
            patients,
            encounters,
            diagnoses,
            claims,
            labs):

        visit_count = (
            encounters
            .groupby("patient_id")
            .size()
            .reset_index(name="visit_count")
        )

        chronic_count = (
            diagnoses
            .groupby("patient_id")
            .size()
            .reset_index(name="diagnosis_count")
        )

        total_cost = (
            claims
            .groupby("patient_id")["paid_amount"]
            .sum()
            .reset_index(name="total_cost")
        )

        abnormal_labs = (
            labs
            .groupby("patient_id")["abnormal_flag"]
            .sum()
            .reset_index(name="abnormal_lab_count")
        )

        master = patients.merge(
            visit_count,
            on="patient_id",
            how="left"
        )

        master = master.merge(
            chronic_count,
            on="patient_id",
            how="left"
        )

        master = master.merge(
            total_cost,
            on="patient_id",
            how="left"
        )

        master = master.merge(
            abnormal_labs,
            on="patient_id",
            how="left"
        )

        master.fillna(0, inplace=True)

        return master

    # --------------------------------------------------
    # Full Pipeline
    # --------------------------------------------------

    def run_preprocessing(
            self,
            patients,
            encounters,
            diagnoses,
            claims,
            labs):

        patients = self.handle_missing_values(
            patients
        )

        patients = self.remove_duplicates(
            patients
        )

        patients = self.create_age_groups(
            patients
        )

        master_df = self.create_master_dataset(
            patients,
            encounters,
            diagnoses,
            claims,
            labs
        )

        return master_df