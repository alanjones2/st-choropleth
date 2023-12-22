import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
# Towards a GIS using Plotly and Streamlit
---
            
### Select the pages from the sidebar to see demonstrations of the various aspects of Plotly's map functions.

#### The app is is described and documented in the tutorial [__*How to create a GIS with Plotly and Streamlit*__](https://towardsdatascience.com/how-to-create-a-simple-gis-map-with-plotly-and-streamlit-7732d67b84e2).
            
---
""")

col2, col3, col4 = st.columns(3)
                       
col2.image("images/1_VyS4gt40OKHc_i6FSRGIrA.png")
col3.image("images/Screenshot 2023-03-08 194017.png")
col4.image("images/Screenshot 2023-12-20 200434.png")
