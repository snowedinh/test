import streamlit as st
import leafmap.foliumap as leafmap
import folium

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

m = leafmap.Map()
m.split_map(
    #left_layer="ESA WorldCover 2020 S2 FCC", right_layer="ESA WorldCover 2020"
    left_layer="https://github.com/snowedinh/gis/raw/refs/heads/main/Spring_tiff_cropped.tif", 
    right_layer="https://github.com/snowedinh/gis/raw/refs/heads/main/timeWindowComposite_tiff_cropped.tif"
)
#m.add_legend(title="ESA Land Cover", builtin_legend="ESA_WorldCover")

legend_html = """
<div style="position: fixed; 
            bottom: 10px; right: 10px; width: 200px; height: 150px; 
            border:2px solid grey; background-color:white; 
            z-index:9999; font-size:14px; padding: 10px;">
<b>耕地分类</b><br>
<img src="https://www.colorhexa.com/000000.png" width="30" height="30"> Low NDVI (Black)<br>
<img src="https://www.colorhexa.com/bfbfbf.png" width="30" height="30"> High NDVI (Gray)<br>
</div>
"""
