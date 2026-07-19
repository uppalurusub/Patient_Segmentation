"""
utils/loader.py

Centralized Data Loader for Healthcare Analytics
"""

import pandas as pd

from pathlib import Path





from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"

print(PROJECT_ROOT)
print(DATA_DIR)


class DataLoader:

    def __init__(self):
        self.data_path = DATA_DIR

        

        if not self.data_path.exists():
            raise FileNotFoundError(
                f"Data directory not found: {self.data_path}"
            )

    # --------------------------------------------------
    # Generic Loader
    # --------------------------------------------------
    def load_csv(self, file_name):

        file_path = self.data_path / file_name

        

        if not file_path.exists():
            raise FileNotFoundError(file_path)

        return pd.read_csv(file_path)

    
    # --------------------------------------------------
    # Patients
    # --------------------------------------------------

    def load_patients(self):

        df = self.load_csv("patients.csv")

        

        expected_columns = [
            "patient_id",
            "age",
            "gender",
            "race",
            "zipcode",
            "insurance_type"
        ]

        self.validate_columns(df, expected_columns)

        return df

    # --------------------------------------------------
    # Encounters
    # --------------------------------------------------

    def load_encounters(self):

        df = self.load_csv("encounters.csv")

        expected_columns = [
            "encounter_id",
            "patient_id",
            "visit_date",
            "visit_type",
            "provider_id",
            "provider_specialty",
            "length_of_stay_days",
            "discharge_status",
            "readmission_flag",
            "total_charges"
        ]

        self.validate_columns(df, expected_columns)

        df["visit_date"] = pd.to_datetime(df["visit_date"])

        return df

    # --------------------------------------------------
    # Diagnoses
    # --------------------------------------------------

    def load_diagnoses(self):

        df = self.load_csv("diagnoses.csv")

        expected_columns = [
            "diagnosis_id",
            "patient_id",
            "visit_date",
            "visit_type",
            "primary_diagnosis",
            "primary_icd10",
            "secondary_diagnoses",
            "secondary_icd10s",
            "provider_specialty"
        ]

        self.validate_columns(df, expected_columns)

        df["visit_date"] = pd.to_datetime(df["visit_date"])

        return df

    # --------------------------------------------------
    # Claims
    # --------------------------------------------------

    def load_claims(self):

        df = self.load_csv("claims.csv")

        expected_columns = [
            "claim_id",
            "patient_id",
            "encounter_id",
            "claim_date",
            "claim_type",
            "payer",
            "billed_amount",
            "allowed_amount",
            "paid_amount",
            "patient_responsibility",
            "claim_status"
        ]

        self.validate_columns(df, expected_columns)

        df["claim_date"] = pd.to_datetime(df["claim_date"])

        return df

    # --------------------------------------------------
    # Labs
    # --------------------------------------------------

    def load_labs(self):

        df = self.load_csv("labs.csv")

        expected_columns = [
            "lab_result_id",
            "patient_id",
            "test_date",
            "test_name",
            "value",
            "unit",
            "reference_low",
            "reference_high",
            "abnormal_flag"
        ]

        self.validate_columns(df, expected_columns)

        df["test_date"] = pd.to_datetime(df["test_date"])

        return df

    # --------------------------------------------------
    # Validation
    # --------------------------------------------------

    @staticmethod
    def validate_columns(df, expected_columns):

        missing_cols = [
            col
            for col in expected_columns
            if col not in df.columns
        ]

        if missing_cols:
            raise ValueError(
                f"Missing columns: {missing_cols}"
            )

    # --------------------------------------------------
    # Load All
    # --------------------------------------------------

    def load_all(self):

        return {
            "patients": self.load_patients(),
            "encounters": self.load_encounters(),
            "diagnoses": self.load_diagnoses(),
            "claims": self.load_claims(),
            "labs": self.load_labs()
        }