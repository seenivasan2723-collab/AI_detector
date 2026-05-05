import streamlit as st
from PIL import Image, ImageChops
import os

# 1. UI Configuration
st.set_page_config(page_title="AI Detector")
st.title(" deepfake ai image detector")

# 2. Image Upload
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

def analyze_image(img_path):
    img = Image.open(img_path)
    # Check for Metadata
    has_metadata = True if img._getexif() else False
    
    # ELA Scan
    temp_file = "temp_resave.jpg"
    img.convert('RGB').save(temp_file, 'JPEG', quality=90)
    resaved_img = Image.open(temp_file)
    
    diff = ImageChops.difference(img.convert('RGB'), resaved_img)
    extrema = diff.getextrema()
    max_diff = max([ex[1] for ex in extrema])
    
    os.remove(temp_file)
    return has_metadata, max_diff

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, use_container_width=True)
    
    if st.button('Analyze Now'):
        with open("test_img.jpg", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        has_meta, score = analyze_image("test_img.jpg")
        os.remove("test_img.jpg")
        
        if not has_meta and score > 20:
            st.error(" Result: AI Generated Image")
        else:
            st.success("✅ Result: Real Human Image")

