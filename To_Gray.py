# Note: This script runs only on a local IDE with "streamlit run main.py"
import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")

with st.expander("Take a selfie"):

    img_photo = st.camera_input("Take photo")
    if img_photo:
        uploaded = Image.open(img_photo)
        to_gray = uploaded.convert("L")
        st.image(to_gray)


with st.expander("Upload your photo"):
    img_file = st.file_uploader("Browse files")
    if img_file:
        uploaded1 = Image.open(img_file)
        to_gray1 = uploaded1.convert("L")
        st.image(to_gray1)
