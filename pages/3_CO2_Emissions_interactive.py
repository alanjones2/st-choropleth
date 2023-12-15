import streamlit as st
import pandas as pd
import plotly.express as px
import json

st.title("CO2 Emissions")
st.write("""The following maps display the CO2 emissions for a
            range of countries over a range of time""")

st.info("""Use the slider to selct a year to display
           the total emissions for each country. 
           Scroll down to see an interactive 3D representation.""")

st.write("""This map uses the 'Natural Earth' projection""")

df_total = pd.read_csv('data/co2_total.csv')
col = 'Annual CO₂ emissions'
max = df_total[col].max()
min = df_total[col].min()

# To get the whole range replace 1950 with the comment that follows it
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

st.write("""This map uses the 'Orthographic' projection.
Click on the globe and move the pointer to rotate it.
""")

fig = px.choropleth(df_total[df_total['Year']==year], locations="Code",
                    color=col,
                    hover_name="Entity",
                    range_color=(min,max),
                    scope= 'world',
                    projection="orthographic",
                    color_continuous_scale=px.colors.sequential.Reds)
st.plotly_chart(fig)