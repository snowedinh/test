import streamlit as st
import rasterio
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import io

# 配置页面布局
st.set_page_config(layout="wide")

# 添加Markdown信息
markdown = """
根据右侧影像的RGB波段值生成曲线
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("三时相的NDVI值与像元点的分布图")
st.markdown("""
分别提取多时相影像的各像元点的灰度值（NDVI的值），绘制直方图，反映各时相的耕地利用信息
""", unsafe_allow_html=True)


# 读取影像
image_url = "https://github.com/snowedinh/gis/raw/refs/heads/main/timeWindowComposite_tiff_cropped.tif"
rgb_image, red_band, green_band, blue_band = create_rgb_from_tiff(image_url)

# 获取影像尺寸
height, width, _ = rgb_image.shape

# 创建一个空的数组来存储每个像素点的RGB值的曲线
x_values = np.arange(0, width)

# 假设我们选择影像中间部分的行来生成曲线（避免绘制大量的像素数据）
y_index = height // 2  # 选择中间行

# 提取中间行的RGB波段值
red_values = red_band[y_index, :]
green_values = green_band[y_index, :]
blue_values = blue_band[y_index, :]

# 绘制曲线图
fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(x_values, red_values, label="Red", color='r')
ax.plot(x_values, green_values, label="Green", color='g')
ax.plot(x_values, blue_values, label="Blue", color='b')

ax.set_xlabel("Pixel Index")
ax.set_ylabel("Band Value")
ax.set_title("RGB Band Values Curve (Middle row of image)")
ax.legend()

# 将图表保存为图片并显示
st.pyplot(fig)

