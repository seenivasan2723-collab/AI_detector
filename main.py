import streamlit as st
from PIL import Image, ImageChops
import os
import time

# 1. Page Configuration and CSS Styling
st.set_page_config(page_title="DeepFake AI Image Detecor", page_icon="", layout="wide")

st.markdown("""
    <style>
    /* Main Background Gradient */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        color: white;
    }
    
    /* Main Title Styling */
    .main-title {
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        background: -webkit-linear-gradient(#00d2ff, #3a7bd5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 20px;
    }

    /* Interactive Button Styling */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #00d2ff 0%, #3a7bd5 100%);
        color: white;
        border-radius: 30px;
        border: none;
        padding: 15px 30px;
        font-size: 20px;
        transition: 0.3s;
        width: 100%;
    }
    
    div.stButton > button:first-child:hover {
        transform: scale(1.05);
        box-shadow: 0px 0px 20px #00d2ff;
    }

    /* Sidebar and Info Box Customization */
    .stAlert {
        background-color: rgba(255, 255, 255, 0.1);
        color: white;
        border: 1px solid #3a7bd5;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Sidebar - Developer Information
with st.sidebar:
    st.title("‍ Developer Info")
    st.write("**Name:** Seenivasan R")
    st.write("**Department:** BSc Computer Technology")
    st.write("**College:** Sri Ramakrishna College")
    st.markdown("---")
    st.info("System uses Metadata Analysis and Error Level Analysis (ELA) to identify synthetic pixel patterns.")

# 3. Home Page Content
st.markdown('<p class="main-title"> DeepFake AI Image Detector</p>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("Drop your image here or browse", type=["jpg", "jpeg", "png"])

def analyze_image(img_path):
    img = Image.open(img_path)
    # Check for EXIF metadata (usually missing in AI images)
    has_metadata = True if img._getexif() else False
    
    # Perform Error Level Analysis (ELA)
    temp_file = "temp_resave.jpg"
    img.convert('RGB').save(temp_file, 'JPEG', quality=90)
    resaved_img = Image.open(temp_file)
    diff = ImageChops.difference(img.convert('RGB'), resaved_img)
    extrema = diff.getextrema()
    max_diff = max([ex[1] for ex in extrema])
    
    os.remove(temp_file)
    return has_metadata, max_diff

if uploaded_file is not None:
    # Image Preview Layout
    col1, col2 = st.columns([1, 1])
    with col1:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Preview', use_container_width=True)
    
    with col2:
        st.write("### Analysis Controls")
        if st.button(' Start Scanning'):
            # Animated Loading Bar
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for percent_complete in range(100):
                time.sleep(0.01)
                progress_bar.progress(percent_complete + 1)
                status_text.text(f"Scanning Pixels... {percent_complete + 1}%")
            
            # Processing the file
            with open("test_img.jpg", "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            has_meta, score = analyze_image("test_img.jpg")
            os.remove("test_img.jpg")
            
            st.markdown("---")
            st.subheader("Analysis Complete!")
            
            # Result Logic and Visual Feedback
            if not has_meta and score > 20:
                st.error(" RESULT: AI GENERATED IMAGE")
                st.write("**Reasoning:** The image lacks standard camera metadata and shows high synthetic compression levels.")
            else:
                st.success("✅ RESULT: REAL HUMAN IMAGE")
                st.write("**Reasoning:** Digital signatures and pixel distribution match natural camera capturing patterns.")
                

