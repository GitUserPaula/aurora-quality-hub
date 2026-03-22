import streamlit as st
import json
from google import genai
import os

def display(client):
    st.title("🔮 JSON Lens")
    st.write("Structural Auditor & Impact Analysis")

    api_key = os.getenv("GOOGLE_API_KEY")
    client = genai.Client(api_key=api_key)

    col1, col2 = st.columns(2)
    with col1:
        json_a = st.text_area("Current JSON (Contract/Old):", height=300)
    with col2:
        json_b = st.text_area("Revised JSON (Payload/New):", height=300)

    if st.button("🚀 Run Deep Audit"):
        if json_a and json_b:
            with st.spinner("Analyzing data integrity..."):
                prompt = (
                    f"As a Senior Data QA, compare these JSONs. Focus on: "
                    f"1. Breaking changes (removed keys, type mismatches). "
                    f"2. New fields. 3. Risk assessment for automation scripts. "
                    f"JSON A: {json_a} | JSON B: {json_b}"
                )
                response = client.models.generate_content(
                    model="models/gemini-2.5-flash", contents=prompt
                )
                st.info(response.text)
        else:
            st.warning("Please provide both JSON structures")