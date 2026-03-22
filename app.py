import streamlit as st
from modules import quality_hub, json_lens, risk_analyzer
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

def main():
    # Branding & THEME
    st.set_page_config(page_title="Aurora Suite", page_icon="🌌", layout="wide")
    st.sidebar.markdown("---")
    st.markdown("""
        <style>
                
        /* Background */
        .stApp {
            background-color: #0a0f1e;
            color: #b0bec5;
        }

        /* Sidebar */
        [data-testid="stSidebarNav"] + div h1, 
        .st-emotion-cache-10o480m h1, 
        section[data-testid="stSidebar"] h1 {
            font-size: 2.2rem !important; 
            margin-bottom: 0.5rem;
        }

        /* Divider */
        section[data-testid="stSidebar"] hr {
            border: 1px solid #30477a;
            margin-top: 0.5rem;
            margin-bottom: 1.5rem;
        }

                
        [data-testid="stSidebar"] {
        background-color: #16213e;
        border-right: 1px solid #1f3b6d;
        }
                
        [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
            font-size: 1.2rem !important;
            padding: 10px 0px;
        }
 
        /* Titles and headers */
        h2, h3, [data-testid="stHeader"] {
            color: #00e5ff !important;
            font-family: 'Courier New', Courier, monospace;
            font-weight: 700;
        }
        h1, [data-testid="stHeader"] {
            color: #9966ff !important;
            font-family: 'Courier New', Courier, monospace;
            font-weight: 700;
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
        }

        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 229, 255, 0.4);
        }
        
        /* Inputs y TextAreas */
        .stTextInput>div>div>input, .stTextArea>div>div>textarea {
            background-color: #1a274e;
            color: #ffffff;
            border: 1px solid #30477a;
        }
        /* Labels */        
        [data-testid="stWidgetLabel"] p {
            font-size: 1.4rem !important;
            color: #00e5ff !important;
            font-weight: bold !important;
        }
        
    /* Markdown tables */
        .stMarkdown table {
        width: 100%;
        color: #ffffff;
    }
                
        </style>
        """, unsafe_allow_html=True)

    # Sidebar Navigation
    st.sidebar.title("🌌 Aurora Suite")
    st.sidebar.markdown("---")
    
    selection = st.sidebar.radio(
        "**Go to Satellite:**", 
        ["🛰️ Center Command", "🧪 Quality Hub", "🔮 JSON Lens", "🛡️ Risk Analyzer"]
    )

    st.sidebar.markdown("*Developed with 💙 by Pau | Quality Engineer*")

    # MODULES
    if selection == "🛰️ Center Command":
        render_home()
    elif selection == "🧪 Quality Hub":
        quality_hub.display(client)
    elif selection == "🔮 JSON Lens":
        json_lens.display(client)
    elif selection == "🛡️ Risk Analyzer":
        risk_analyzer.display(client)

def render_home():
    st.title("🛰️ Center Command")
    st.markdown("---")
    st.markdown(f"### Welcome back, **Pau**! 👩‍🚀")
    st.write("""
        All Aurora systems are operational ✨📡 This is your mission control for 
        high-precision software quality engineering 🕵️‍♀️
    """)
    
    # "Status Report"
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("API Status", "Connected", "Active")
    col2.metric("Aurora Hub", "v2.5", "Up to date")
    col3.metric("JSON Lens", "Beta", "Stable")
    col4.metric("Risk Analyzer", "New", "Release 1.0", delta_color="normal")

if __name__ == "__main__":
    main()