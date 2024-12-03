import streamlit as st
import leafmap.foliumap as leafmap
import os



st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

# Customize page title
st.title("空谱融合的地块级耕地种植状况遥感监测")

st.markdown(
    """
    融合高空间分辨率遥感影像的空间信息和时间序列遥感数据的谱信息，构建空谱融
合的遥感模型，实现江汉平原地块级的耕地种植状况监测
    """
)

st.header("研究区域的介绍")

markdown = """
以江汉平原地区一块小区域（如图所示）进行实证研究
"""
st.markdown(markdown)

m = leafmap.Map(center=[30.5469,112.8212],zoom=10,minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
