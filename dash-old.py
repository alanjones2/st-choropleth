import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df_w = pd.read_csv('data/co2_total_world.csv')
df_total = pd.read_csv('data/co2_total.csv')

if 'year' not in st.session_state:
    st.session_state['year'] = 2021

#
# Define layout
#
# header bar 
# - contains header text in the first and the global emissions for the selected year
colh1, colh2 = st.columns((4,2))
colh1.markdown("""## Global CO2 Emissions""")
colh2.markdown("")  # this will be overwritten in the app

# body columns
# - the first column contains the map of global emissions
# - the second column contains graphs for emissions from selected countries 
col1, col2 = st.columns ((8,4))

# footer - acknowledgements, etc
footer = st.container()
footer.write("footer - TBA")

#
# App logic
#

# define parameters for map graphic
col = 'Annual CO₂ emissions'    # the column that contains the emissions data
max = df_total[col].max()       # maximum emissions value for color range
min = df_total[col].min()       # minimum emissions value for color range

# define the year range for the slider
# to get the whole range replace 1950 with the comment that follows it
first_year = 1950 #df_total['Year'].min()
last_year = df_total['Year'].max()

# The first body column contains the map
with col1:
    # set the year with a slider
    st.session_state['year'] = st.slider('Select year',first_year,last_year, key=col)

    # selections of the various projections (disabled)
    p = 'equirectangular'   #default projection
    #projections =['equirectangular', 'mercator', 'orthographic', 'natural earth', 'kavrayskiy7', 'miller', 'robinson', 'eckert4', 'azimuthal equal area', 'azimuthal equidistant', 'conic equal area', 'conic conformal', 'conic equidistant', 'gnomonic', 'stereographic', 'mollweide', 'hammer', 'transverse mercator', 'albers usa', 'winkel tripel', 'aitoff', 'sinusoidal']
    #p = st.selectbox('Which projection do you want to use for the map?', projections)

    # create the map
    fig = px.scatter_geo(df_total[df_total['Year']==st.session_state['year']], locations="Code",
                        color=col,
                        size=col,
                        hover_name="Entity",
                        range_color=(min,max),
                        scope= 'world',
                        projection=p,
                        title='World CO2 Emissions',
                        template = 'plotly_dark',
                        color_continuous_scale=px.colors.sequential.Reds
                        )
    fig.update_layout(margin={'r':50, 't':0, 'b':0, 'l':0})
    #fig.update_coloraxes(showscale=False) # remove color bar legend
    #config={'staticPlot':False}
    
    st.plotly_chart(fig, use_container_width=True,)#  **{'config': config})

    #col3, col4 = st.columns(2)
    #with col4:
    #    fig = px.choropleth(df_total[df_total['Year']==year], locations="Code",
    #            color=col,
    #            hover_name="Entity",
    #            range_color=(min,max),
    #            scope= 'world',
    #            projection="orthographic",
    #            height=400,
    #           color_continuous_scale=px.colors.sequential.Reds)
    #    st.plotly_chart(fig, use_container_width=True)
    #with col3:
    #    st.write("description")

with col2:
    countries = df_total['Entity'].unique()
    c = st.multiselect('Add a country?', countries)
    fig = px.line(df_total[df_total['Entity'].isin(c)], x='Year', y='Annual CO₂ emissions', color = 'Entity')
    st.plotly_chart(fig, use_container_width=True)

# set the header with the new year data
emissions = df_w[df_w['Year']==st.session_state['year']]['Annual CO₂ emissions']
colh2.metric(label=f"__Total emissions for {st.session_state['year']}__", value=emissions)
