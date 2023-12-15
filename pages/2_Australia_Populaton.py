import streamlit as st
import pandas as pd
import plotly.express as px
import json

st.title("Australian states population")
st.info("Hover over the map to see the names of the states and their population")

f = open('geo/australia.geojson')
oz = json.load(f)
# oz["features"][0]


df = pd.read_csv('data/Australian Bureau of Statistics.csv')

fig = px.choropleth(df, geojson=oz, color="Population at 31 March 2023 ('000)",
                    locations="State", featureidkey="properties.name",
                    projection="mercator",
                    color_continuous_scale="Reds",
                    range_color=(0, 10000),
                    template = 'plotly_dark'
                   )
fig.update_geos(fitbounds="locations")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig)