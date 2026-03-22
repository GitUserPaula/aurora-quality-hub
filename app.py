import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Page Configuration
st.set_page_config(page_title="Aurora Quality Hub", page_icon="🌌", layout="wide")

# Custom CSS for the "Aurora" look
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #0a0f1e;
        color: #b0bec5;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #16213e;
        border-right: 1px solid #1f3b6d;
    }

    /* Titles and headers */
    h1, h2, h3, [data-testid="stHeader"] {
        color: #00e5ff !important;
        font-family: 'Courier New', Courier, monospace; /* Toque tech */
        font-weight: 700;
    }

    /* Labels */
    .stSlider label, .stSelectbox label, .stTextInput label, .stTextArea label, .stRadio label {
        color: #ffffff;
    }

    /* Buttons */
    .stButton > button {
        width: 100%;
        border-radius: 8px;
        background: linear-gradient(45deg, #00e5ff, #7c4dff);
        color: #ffffff;
        font-weight: bold;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 229, 255, 0.3);
    }

    .stButton > button:hover {
        background: linear-gradient(45deg, #7c4dff, #00e5ff);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(124, 77, 255, 0.5);
    }

    /* Alerts (Success, Info, Warning) */
    .stAlert {
        border-radius: 8px;
        border: 1px solid #1f3b6d;
    }
    .stAlert[data-baseweb="alert"] {
        background-color: rgba(22, 33, 62, 0.7); /* Transparente */
    }
    
    /* Input Fields */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #1a274e;
        color: #ffffff;
        border: 1px solid #30477a;
    }

    </style>
    """, unsafe_allow_html=True)

# Sidebar for Navigation and Settings
with st.sidebar:
    st.title("🌌 Aurora Settings")
    
    # Priority: Env Variable > Manual Input
    env_key = os.getenv("GOOGLE_API_KEY")
    api_key = st.text_input("Gemini API Key", value=env_key if env_key else "", type="password", help="Get your key at Google AI Studio")
    
    st.divider()
    st.subheader("Select Module")
    module = st.radio(
        "Workflow:",
        ["Report Assistant", "Test Case Generator", "Risk Analysis"]
    )
    
    st.divider()
    st.caption("Developed by Pau | Quality Engineer")

# AI Logic Initialization
if api_key:
    client = genai.Client(api_key=api_key) 
else:
    st.warning("⚠️ Please provide a Gemini API Key in the sidebar.")

# --- HUB MODULES ---

if module == "Report Assistant" and api_key:
    st.header("📝 Report Assistant")
    st.write("Transform informal notes into professional-grade technical reports.")
    
    user_input = st.text_area("Describe the issue...", placeholder="e.g., The login button is unresponsive on Android 14.")
    
    if st.button("Generate Report"):
        if user_input and api_key:
            with st.spinner("Aurora is processing the bug..."):
                prompt = (
                    f"Act as a Senior QA Engineer. Convert the following description into a formal bug report in Markdown. "
                    f"Include: Title, Severity (Suggest one), Steps to Reproduce, Actual Result, and Expected Result. "
                    f"Input: {user_input}"
                )
                response = client.models.generate_content(
                model="models/gemini-2.5-flash", 
                contents=prompt
                )
                st.markdown("---")
                st.subheader("✨ Aurora's Draft")
                st.markdown(response.text)
        else:
            st.error("Missing description or API Key.")

elif module == "Test Case Generator" and api_key:
    st.header("🧪 Test Case Generator")
    st.write("Generate comprehensive test scenarios based on features or User Stories.")
    
    feature = st.text_area("Feature Description:", placeholder="e.g., Implementing a 2FA flow via SMS.", height=150)
    
    if st.button("Generate Test Suite"):
        if feature:
            with st.spinner("Designing test cases..."):
                
                prompt = (
                    f"As a Senior QA Expert, generate a structured list of test cases for the following feature. "
                    f"IMPORTANT: Use a clean Markdown table with only these columns: ID, Title, Type (Happy/Edge), and Expected Result. "
                    f"Keep descriptions concise to avoid formatting issues. "
                    f"Feature: {feature}"
                )
                
                response = client.models.generate_content(
                    model="models/gemini-2.5-flash", 
                    contents=prompt
                )
                
                st.markdown("---")
                st.subheader("✨ Aurora's Test Suite")
                
                with st.container():
                    st.markdown(response.text)
                
                st.download_button("📥 Download Test Suite", response.text, file_name="test_cases.md")
        else:
            st.error("Please describe the feature first.")

elif module == "Risk Analysis":
    st.header("⚖️ Risk Analysis")
    st.write("Identify potential quality risks before testing starts.")
    st.info("Module under development... Stay tuned! 🚀")