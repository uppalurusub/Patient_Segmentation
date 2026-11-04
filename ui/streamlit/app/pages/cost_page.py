from components.sidebar import render_sidebar
import streamlit as st
import pandas as pd
import plotly.express as px
from api.client import get_data




render_sidebar()

st.header("Cost Analytics")

summary = get_data(
"/cost/summary"
)

c1, c2, c3, c4= st.columns(4)

c1.metric(
"Total Cost",
round(summary["total_cost"],2)
)

c2.metric(
"Average Cost",
round(summary["average_cost"],2)
)

c3.metric(
"Maximun Cost",
round(summary["maximum_cost"],2)
)

c4.metric(
"Minimun Cost",
round(summary["minimum_cost"],2)
)

st.divider()

trend = get_data(
"/cost/monthly-trend"
)

if trend:

    st.subheader(
    "Monthly Cost Trend"
    )

    trend_df = pd.DataFrame(trend)

    
    
    fig = px.line(
        trend_df,
        x="month",
        y="total_cost",
        title="Monthly Trend"
    )

    st.plotly_chart(
        fig,
        width='stretch'
    )

    st.dataframe(
    pd.DataFrame(trend_df)
    )

st.divider()

st.title("High Cost Patients")

high_cost = get_data(
"/cost/high-cost-patients"
)

if high_cost:

    st.dataframe(
    pd.DataFrame(high_cost)
    )