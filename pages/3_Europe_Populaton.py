import streamlit as st
import pandas as pd
import plotly.express as px
import json

st.set_page_config(layout="wide")

st.title("Population of European Countries")
st.info("Hover over the map to see the names of the states and their population")

df = pd.read_csv('data/europop.csv')

col1, col2 = st.columns(2)

fig = px.choropleth(df, scope = 'europe',
                    color="Population (historical estimates)",
                    locations="Code", 
                    hover_name = 'Entity',
                    color_continuous_scale="Purples",
                    range_color=(0, 100000000),
                    fitbounds = 'locations',
                    template = 'plotly_dark',
                    title = "European populations"
                   )

col1.plotly_chart(fig)

fig = px.scatter_geo(df, scope = 'europe', 
                    color="Population (historical estimates)",
                    size="Population (historical estimates)",
                    locations="Code", 
                    hover_name = 'Entity',
                    color_continuous_scale="Purples",
                    range_color=(0, 100000000),
                    fitbounds = 'locations',
                    template = 'plotly_dark',
                    title = "European populations"
                   )

col2.plotly_chart(fig)