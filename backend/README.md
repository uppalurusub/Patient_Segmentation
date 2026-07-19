# 🏥 Patient Segmentation for Population Health Management

> An end-to-end Machine Learning application for Healthcare Analytics and Patient Segmentation using FastAPI, and multiple clustering algorithms.

---

# Table of Contents

* Overview
* Business Problem
* Solution Overview
* Features
* System Architecture
* Technology Stack
* Project Structure
* Installation
* Configuration
* Running the Application
* REST APIs
* Machine Learning Pipeline
* Clustering Algorithms


---

# Overview

Healthcare organizations generate enormous amounts of patient data every day. Identifying groups of patients with similar characteristics enables hospitals to improve patient care, optimize resource utilization, reduce costs, and implement personalized healthcare strategies.

This project provides a complete AI-powered Patient Segmentation platform that combines:

* Data preprocessing
* Feature engineering
* Multiple clustering algorithms
* Cluster evaluation
* Population health analytics
* Clinical risk analytics
* Financial analytics
* Interactive dashboards
* REST APIs
* React frontend

---

# Business Problem

Hospitals often struggle to answer questions such as:

* Which patients are at high clinical risk?
* Which patients are likely to incur high healthcare costs?
* Which patients require preventive care?
* Which patients belong to similar disease cohorts?
* How can healthcare resources be optimized?

Manual identification is time-consuming and inconsistent.

Machine Learning-based patient segmentation enables healthcare providers to make data-driven decisions.

---

# Solution Overview

The application performs the following steps:

1. Load patient dataset
2. Clean missing values
3. Encode categorical variables
4. Scale numerical features
5. Perform feature engineering
6. Train multiple clustering algorithms
7. Compare clustering quality
8. Select the best-performing model
9. Generate patient segments
10. Store experiments in MLflow
11. Expose predictions through FastAPI
12. Visualize results using React Dashboard

---

# Key Features

## Backend

* FastAPI REST APIs
* Modular Service Architecture
* Dependency Injection
* Loguru Logging
* Pydantic Validation
* Exception Handling
* Configuration Management


## Machine Learning

Supports multiple clustering algorithms including:

* K-Means
* Hierarchical Clustering
* Gaussian Mixture Models
* DBSCAN
* OPTICS
* Spectral Clustering
* Birch
* Affinity Propagation
* Mean Shift
* MiniBatch KMeans
* Agglomerative Clustering

---

## Analytics Modules

### Population Health Analytics

* Total Patients
* Age Distribution
* BMI Distribution
* Gender Mix
* Smoking Rate
* Alcohol Consumption
* Exercise Compliance
* Charlson Comorbidity Score

### Disease Prevalence

* Diabetes
* Hypertension
* Coronary Artery Disease
* COPD
* CKD
* Heart Failure
* Depression
* Multi-morbidity

### Clinical Risk Analytics

* High Blood Pressure
* Obesity
* Tachycardia
* Medication Adherence
* Abnormal Lab Results

### Financial Analytics

* Average Cost per Admission
* High Cost Patients
* Cost by Diagnosis
* Cost by DRG
* Readmission Cost

### Outcomes Analytics

* Mortality Rate
* ICU Admission
* Length of Stay
* Readmission Rate
* Discharge Status

---

# Technology Stack

## Backend

* Python 3.11+
* FastAPI
* Uvicorn
* Pandas
* NumPy
* Scikit-learn




## Visualization

* Plotly
* Matplotlib


# Installation

## Clone Repository

```bash
git clone <repository-url>

cd Patient_Segmentation
```

---

## Backend Installation

```bash
cd Backend

python -m venv .venv

source .venv/bin/activate

# Windows

.venv\Scripts\activate

pip install -r requirements.txt
```


# Configuration

Create a `.env` file:

```env
DATA_PATH=data/patients.csv


```

---

# Running Backend

```bash
cd Backend/src

python -m app.main
```

or

```bash
uvicorn app.main:app --reload
```



# REST APIs

Typical endpoints include:

```
GET     /health

GET     /analytics/population

GET     /analytics/clinical

GET     /analytics/financial

GET     /analytics/outcomes

GET     /segmentation/train

POST    /segmentation/predict

GET     /mlflow/experiments
```


# Evaluation Metrics

Cluster quality is evaluated using:

* Silhouette Score
* Davies-Bouldin Index
* Calinski-Harabasz Score
* Inertia
* Cluster Balance





# Author

Developed as a comprehensive Machine Learning Healthcare Analytics platform demonstrating production-ready architecture, clustering, experiment tracking, analytics dashboards, and modern MLOps best practices.
