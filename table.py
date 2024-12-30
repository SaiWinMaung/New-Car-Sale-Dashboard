import streamlit as st
import pandas as pd

def show_page():
    st.title('Car Sale Table')
    df = pd.read_csv("cars.csv", index_col=0)

    st.write(df)