from components.sidebar import render_sidebar
import streamlit as st

from api.client import get_data
from utils.charts import pie_chart
import pandas as pd
import plotly.express as px



render_sidebar()

st.header("Patient Analytics")

kpis = get_data("/patients/kpis")

if kpis:

    cols = st.columns(len(kpis))

    for i, (k, v) in enumerate(kpis.items()):

        cols[i].metric(k, v)

age = get_data(
"/patients/analytics/age-distribution"
)

if age:
    st.subheader("Age Distribution")
    
    age_df = pd.DataFrame(age)

    

    

    fig = px.bar(
        age_df,
        x="age_group",
        y="count",
        
        title="Age Distribution"
    )

    st.plotly_chart(
        fig,
        width='stretch'
    )

    st.dataframe(
    pd.DataFrame(age_df)
    )

gender = get_data(
"/patients/analytics/gender-distribution"
)

if gender:
    pie_chart(
    gender,
    "gender",
    "count",
    "Gender Distribution"
    )