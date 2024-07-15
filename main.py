import streamlit as st
import pandas as pd
import plotly.express as px
st.title("In Search for Happiness")

df = pd.read_csv("happy.csv")

xaxis = st.selectbox(label="Select the Data for the X-Axis", options=("GDP", "Happiness", "Generosity"))
yaxis = st.selectbox(label="Select the data for the Y-Axis", options=("GDP", "Happiness", "Generosity"))

match xaxis:
    case "GDP":
        x1 = df["gdp"]
    case "Happiness":
        x1 = df["happiness"]
    case "Generosity":
        x1 = df["generosity"]

match yaxis:
    case "GDP":
        y1 = df["gdp"]
    case "Happiness":
        y1 = df["happiness"]
    case "Generosity":
        y1 = df["generosity"]

st.subheader(f"{xaxis} and {yaxis}")

fig1 = px.scatter(x=x1, y=y1, labels={'x':xaxis, 'y': yaxis})
st.plotly_chart(fig1)
