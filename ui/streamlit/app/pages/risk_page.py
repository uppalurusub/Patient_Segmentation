from components.sidebar import render_sidebar
import streamlit as st
import pandas as pd
import plotly.express as px
from api.client import get_data




render_sidebar()

st.header("Risk Analytics")

summary = get_data(
"/risk/summary"
)

c1, c2, c3= st.columns(3)

c1.metric(
"Average Risk Score",
summary["average_risk_score"]
)

c2.metric(
"Maximum Risk Score",
summary["maximum_risk_score"]
)

c3.metric(
"Minimum Risk Score",
summary["minimum_risk_score"]
)

st.divider()

distribution = get_data(
"/risk/distribution"
)

if distribution:

    st.subheader(
    "Risk Distribution"
    )

    

    dis_df = pd.DataFrame(distribution)

    order = [
        "Low",
        "Medium",
        "High"
    ]

    fig = px.bar(
        dis_df,
        x="risk_category",
        y="count",
        category_orders={
            "risk_category": order
        },
        title="Risk Distribution"
    )

    st.plotly_chart(
        fig,
        width='stretch'
    )

    st.dataframe(
    pd.DataFrame(dis_df)
    )

    

high_risk = get_data(
"/risk/high"
)

if high_risk:

    st.subheader(
    "High Risk Patients"
    )

    st.dataframe(
    pd.DataFrame(high_risk)
    )