from collections.abc import Callable
from typing import Any

import streamlit as st


def render_action_form(
    title: str,
    button_label: str,
    on_submit: Callable[[], Any],
) -> Any:
    st.subheader(title)

    with st.form(key=f"{title.lower().replace(' ', '_')}_form"):
        submitted = st.form_submit_button(button_label, use_container_width=True)

    if submitted:
        with st.spinner("Processing request..."):
            return on_submit()

    return None
