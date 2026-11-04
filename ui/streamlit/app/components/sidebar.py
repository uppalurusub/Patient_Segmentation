import streamlit as st

from config import BASE_URL


def render_sidebar() -> None:
    with st.sidebar:
        st.title("Healthcare Analytics")
        st.caption("Patient Segmentation Platform")
        st.divider()

        st.markdown(
            """
            Use the page navigation to access:

            - Executive Dashboard
            - Patient Analytics
            - Clinical Analytics
            - Risk Analytics
            - Cost Analytics
            - Utilization Analytics
            - Patient Segmentation
            """
        )

        st.divider()
        st.caption(f"API: {BASE_URL}")
