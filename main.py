import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import chartpage
import table

st.set_page_config(layout="wide", page_icon=":car:", page_title="Car Sale Dashboard")

page = st.sidebar.selectbox("Select Page Option", ["Chart Page", "Table Page"])


if page == "Chart Page":
    chartpage.show_page()

else:
    table.show_page()
