import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
st.set_page_config(layout="wide", page_icon=":car:", page_title="Car Sale Dashboard")

def show_page():
    df = pd.read_csv("cars.csv", index_col=0)

    df = df.rename(columns={"Foreign/Local Used": "Foregin_Local_Used"})


    st.sidebar.header("Please Filter here")


    automation = st.sidebar.radio(
        "Select the Automation", options=df["Automation"].unique()
    )

    categories = st.sidebar.radio(
        "Select the Local or Foregin", options=df["Foregin_Local_Used"].unique()
    )

    df_selection = df.query(
        "Automation == @automation & Foregin_Local_Used == @categories "
    )

    st.title(":car: Car Sale Dashboard")
    st.write("##")

    average_price = int(df_selection["price"].mean() / 1000)
    car_count = df_selection.shape[0]
    earliest_make_year = df_selection["make-year"].min()

    left_column, middle_column, right_column = st.columns(3)

    with left_column:
        st.header("Average Price")
        st.subheader(f"US $ {average_price}")

    with middle_column:
        st.header("Car Count")
        st.subheader(f"{car_count :,} Cars")

    with right_column:
        st.header("Earliest Make Year")
        st.subheader(f"{earliest_make_year}")

    st.divider()

    price_per_color = (
        df_selection.groupby(by=["color"])[["price"]].sum().sort_values("price")
    )

    fig_price_per_color = px.bar(
        price_per_color,
        y=price_per_color.index,
        x="price",
        template="plotly_white",
        color_discrete_sequence=["#9d408b"] * len(price_per_color),
    )

    price_by_make = (
        df_selection.groupby(by="manufacturer")[["price"]].sum().sort_values("price")
    )

    fig_price_by_make = px.bar(
        price_by_make,
        x=price_by_make.index,
        y="price",
        template="plotly_white",
        color_discrete_sequence=["#9d408b"] * len(price_per_color),
    )

    graph1, graph2 = st.columns(2)

    with graph1:
        st.plotly_chart(fig_price_per_color, use_container_width=True)

    with graph2:
        st.plotly_chart(fig_price_by_make, use_container_width=True)

    st.divider()

    seat_make_dist = (
        df.groupby("seat-make")[["price"]].agg("count").sort_values("seat-make")
    )

    fig_seat_dist = px.pie(
        seat_make_dist,
        values="price",
        names=seat_make_dist.index,
        title="<b> Seat Make Distribution </b>",
        hole=0.4,
    )

    fig_make_year = px.histogram(
        df_selection, x="make-year", title="<b> Make Year Distribution </b>"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        min_price = df_selection["price"].min()
        col1.metric(label="Minimum Price of Car", value=int(min_price / 1000))

    with col1:
        max_price = df_selection["price"].max()
        col1.metric(label="Maximum Price of Car", value=int(max_price / 1000))

    with col1:
        median_price = df_selection["price"].median()
        col1.metric(label="Median Price of Car", value=int(median_price / 1000))

    with col2:
        st.plotly_chart(fig_seat_dist, use_container_width=True)

    with col3:
        st.plotly_chart(fig_make_year, use_container_width=True)
