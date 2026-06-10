import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Geospatial Data Analysis")

df = pd.read_csv("data/sales_data.csv")

st.subheader("Sales Dataset")
st.dataframe(df)

state_sales = df.groupby("state")["sales"].sum().reset_index()

st.subheader("Sales Distribution Map")

fig = px.choropleth(
    state_sales,
    locations="state",
    locationmode="USA-states",
    color="sales",
    scope="usa",
    color_continuous_scale="Viridis",
)

st.plotly_chart(fig)

average_sales = state_sales["sales"].mean()

high_demand = state_sales[state_sales["sales"] > average_sales]

st.subheader("Recommended Expansion Locations")

st.write(
    "States with above-average sales are recommended for business expansion."
)

st.dataframe(high_demand)
