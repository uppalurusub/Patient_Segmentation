from components.sidebar import render_sidebar
import streamlit as st
import pandas as pd
import plotly.express as px
from api.client import get_data




render_sidebar()

st.header(
"Utilization Analytics"
)

summary = get_data(
"/utilization/summary"
)

c1, c2, c3, c4= st.columns(4)

c1.metric(
"Total Visits",
round(summary["total_visits"],2)
)

c2.metric(
"Average Visits Per Patient",
round(summary["average_visits_per_patient"],2)
)

c3.metric(
"Average Length Of Stay",
round(summary["average_los"],2)
)

c4.metric(
"Readmission Rate %",
round(summary["readmission_rate_pct"],2)
)

visits = get_data(
"/utilization/visit-distribution"
)

if visits:

    st.subheader(
    "Visit Distribution"
    )

    st.bar_chart(
    pd.DataFrame(visits)
    )

    st.dataframe(
    pd.DataFrame(visits)
    )

los = get_data(
"/utilization/los-distribution"
)

if los:

    st.subheader(
    "Length Of Stay"
    )

    los_df = pd.DataFrame(los)

    order = [
        "0-2",
        "3-5",
        "6-10",
        "11-20",
        "20+"
    ]

    fig = px.bar(
        los_df,
        x="los_group",
        y="count",
        category_orders={
            "los_group": order
        },
        title="Length Of Stay Distribution"
    )

    st.plotly_chart(
        fig,
        width='stretch'
    )

    st.dataframe(
    pd.DataFrame(los)
    )