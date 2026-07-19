# 🏥 Patient Segmentation Analytics Platform

A full-stack Healthcare Analytics application built using **FastAPI** and **React + TypeScript** that enables healthcare organizations to analyze patient populations, identify meaningful patient segments, evaluate clinical and financial performance, monitor utilization, and support data-driven decision making.

The platform provides interactive dashboards and REST APIs for patient analytics, risk stratification, clinical insights, utilization monitoring, and cost analytics.

---

# Project Overview

Patient Segmentation Analytics helps healthcare organizations:

- Understand patient demographics
- Identify patient cohorts
- Analyze healthcare utilization
- Evaluate clinical outcomes
- Measure healthcare costs
- Perform risk stratification
- Monitor enterprise healthcare KPIs
- Build data-driven population health strategies

---

# Architecture

```
                    React + TypeScript
                             │
                             │ REST API
                             ▼
                     FastAPI Backend
                             │
               Business Service Layer
                             │
                 Analytics Implementation
                             │
               CSV Healthcare Datasets
```

---

# Technology Stack

## Backend

- Python 3.11+
- FastAPI
- Pandas
- NumPy
- Uvicorn

---

## Frontend

- React 19
- TypeScript
- Vite
- React Router
- Axios
- CSS

---

# Project Structure

```
Patient_Segmentation/

│
├── backend/
│   │
│   ├── data/
│   │      patients.csv
│   │      diagnoses.csv
│   │      encounters.csv
│   │      claims.csv
│   │      labs.csv
│   │
│   └── patient-segmentation-python-app/
│
│          main.py
│
│          routers/
│          services/
│          implementations/
│          utils/
│
│
├── ui/
│   └── reactjs/
│
│        patient-segmentation-react-app/
│
│            src/
│              api/
│              components/
│              hooks/
│              pages/
│              routes/
│              types/
│              utils/
│
├── requirements.txt
│
└── README.md
```

---

# Backend Modules

The FastAPI application exposes analytics APIs for:

- Patient Analytics
- Patient Segmentation
- Risk Stratification
- Clinical Analytics
- Cost Analytics
- Utilization Analytics
- Executive Dashboard

---

# Frontend Modules

The React application provides pages for:

- Dashboard
- Patient Analytics
- Clinical Analytics
- Risk Analytics
- Cost Analytics
- Utilization Analytics
- Patient Segmentation

---

# Backend Folder Structure

```
backend/

data/

implementations/

routers/

services/

utils/

main.py
```

---

# Frontend Folder Structure

```
src/

api/

components/

hooks/

pages/

routes/

types/

utils/
```

---

# Healthcare Datasets

The application analyzes healthcare datasets including:

- Patients
- Diagnoses
- Encounters
- Claims
- Laboratory Results

These datasets are loaded by the backend analytics engine.

---

# Analytics Modules

## 1. Patient Analytics

Provides:

- Total Patients
- Gender Distribution
- Age Distribution
- Patient Demographics
- Population Summary

---

## 2. Patient Segmentation

Identifies patient cohorts based on healthcare characteristics.

Examples include:

- Low Risk Patients
- Chronic Disease Patients
- High Cost Patients
- Frequent Visitors
- Preventive Care Patients

---

## 3. Risk Stratification

Provides patient risk metrics including:

- High Risk Population
- Disease Burden
- Chronic Conditions
- Readmission Risk
- Clinical Risk Scores

---

## 4. Clinical Analytics

Clinical insights including:

- Diagnosis Distribution
- Disease Trends
- Clinical Indicators
- Laboratory Metrics

---

## 5. Cost Analytics

Financial insights such as:

- Total Healthcare Cost
- Average Claim Cost
- Cost by Patient
- Cost Distribution
- High Cost Population

---

## 6. Utilization Analytics

Healthcare utilization metrics including:

- Encounter Counts
- Visit Frequency
- Service Utilization
- Resource Consumption

---

## 7. Executive Dashboard

Enterprise summary displaying:

- Patient KPIs
- Clinical KPIs
- Financial KPIs
- Utilization KPIs
- Risk KPIs

---

# REST API

The backend provides REST APIs for each analytics module.

Example endpoints include:

```
/patient
/segment
/risk
/clinical
/cost
/utilization
/dashboard
```

Interactive API documentation:

```
http://localhost:8000/docs
```

ReDoc:

```
http://localhost:8000/redoc
```

---

# Installation

## Clone Repository

```bash
git clone <repository-url>

cd Patient_Segmentation
```

---

# Backend Setup

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run FastAPI

```bash
cd backend/patient-segmentation-python-app

uvicorn main:app --reload
```

Server

```
http://localhost:8000
```

---

# Frontend Setup

Navigate

```bash
cd ui/reactjs/patient-segmentation-react-app
```

Install packages

```bash
npm install
```

Run

```bash
npm run dev
```

Application

```
http://localhost:5173
```

---

# Build Production

```bash
npm run build
```

Preview

```bash
npm run preview
```

---

# API Documentation

Swagger UI

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# Backend Layers

The project follows a layered architecture.

```
Router

↓

Service

↓

Implementation

↓

Utility Layer

↓

Healthcare Dataset
```

---

# Features

- FastAPI REST APIs
- React TypeScript Frontend
- Modular Architecture
- Healthcare Analytics
- Population Health Dashboard
- Patient Segmentation
- Risk Stratification
- Clinical Analytics
- Cost Analytics
- Utilization Analytics
- Interactive Dashboard
- Enterprise Project Structure

---

# Future Enhancements

- Machine Learning Based Segmentation
- K-Means Clustering
- DBSCAN Clustering
- Hierarchical Clustering
- Predictive Risk Models
- Authentication & Authorization
- Database Integration
- Docker Support
- Kubernetes Deployment
- Cloud Deployment (Azure/AWS/GCP)
- CI/CD Pipelines

---

# Development Workflow

```
React UI

↓

Axios API Layer

↓

FastAPI Router

↓

Service Layer

↓

Analytics Implementation

↓

Healthcare Dataset
```

---

# Author

Patient Segmentation Analytics Platform

Built using:

- FastAPI
- React
- TypeScript
- Healthcare Analytics
- Python
- Pandas

---

# License

This project is intended for educational, research, and healthcare analytics purposes.