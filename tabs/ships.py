import streamlit as st
import plotly.express as px


def ships(df, freq):
    order = {
        "agent_symbol": df.groupby("agent_symbol")
        .last()
        .sort_values("ship_count", ascending=False)
        .index
    }
    st.title("Ships")
    st.plotly_chart(
        px.line(
            df,
            x="timestamp",
            y="ship_count",
            color="agent_symbol",
            category_orders=order,
        ),
        use_container_width=True,
    )
    st.title("Ships Change")
    change = (
        df.groupby("agent_symbol")
        .apply(
            lambda x: x.set_index("timestamp")
            .resample(freq)["ship_count"]
            .last()
            .ffill()
            .diff()
        )
        .reset_index()
    )
    st.plotly_chart(
        px.line(
            change,
            x="timestamp",
            y="ship_count",
            color="agent_symbol",
            category_orders=order,
        ),
        use_container_width=True,
    )
