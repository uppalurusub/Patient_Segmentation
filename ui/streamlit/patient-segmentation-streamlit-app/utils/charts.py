import pandas as pd
import plotly.express as px
import streamlit as st


def bar_chart(data, x_col, y_col, title):

    df = pd.DataFrame(data)

    fig = px.bar(
        df,
        x=x_col,
        y=y_col,
        title=title
    )

    st.plotly_chart(
        fig,
        width='stretch'
    )


def pie_chart(data, names, values, title):

    df = pd.DataFrame(data)

    fig = px.pie(
        df,
        names=names,
        values=values,
        title=title
    )

    st.plotly_chart(
        fig,
        width='stretch'
    )