import streamlit as st
import pandas as pd
import plotly.express as px
import json

st.title("CO2 Emissions")
st.write("""The following map displays the CO2 emissions for a
            range of countries over a range of time""")

st.info("""This an example of simple outline maps in Plotly, for
different parts of the World
""")

col1, col2 = st.columns(2)

df_total = pd.read_csv('data/co2_total.csv')
df_total_2021 = df_total[df_total['Year']==2021]
col = 'Annual CO₂ emissions'
max = df_total_2021[col].max()
min = df_total_2021[col].min()

# No scope is specifies in the first map: 'world' is the default

fig = px.choropleth(df_total_2021, locations="Code",
                    color=col,
                    hover_name="Entity",
                    range_color=(min,max),
                    template = 'plotly_dark',
                    title = 'World'
                    )
col1.plotly_chart(fig)

# Define scope as 'europe'

fig = px.choropleth(df_total_2021, locations="Code",
                    scope = 'europe',
                    color=col,
                    hover_name="Entity",
                    range_color=(min,max),
                    template = 'plotly_dark',
                    title = 'Europe'
                    )
col2.plotly_chart(fig)

# Define scope as 'asia'

fig = px.choropleth(df_total_2021, locations="Code",
                    scope = 'asia',
                    color=col,
                    hover_name="Entity",
                    range_color=(min,max),
                    template = 'plotly_dark',
                    title = 'Asia'
                    )
col1.plotly_chart(fig)

# Define scope as 'north america'

fig = px.choropleth(df_total_2021, locations="Code",
                    scope = 'north america',
                    color=col,
                    hover_name="Entity",
                    range_color=(min,max),
                    template = 'plotly_dark',
                    title = 'North America'
                    )
col2.plotly_chart(fig)
