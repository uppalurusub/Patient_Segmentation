from components.sidebar import render_sidebar
import streamlit as st
import pandas as pd
import plotly.express as px
from api.client import get_data




render_sidebar()

st.header("Clinical Analytics")

summary = get_data(
"/clinical/summary"
)

c1, c2, c3= st.columns(3)

c1.metric(
"Total Patients",
summary["total_patients"]
)

c2.metric(
"Chronic Patients",
summary["chronic_patients"]
)

c3.metric(
"Abnormal Lab Patients",
summary["abnormal_lab_patients"]
)

st.divider()

diagnoses = get_data(
"/clinical/top-diagnoses"
)

if diagnoses:

    st.subheader(
    "Top Diagnoses"
    )


    st.dataframe(
    pd.DataFrame(diagnoses)
    )

prevalence = get_data(
"/clinical/disease-prevalence"
)

if prevalence:

    st.subheader(
    "Disease Prevalence"
    )

    prevalence_df = pd.DataFrame(prevalence)

    

    fig = px.bar(
        prevalence_df,
        x="diagnosis",
        y=["patient_count"],
        title="Disease Prevalence Distribution"
    )

    st.plotly_chart(
        fig,
        width='stretch'
    )

    st.dataframe(
    pd.DataFrame(prevalence)
    )

