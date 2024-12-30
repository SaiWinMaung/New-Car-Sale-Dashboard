import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import chartpage
import table

page = st.sidebar.selectbox('Select Page Option', ['Chart Page', 'Table Page'])


if page == 'Chart Page':
    chartpage.show_page()

else :
    table.show_page()