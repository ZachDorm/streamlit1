import streamlit as st
import leafmap
from leafmap import foliumap as leafmap
import xyzservices.providers as xyz
import basal_and_bark
from basal_and_bark import basal_and_bark as basal


st.title("This is a demo of a map that allows the user to add a basemap to a map. There is a dropdown list, and a box where you can enter a url pointing to xyz services.")
st.expander("test")
m= basal_and_bark.Map(center = [40,-100], zoom = 4, test = "test", scroll_wheel_zoom = True)
m= leafmap.Map(center = [40,-100], zoom = 4, test = "test", scroll_wheel_zoom = True)

radio = st.radio('URL or dropdown', ('URL', 'dropdown'))

col1, col2 = st.columns([4,1])

with col2:


    if radio == 'URL':
        input = st.text_input('Please enter url for basemap', 'Esri.WorldImagery')
        #basemap = eval(f"xyz.{input}")
        #url = basemap.build_url()
        m.add_tile_layer(url=input, name="map", attribution = ' ')

    else:
        base = st.selectbox('Please select a basemap', ('Topo', 'ShadeRelief', 'Gray'))

        if base == "Topo":
            m.add_basemap(basemap= "Esri.WorldTopoMap")
        if base == "ShadeRelief":
            m.add_basemap(basemap= "Esri.WorldShadedRelief")
        if base == "Gray":
            m.add_basemap(basemap= "Esri.WorldGrayCanvas")
with col1:

    m.to_streamlit(height=700)
