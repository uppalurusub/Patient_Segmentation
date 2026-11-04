from components.sidebar import render_sidebar
import pandas as pd
import streamlit as st

from api.client import get_data, post_data
from components.request_form import render_action_form
from components.response_view import render_response


render_sidebar()

st.header("Patient Segmentation")

result = render_action_form(
    title="Run Patient Segmentation",
    button_label="Run Segmentation",
    on_submit=lambda: post_data("/segments/run"),
)

if result is not None:
    st.success("Segmentation Complete")
    render_response(result, title="Segmentation Result")

distribution = get_data("/segments/distribution")

if distribution:
    st.subheader("Segment Distribution")
    distribution_df = pd.DataFrame(distribution)
    st.bar_chart(distribution_df)
    st.dataframe(distribution_df, width="stretch")

summary = get_data("/segments/summary")

if summary:
    render_response(summary, title="Segment Summary")
