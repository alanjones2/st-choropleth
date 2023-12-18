####################################
# Global CO2 Emissions dashboard
# (c) Alan Jones, 2023
####################################

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# the data is local but it might better to cache it
@st.cache_data
def get_data():
    df_w = pd.read_csv('data/co2_total_world.csv')
    df_w = df_w.drop(columns=['Unnamed: 0'])
    df_total = pd.read_csv('data/co2_total.csv')
    df_total = df_total.drop(columns=['Unnamed: 0'])
    countries = df_total['Entity'].unique()
    return df_w, df_total, countries

# set dataframes, and countries list
df_w, df_total, countries = get_data()

# initialise the year if not already set
if 'year' not in st.session_state:
    st.session_state['year'] = 2021



#
# Define layout
#
# header bar 
# - contains header text in the first and the global emissions for the selected year
colh1, colh2 = st.columns((4,2))
colh1.markdown("## Global CO2 Emissions")
colh2.markdown("")  # this will be overwritten in the app

# body columns
# - the first column contains the map of global emissions
# - the second column contains graphs for emissions from selected countries 
col1, col2 = st.columns ((8,4))

# footer - acknowledgements, etc
footer = st.container()
footer.write("Global CO2 Emission Data from 1750 to 2021. Data derived, with thanks, from [__*Our World in Data*__](https://ourworldindata.org/)")

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
    # get the year with a slider
    st.session_state['year'] = st.slider('Select year',first_year,last_year, key=col)

    # set projection
    p = 'equirectangular'   # default projection

    # create the maps
    fig1 = px.scatter_geo(df_total[df_total['Year']==st.session_state['year']], 
                        locations="Code",       # The ISO code for the Entity (country)
                        color=col,              # color is set by this column
                        size=col,               # size of the scatter dot mirrors the color
                        hover_name="Entity",    # hover name is the name of the Entity (country)
                        range_color=(min,max),  # the range of values as set above
                        scope= 'world',         # a world map - the default
                        projection=p,           # the project as set above
                        title='World CO2 Emissions',
                        template = 'plotly_dark',
                        color_continuous_scale=px.colors.sequential.Reds
                        )
    fig1.update_layout(margin={'r':0, 't':0, 'b':0, 'l':0})  # maximise the figure size
    fig2 = px.choropleth(df_total[df_total['Year']==st.session_state['year']], 
                        locations="Code",       # The ISO code for the Entity (country)
                        color=col,              # color is set by this column
                        hover_name="Entity",    # hover name is the name of the Entity (country)
                        range_color=(min,max),  # the range of values as set above
                        scope= 'world',         # a world map - the default
                        projection=p,           # the project as set above
                        title='World CO2 Emissions',
                        template = 'plotly_dark',
                        color_continuous_scale=px.colors.sequential.Reds
                        )
    fig2.update_layout(margin={'r':0, 't':0, 'b':0, 'l':0})  # maximise the figure size
    
    map = st.radio(
    "Choose the map style",
    ["Scatter", "Choropleth"], horizontal = True)
    fig = fig1 if map == 'Scatter' else fig2

    # plot the map
    st.plotly_chart(fig, use_container_width=True)

# the second body column contains a selector for countries and a line chart for each selected country
with col2:
    # add/subtract from the selected countries
    c = st.multiselect('Add a country:', countries, default=['United States', 'China', 'Russia', 'Germany'])
    tab1, tab2 = col2.tabs(["Graph", "Table"])

    with tab1:
        # plot a line graph of emissions for selected countries
        fig = px.line(df_total[df_total['Entity'].isin(c)], x='Year', y='Annual CO₂ emissions', color = 'Entity')
        st.plotly_chart(fig, use_container_width=True)
    with tab2:
        table = df_total[df_total['Year']==st.session_state['year']]
        st.dataframe(table[table['Entity'].isin(c)], use_container_width=True)

# set the header with the new year data
emissions = df_w[df_w['Year']==st.session_state['year']]['Annual CO₂ emissions']
colh2.metric(label=f"__Total emissions for {st.session_state['year']}__", value=emissions)


