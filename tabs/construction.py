import streamlit as st
import plotly.express as px


def construction(df, freq):
    df["total_materials"] = df.FAB_MATS + df.ADVANCED_CIRCUITRY
    order = {
        "agent_symbol": df.groupby("agent_symbol")
        .last()
        .sort_values("total_materials", ascending=False)
        .index
    }

    change = (
        df.groupby("agent_symbol")
        .apply(
            lambda x: x.set_index("timestamp")
            .resample(freq)[["FAB_MATS", "ADVANCED_CIRCUITRY"]]
            .last()
            .ffill()
            .diff()
        )
        .reset_index()
    )

    col1, col2 = st.columns(2)
    with col1:
        st.title("FAB_MATS")
        st.plotly_chart(
            px.line(
                df,
                x="timestamp",
                y="FAB_MATS",
                color="agent_symbol",
                category_orders=order,
            ),
            use_container_width=True,
        )
        st.title("FAB_MATS CHANGE")

        st.plotly_chart(
            px.line(
                change,
                x="timestamp",
                y="FAB_MATS",
                color="agent_symbol",
                category_orders=order,
            ),
            use_container_width=True,
        )

    with col2:
        st.title("ADVANCED_CIRCUITRY")
        st.plotly_chart(
            px.line(
                df,
                x="timestamp",
                y="ADVANCED_CIRCUITRY",
                color="agent_symbol",
                category_orders=order,
            ),
            use_container_width=True,
        )
        st.title("ADVANCED_CIRCUITRY CHANGE")

        st.plotly_chart(
            px.line(
                change,
                x="timestamp",
                y="ADVANCED_CIRCUITRY",
                color="agent_symbol",
                category_orders=order,
            ),
            use_container_width=True,
        )
