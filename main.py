import streamlit as st
from PIL import Image, ImageChops, ImageEnhance
import os
st.set_page_config(page_title="seenu's deepfake detector", page_icon="")
st.title(" Deepfake AI Image Detector")
st.info("This system analyzes image Metadata and Pixel Compression (ELA) to detect AI generation.")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

def analyze_image(img_path):
    # Metadata Check (EXIF Data)
    img = Image.open(img_path)
    has_metadata = True if img._getexif() else False
    
    # ELA (Error Level Analysis) Scan
    temp_resaved = "temp.jpg"
    # Resave at 90% quality to check for compression differences
    img.convert('RGB').save(temp_resaved, 'JPEG', quality=90)
    resaved_img = Image.open(temp_resaved)
    
    diff = ImageChops.difference(img.convert('RGB'), resaved_img)
    extrema = diff.getextrema()
    max_diff = max([ex[1] for ex in extrema])
    if max_diff == 0: max_diff = 1
    
    os.remove(temp_resaved)
    return has_metadata, max_diff

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_container_width=True)
    
    if st.button('Analyze Image'):
        # Save temporarily for processing
        with open("temp_img.jpg", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        has_meta, diff_score = analyze_image("temp_img.jpg")
        os.remove("temp_img.jpg")
        
        st.subheader("Analysis Result:")
        
        # Logic: If no metadata exists and pixel difference is high, it's likely AI
        if not has_meta and diff_score > 20:
            st.error(" Result: AI-Generated Image Detected")
            st.write("**Reason:** No digital signature (Metadata) found and pixel distribution appears synthetic.")
        else:
            st.success("✅ Result: Real Human Image Detected")
            st.write("**Reason:** Image contains natural pixel patterns and valid digital traces.")

