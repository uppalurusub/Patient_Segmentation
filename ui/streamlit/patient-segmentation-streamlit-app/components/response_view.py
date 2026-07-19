from typing import Any

import pandas as pd
import streamlit as st


def render_response(
    data: Any,
    *,
    title: str | None = None,
    empty_message: str = "No data available.",
) -> None:
    if title:
        st.subheader(title)

    if data is None or data == [] or data == {}:
        st.info(empty_message)
        return

    if isinstance(data, list):
        st.dataframe(pd.DataFrame(data), width="stretch")
        return

    if isinstance(data, dict):
        scalar_values = all(
            not isinstance(value, (dict, list))
            for value in data.values()
        )
        if scalar_values:
            st.dataframe(
                pd.DataFrame([data]),
                width="stretch",
                hide_index=True,
            )
        else:
            for key, value in data.items():
                st.markdown(f"**{key.replace('_', ' ').title()}**")
                render_response(value)
        return

    st.write(data)
