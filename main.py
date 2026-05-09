import streamlit as st
from PIL import Image, ImageOps
import numpy as np
import time

st.title("🖼️ AI vs Human Image Detector")

# --- UI ---
uploaded_file = st.file_uploader("Upload image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    if st.button("Check Accuracy"):
        with st.spinner('Deep scanning pixels...'):
            time.sleep(2) # Loading effect kaga
            
            # Simple Logic: Image size or random vachu oru result
            # Real project-la inga thaan model predict pannum
            result = "AI GENERATED (DEEPFAKE) ❌" if np.mean(image) > 120 else "REAL HUMAN ✅"
            
            if "REAL" in result:
                st.success(f"Result: {result}")
            else:
                st.error(f"Result: {result}")