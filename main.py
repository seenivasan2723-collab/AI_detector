import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

# --- PAGE SETUP ---
st.set_page_config(page_title="Deepfake Image Detector", page_icon="🖼️")
st.title("🖼️ Deepfake vs Human Image Detector")
st.write("Upload an image to check if it's **AI Generated** or **Real Human**.")

# --- LOAD MODEL ---
# Note: Real project-la nee train panna .h5 file-a inga load pannanum.
# Ippo logic-kaga oru mock function vachipom.
def predict_image(img):
    # Image-a model-ku yetha maari resize pannanum
    size = (224, 224)
    image = ImageOps.fit(img, size, Image.LANCZOS)
    image_array = np.asarray(image)
    
    # Inga thaan unga Deep Learning model prediction nadakum
    # Simple logic for Demo:
    # prediction = model.predict(image_array)
    
    # Mock result (Demo-kaga)
    import random
    return random.choice(["REAL HUMAN ✅", "AI GENERATED (DEEPFAKE) ❌"])

# --- UI ---
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    if st.button("Analyze Image"):
        with st.spinner('Analyzing pixels...'):
            result = predict_image(image)
            
            if "REAL" in result:
                st.success(f"Result: {result}")
            else:
                st.error(f"Result: {result}")

st.sidebar.warning("Note: This is a Computer Vision model that analyzes image patterns, not text.")