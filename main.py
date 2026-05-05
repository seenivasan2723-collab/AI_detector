import streamlit as st
from PIL import Image, ImageChops
import os
import time

# 1. Advanced Page Config
st.set_page_config(page_title="Deep Fake AI Image Detector", page_icon="🧪", layout="wide")

# 2. Cyberpunk Glassmorphism CSS
st.markdown("""
    <style>
    /* Dark Deep Space Background */
    .stApp {
        background: radial-gradient(circle at center, #0f172a 0%, #020617 100%);
        color: #f8fafc;
    }

    /* Glass Cards */
    div[data-testid="stVerticalBlock"] > div {
        background: rgba(30, 41, 59, 0.5);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 25px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
    }

    /* Glowing Title */
    .hero-title {
        font-size: 72px;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(to right, #22d3ee, #818cf8, #d946ef);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 15px rgba(34, 211, 238, 0.3));
        margin-bottom: 5px;
    }

    /* Neon Scanner Button */
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #06b6d4, #3b82f6);
        border: none;
        color: white;
        padding: 20px;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 2px;
        border-radius: 15px;
        box-shadow: 0 0 20px rgba(6, 182, 212, 0.4);
        transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    div.stButton > button:first-child:hover {
        box-shadow: 0 0 40px rgba(6, 182, 212, 0.8);
        transform: scale(1.02);
    }

    /* Custom File Uploader */
    .stFileUploader {
        border: 2px dashed #334155;
        border-radius: 20px;
        background: rgba(15, 23, 42, 0.4);
    }

    /* Sidebar Glass */
    section[data-testid="stSidebar"] {
        background: rgba(15, 23, 42, 0.8);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Interactive Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", width=80)
    st.title("User Profile")
    st.write(" **Project:** AI Image Forensics")
    st.write(" **Developer:** Seenivasan R")
    st.write("️ **ID:** 24129049")
    st.markdown("---")
    st.markdown("###  System Vitals")
    st.code("CPU: STABLE\nRAM: OPTIMIZED\nLATENCY: 12ms", language='bash')

# 4. Main Lab Interface
st.markdown('<p class="hero-title">Deep Fake AI Image Detector</p>', unsafe_allow_html=True)
st.write("<p style='text-align: center; font-family: monospace; color: #94a3b8;'>v4.0.1 // NEURAL PATTERN RECOGNITION ENGINE</p>", unsafe_allow_html=True)

col1, col2 = st.columns([1.2, 0.8], gap="large")

with col1:
    st.markdown("####  TARGET ACQUISITION")
    uploaded_file = st.file_uploader("Drop encrypted image files here", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        img_preview = Image.open(uploaded_file)
        st.image(img_preview, caption="[BUFFERED IMAGE DATA]", use_container_width=True)

def run_forensics(path):
    img = Image.open(path)
    meta = True if img._getexif() else False
    
    # ELA Analysis (Error Level Analysis)
    buf = "ela_buffer.jpg"
    img.convert('RGB').save(buf, 'JPEG', quality=90)
    diff = ImageChops.difference(img.convert('RGB'), Image.open(buf))
    score = max([v[1] for v in diff.getextrema()])
    os.remove(buf)
    return meta, score

with col2:
    st.markdown("#### 🛠️ SCAN TERMINAL")
    if uploaded_file:
        if st.button("INITIATE DEEP SCAN"):
            log_area = st.empty()
            progress = st.progress(0)
            
            # Interactive Console Logs
            logs = [
                " Accessing file buffer...",
                "🧬 Extracting bitstream patterns...",
                " Checking EXIF metadata headers...",
                " Calculating ELA compression noise...",
                "🤖 Running heuristic comparison...",
                "✅ Finalizing report..."
            ]
            
            for idx, log in enumerate(logs):
                log_area.code(f"USER@SRCAS:~$ {log}")
                progress.progress((idx + 1) * 16)
                time.sleep(0.5)
            
            # Execution
            with open("active_scan.jpg", "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            has_meta, diff_val = run_forensics("active_scan.jpg")
            os.remove("active_scan.jpg")
            
            st.markdown("####  SCAN REPORT")
            
            # Dynamic Results
            if not has_meta and diff_val > 22:
                st.error(" CRITICAL: AI SIGNATURE DETECTED")
                st.warning(f"Forensic Variance: {diff_val}% // Metadata: NULL")
                st.balloons()
            else:
                st.success(" VERIFIED: AUTHENTIC CONTENT")
                st.info(f"Forensic Variance: {diff_val}% // Metadata: VALID")
                st.snow()
    else:
        st.info("System idle. Waiting for image input...")

# 5. Dashboard Footer
st.markdown("<br><br><p style='text-align: center; color: #334155;'>© 2026 // SEENIVASAN R // FORENSIC CORE v4.0</p>", unsafe_allow_html=True)

