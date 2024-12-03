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

st.title("江汉平原的多时相影像与春季遥感影像的比较")
st.markdown("""
左图为三月的影像，以第1、2、3波段赋值给rgb波段；
右图为以3、5、7月三个关键物候期的中值合成影像分别赋值给rgb通道的多时相影像
""", unsafe_allow_html=True)


m = leafmap.Map()
m.split_map(
    #left_layer="ESA WorldCover 2020 S2 FCC", right_layer="ESA WorldCover 2020"
    left_layer="https://github.com/snowedinh/gis/raw/refs/heads/main/Spring_tiff_cropped.tif", 
    right_layer="https://github.com/snowedinh/gis/raw/refs/heads/main/timeWindowComposite_tiff_cropped.tif"
)
#m.add_legend(title="ESA Land Cover", builtin_legend="ESA_WorldCover")
# Show map in Streamlit
m.to_streamlit(height=500)
"""
