import streamlit as st
import plotly.express as px


def current(df):
    col1, col2 = st.columns(2)
    current_data = df.groupby("agent_id").last().sort_values("credits", ascending=False)

    with col1:
        st.title("Credits")
        st.plotly_chart(
            px.histogram(
                current_data, x="agent_symbol", y="credits", color="agent_symbol"
            ),
            use_container_width=True,
        )

        st.title("FAB_MATS")
        st.plotly_chart(
            px.histogram(
                current_data, x="agent_symbol", y="FAB_MATS", color="agent_symbol"
            ),
            use_container_width=True,
        )

    with col2:
        st.title("Ship Count")
        st.plotly_chart(
            px.histogram(
                current_data, x="agent_symbol", y="ship_count", color="agent_symbol"
            ),
            use_container_width=True,
        )

        st.title("ADVANCED_CIRCUITRY")
        st.plotly_chart(
            px.histogram(
                current_data,
                x="agent_symbol",
                y="ADVANCED_CIRCUITRY",
                color="agent_symbol",
            ),
            use_container_width=True,
        )
