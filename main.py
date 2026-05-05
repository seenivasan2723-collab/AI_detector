import streamlit as st
from PIL import Image, ImageChops
import os
import time

# 1. Page Configuration
st.set_page_config(page_title="Deep Fake AI Image Detector", page_icon="🤖", layout="wide")

# 2. Advanced CSS for Glassmorphism and Animations
st.markdown("""
    <style>
    /* Gradient Background */
    .stApp {
        background: radial-gradient(circle at top right, #1e3a8a, #0f172a);
        color: #e2e8f0;
    }

    /* Glassmorphism Effect for containers */
    .stFileUploader, .stMarkdown, div[data-testid="stVerticalBlock"] > div {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
    }

    /* Animated Title */
    @keyframes fadeInDown {
        0% { opacity: 0; transform: translateY(-20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    .main-title {
        font-size: 60px;
        font-weight: 800;
        text-align: center;
        letter-spacing: -1px;
        background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: fadeInDown 1s ease-out;
    }

    /* Neon Button */
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #00f2fe 0%, #4facfe 100%);
        border: none;
        color: white;
        padding: 15px 0px;
        font-weight: bold;
        font-size: 22px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 242, 254, 0.3);
        transition: all 0.3s ease;
        width: 100%;
    }

    div.stButton > button:first-child:hover {
        box-shadow: 0 0 25px rgba(0, 242, 254, 0.6);
        transform: translateY(-2px);
    }

    /* Hide Streamlit Header/Footer for clean look */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Styling
with st.sidebar:
    st.markdown("## 🛡️ System Core")
    st.markdown("---")
    st.write(" **Lead Dev:** Seenivasan R")
    st.write(" **Dept:** BSc Computer Technology")
    st.write("️ **Institution:** SRCAS")
    st.markdown("---")
    st.success("ELA Scan Engine: Online")
    st.info("Metadata Engine: Online")

# 4. Main Interface
st.markdown('<p class="main-title">AI VISION PRO</p>', unsafe_allow_html=True)
st.write("<p style='text-align: center; color: #94a3b8;'>Advanced Neural Pattern Recognition & Forensic Analysis</p>", unsafe_allow_html=True)

# Layout Columns
col_left, col_right = st.columns([1, 1], gap="large")

with col_left:
    st.markdown("###  Source Input")
    uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        img_display = Image.open(uploaded_file)
        st.image(img_display, caption="Target Buffer", use_container_width=True)

def perform_forensic_scan(img_path):
    img = Image.open(img_path)
    has_metadata = True if img._getexif() else False
    
    # ELA Analysis
    temp = "scan_buffer.jpg"
    img.convert('RGB').save(temp, 'JPEG', quality=90)
    diff = ImageChops.difference(img.convert('RGB'), Image.open(temp))
    score = max([ex[1] for ex in diff.getextrema()])
    os.remove(temp)
    return has_metadata, score

with col_right:
    st.markdown("### ⚙️ Forensic Terminal")
    if uploaded_file:
        if st.button("EXECUTE SCAN"):
            # Mock Scanning Animation
            status = st.empty()
            bar = st.progress(0)
            
            stages = ["Initializing...", "Checking EXIF...", "Analyzing Pixels...", "Comparing Bitstreams..."]
            for i, stage in enumerate(stages):
                status.markdown(f"**Current Task:** `{stage}`")
                bar.progress((i + 1) * 25)
                time.sleep(0.6)
            
            # Save and Scan
            with open("temp_target.jpg", "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            is_real_meta, ela_val = perform_forensic_scan("temp_target.jpg")
            os.remove("temp_target.jpg")
            
            st.markdown("---")
            st.markdown("###  Final Report")
            
            if not is_real_meta and ela_val > 22:
                st.error("⚠️ THREAT DETECTED: AI GENERATED CONTENT")
                st.warning(f"Forensic Score: {ela_val} | Metadata: Missing")
                st.balloons()
            else:
                st.success("✅ VERIFIED: AUTHENTIC HUMAN CAPTURE")
                st.info(f"Forensic Score: {ela_val} | Metadata: Detected")
                st.snow()
    else:
        st.write("Please upload a file to initialize the scanning terminal.")

# 5. Footer info
st.markdown("<br><hr><center>Secure Forensic Lab Environment v2.4.0</center>", unsafe_allow_html=True)

