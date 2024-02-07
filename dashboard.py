from datetime import timedelta
import streamlit as st

from db import load_db
from tabs.construction import construction
from tabs.current import current
from tabs.credits import credits
from pytimeparse.timeparse import timeparse

from tabs.ships import ships

st.set_page_config(layout="wide")


def main():
    st.title("SpaceTraders Leaderboard")
    tab_current, tab_credits, tab_ships, tab_construction = st.tabs(
        ["Current", "Credits", "Ships", "Construction"]
    )

    df = load_db()

    current_data = df.groupby("agent_id").last().sort_values("credits", ascending=False)
    agents = current_data.agent_symbol
    with st.sidebar:
        selected_duration = st.selectbox(
            f"Select duration: ", ["1h", "6h", "1d", "7d", "all"], index=3
        )
        selected_frequency = st.selectbox(
            f"Select frequency for windows: ", ["1min", "30min", "1h", "6h"], index=3
        )
        selected_agents = st.multiselect(
            f"Select agents: ", agents, default=agents.iloc[:20]
        )

    df = df.query("agent_symbol in @selected_agents")
    if selected_duration != "all":
        last_time = df.timestamp.max()
        from_time = last_time - timedelta(seconds=timeparse(selected_duration))
        df = df.query("timestamp > @from_time")

    with tab_current:
        current(df)
    with tab_credits:
        credits(
            df,
            freq=selected_frequency,
        )
    with tab_ships:
        ships(
            df,
            freq=selected_frequency,
        )
    with tab_construction:
        construction(
            df,
            freq=selected_frequency,
        )


main()
