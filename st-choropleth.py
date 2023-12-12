import streamlit as st
import pandas as pd
import plotly.express as px
import json

df_total = pd.read_csv('co2_total.csv')
col = 'Annual CO₂ emissions'
max = df_total[col].max()
min = df_total[col].min()

first_year = 1950 #df_total['Year'].min()
last_year = df_total['Year'].max()
year = st.slider('Select year',first_year,last_year, key=col)

fig = px.choropleth(df_total[df_total['Year']==year], locations="Code",
                    color=col,
                    hover_name="Entity",
                    range_color=(min,max),
                    scope= 'world',

                    projection="natural earth",
                    color_continuous_scale=px.colors.sequential.Reds)
st.plotly_chart(fig)

fig = px.choropleth(df_total[df_total['Year']==year], locations="Code",
                    color=col,
                    hover_name="Entity",
                    range_color=(min,max),
                    scope= 'world',
                    projection="orthographic",
                    color_continuous_scale=px.colors.sequential.Reds)
st.plotly_chart(fig)

#################

f = open('australia.geojson')
oz = json.load(f)
#oz["features"][2]['properties']

df = pd.read_csv('Australian Bureau of Statistics.csv')

fig = px.choropleth(df, geojson=oz, color="Population at 31 March 2023 ('000)",
                    locations="State", featureidkey="properties.name",
                    projection="equirectangular",
                    range_color=(200,10000),
                    color_continuous_scale=px.colors.sequential.Peach
                   )
fig.update_geos(fitbounds="locations")#, visible=True)
st.plotly_chart(fig)