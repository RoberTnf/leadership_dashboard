import streamlit as st
import plotly.express as px


def credits(df, freq):
    order = {
        "agent_symbol": df.groupby("agent_symbol")
        .last()
        .sort_values("credits", ascending=False)
        .index
    }
    st.title("Credits")
    st.plotly_chart(
        px.line(
            df, x="timestamp", y="credits", color="agent_symbol", category_orders=order
        ),
        use_container_width=True,
    )
    st.title("Credits change")
    change = (
        df.groupby("agent_symbol")
        .apply(
            lambda x: x.set_index("timestamp")
            .resample(freq)["credits"]
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
            y="credits",
            color="agent_symbol",
            category_orders=order,
        ),
        use_container_width=True,
    )
