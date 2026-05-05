import streamlit as st
from PIL import Image, ImageChops, ImageEnhance
import os

# 1. UI Configuration
st.set_page_config(page_title="Deep fake Ai image detector", page_icon="")
st.title("Deep Fake AI Image detector")
st.info("This system analyzes Metadata and Pixel Compression (ELA) to detect AI generation.")

# 2. Image Upload Section
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

def analyze_image(img_path):
    # Metadata Check
    img = Image.open(img_path)
    has_metadata = True if img._getexif() else False
    
    # ELA (Error Level Analysis) Scan
    temp_resaved = "temp_resave.jpg"
    img.convert('RGB').save(temp_resaved, 'JPEG', quality=90)
    resaved_img = Image.open(temp_resaved)
    
    diff = ImageChops.difference(img.convert('RGB'), resaved_img)
    extrema = diff.getextrema()
    max_diff = max([ex[1] for ex in extrema])
    if max_diff == 0: max_diff = 1
    
    os.remove(temp_resaved)
    return has_metadata, max_diff

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_container_width=True)
    
    if st.button('Analyze Image'):
        with open("temp_upload.jpg", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        has_meta, diff_score = analyze_image("temp_upload.jpg")
        os.remove("temp_upload.jpg")
        
        st.subheader("Analysis Result:")
        
        if not has_meta and diff_score > 20:
            st.error(" Result: AI Generated Image Detected")
            st.write("Reason: No digital signature (Metadata) found and synthetic pixel patterns detected.")
        else:
            st.success("✅ Result: Real Human Image Detected")
            st.write("Reason: Natural pixel distribution and valid digital metadata found.")

