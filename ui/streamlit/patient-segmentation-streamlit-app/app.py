import streamlit as st

from components.sidebar import render_sidebar

st.set_page_config(
    page_title="Healthcare Analytics Platform",
    page_icon="🏥",
    layout="wide",
)

render_sidebar()

st.title("🏥 Patient Segmentation")
st.markdown(
    """
    Welcome to the **Enterprise Patient Segmentation Dashboard**.

    Select a page from the navigation menu to explore population,
    clinical, risk, cost, utilization, and segmentation analytics.
    """
)

st.subheader("Modules Available")
st.markdown(
    """
    - Executive Dashboard
    - Patient Analytics
    - Clinical Analytics
    - Risk Analytics
    - Cost Analytics
    - Utilization Analytics
    - Patient Segmentation
    """
)
