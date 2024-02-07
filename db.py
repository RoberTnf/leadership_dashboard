import streamlit as st
import pandas as pd
import sqlite3
from datetime import timedelta
import json


@st.cache_data(ttl=timedelta(minutes=5))
def load_db():
    con = sqlite3.connect("db.db")
    with con:
        df = pd.read_sql_query(
            """
            SELECT * FROM leaderboard_entry le
            JOIN crawl_run cr ON cr.id = le.crawl_run_id
            JOIN static_agent_detail sa ON sa.id=le.agent_id
                                     """,
            con,
        )

        df["construction_json"] = df["construction_json"].apply(lambda x: json.loads(x))
        df["FAB_MATS"] = df.construction_json.str["materials"].apply(
            lambda x: [f["fulfilled"] for f in x if f["tradeSymbol"] == "FAB_MATS"][0]
        )
        df["ADVANCED_CIRCUITRY"] = df.construction_json.str["materials"].apply(
            lambda x: [
                f["fulfilled"] for f in x if f["tradeSymbol"] == "ADVANCED_CIRCUITRY"
            ][0]
        )
        df["timestamp"] = pd.to_datetime(df["timestamp"])

    return df
