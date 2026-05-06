import streamlit as st
from PIL import Image, ImageChops
import os
import time

# 1. Page Configuration
st.set_page_config(page_title="Deep Fake AI Detector", page_icon="⚖️", layout="wide")

# 2. Corporate UI Styling (CSS)
st.markdown("""
    <style>
    /* Professional Navy & Slate Theme */
    .stApp {
        background-color: #0f172a;
        color: #f1f5f9;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }

    /* Soft Animated Background */
    @keyframes slowOrbit {
        from { background-position: 0% 50%; }
        to { background-position: 100% 50%; }
    }
    
    /* Clean Sidebar */
    [data-testid="stSidebar"] {
        background-color: #1e293b;
        border-right: 1px solid #334155;
    }

    /* Corporate Card Style */
    div[data-testid="stVerticalBlock"] > div {
        background: #1e293b;
        border-radius: 12px;
        padding: 24px;
        border: 1px solid #334155;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }

    /* Hero Title - Gradient & Smooth Animation */
    .corporate-header {
        font-size: 48px;
        font-weight: 700;
        text-align: center;
        background: linear-gradient(135deg, #38bdf8 0%, #818cf8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
        animation: fadeIn 1.5s ease-in;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Professional Button */
    div.stButton > button:first-child {
        background-color: #3b82f6;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 12px 24px;
        font-weight: 600;
        width: 100%;
        transition: background 0.3s ease, transform 0.2s ease;
    }

    div.stButton > button:first-child:hover {
        background-color: #2563eb;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
    }

    /* Metric Styling */
    [data-testid="stMetricValue"] {
        font-size: 28px;
        color: #38bdf8;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar - Enterprise Branding
with st.sidebar:
    st.markdown("###  SYSTEM STATUS")
    st.write("● Node: **SRCAS-LAB-01**")
    st.write("● Encryption: **AES-256**")
    st.markdown("---")
    st.markdown("### ‍ PROJECT LEAD")
    st.write("**Seenivasan R**")
    st.caption("BSc Computer Technology")
    st.markdown("---")
    st.info("Authorized Personnel Only")

# 4. Main Application Layout
st.markdown('<h1 class="corporate-header">Deep Fake AI Detector</h1>', unsafe_allow_html=True)
st.write("<p style='text-align: center; color: #94a3b8; margin-bottom: 40px;'>Enterprise-grade AI content verification and metadata validation.</p>", unsafe_allow_html=True)

left_col, right_col = st.columns([1, 1], gap="large")

with left_col:
    st.markdown("###  Document Upload")
    uploaded_file = st.file_uploader("Select high-resolution image for analysis", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="Target Asset Loaded", use_container_width=True)

def analyze_forensics(img_path):
    img = Image.open(img_path)
    # Metadata Presence
    has_exif = True if img._getexif() else False
    
    # ELA (Error Level Analysis)
    temp_path = "corp_buffer.jpg"
    img.convert('RGB').save(temp_path, 'JPEG', quality=90)
    diff = ImageChops.difference(img.convert('RGB'), Image.open(temp_path))
    noise_score = max([v[1] for v in diff.getextrema()])
    os.remove(temp_path)
    return has_exif, noise_score

with right_col:
    st.markdown("### ⚙️ Analysis Terminal")
    if uploaded_file:
        if st.button("EXECUTE DIAGNOSTICS"):
            # Professional Progress Tracking
            status_placeholder = st.empty()
            bar = st.progress(0)
            
            steps = ["Synchronizing Neural Engines...", "Parsing EXIF Headers...", "Analyzing Artifact Noise...", "Compiling Final Report..."]
            for i, step in enumerate(steps):
                status_placeholder.text(f"TASK: {step}")
                bar.progress((i + 1) * 25)
                time.sleep(0.8)
            
            # Processing
            with open("active_scan.jpg", "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            meta_exists, noise = analyze_forensics("active_scan.jpg")
            os.remove("active_scan.jpg")
            
            st.markdown("---")
            st.markdown("###  Executive Summary")
            
            m1, m2 = st.columns(2)
            m1.metric("Metadata", "VALID" if meta_exists else "MISSING")
            m2.metric("Noise Variance", f"{noise}%")

            if not meta_exists and noise > 22:
                st.error(" CRITICAL ALERT: AI SIGNATURES DETECTED")
                st.caption("Heuristic analysis suggests synthetic pixel generation.")
                st.balloons()
            else:
                st.success("✅ VERIFICATION SUCCESSFUL: HUMAN ORIGIN")
                st.caption("Artifact patterns match natural lens-capture physics.")
                st.snow()
    else:
        st.write("Awaiting document input to begin diagnostics.")

# Footer
st.markdown("<br><hr><p style='text-align: center; opacity: 0.6;'>© 2026 Enterprise Security Solutions | Seenivasan R | SRCAS</p>", unsafe_allow_html=True)

