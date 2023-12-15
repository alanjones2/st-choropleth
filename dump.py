import streamlit as st
import pandas as pd
import plotly.express as px
import json

def draw(df, col, max, min, first_year, last_year):


  year = st.slider('Select year',first_year,last_year, key=col)
  fig = px.choropleth(df[df['Year']==year], locations="Code",
                      color=col,
                      hover_name="Entity",
                      range_color=(min,max),
                      color_continuous_scale=px.colors.sequential.Reds)
  return fig


df_total = pd.read_csv('co2_total.csv')
col = 'Annual CO₂ emissions'
max = df_total[col].max()
min = df_total[col].min()

first_year = 1950 #df_total['Year'].min()
last_year = df_total['Year'].max()
fig = draw(df_total,'Annual CO₂ emissions', max, min, first_year, last_year )
st.plotly_chart(fig)

df_capita = pd.read_csv('co2-per-capita.csv')
col = 'Annual CO₂ emissions (per capita)'
max = 20 #df_capita[col].max()
min = df_capita[col].min()

first_year = 1950 #df_capita['Year'].min()
last_year = df_capita['Year'].max()
fig = draw(df_capita,col, max, min, first_year, last_year )
st.plotly_chart(fig)

f = open('australia.geojson')
oz = json.load(f)
oz["features"][2]['properties']

df = pd.read_csv('Australian Bureau of Statistics.csv')

fig = px.choropleth(df, geojson=oz, color="Population at 31 March 2023 ('000)",
                    locations="State", featureidkey="properties.name",
                    projection="mercator"
                   )
fig.update_geos(fitbounds="locations")#, visible=True)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig)

f = open('/geo/countries.geo.json')
world = json.load(f)

fig = px.choropleth_mapbox(df_total_2021, geojson=world, locations='Code', color=col,
                           color_continuous_scale="Reds",
                           range_color=(min,max),
                           mapbox_style="carto-positron",
                           zoom=0, center = {"lat": 0, "lon": 0},
                           opacity=0.2,
                           labels={col:col}
                        )
st.plotly_chart(fig)