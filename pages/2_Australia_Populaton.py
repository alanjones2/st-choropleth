import streamlit as st
import pandas as pd
import plotly.express as px
import json

st.set_page_config(layout="wide")

st.title("Population of Australian States")
st.info("Hover over the map to see the names of the states and their population")

f = open('geo/australia.geojson')
oz = json.load(f)
#oz["features"][1]


df = pd.read_csv('data/Australian Bureau of Statistics.csv')

col1, col2 = st.columns(2)

fig = px.choropleth(df, geojson=oz, 
                    color="Population at 31 March 2023 ('000)",
                    locations="State", 
                    featureidkey="properties.name",
                    color_continuous_scale="Reds",
                    range_color=(0, 10000),
                    fitbounds = 'geojson',
                    template = 'plotly_dark'
                   )
col1.plotly_chart(fig)

fig = px.scatter_geo(df, geojson=oz, 
                    color="Population at 31 March 2023 ('000)",
                    size="Population at 31 March 2023 ('000)",
                    locations="State", 
                    featureidkey="properties.name",
                    color_continuous_scale="Blues",
                    range_color=(0, 10000),
                    fitbounds = 'geojson',
                    template = 'plotly_dark'
                   )
col2.plotly_chart(fig)