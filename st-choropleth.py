import streamlit as st
import pandas as pd
import plotly.express as px
import random

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
