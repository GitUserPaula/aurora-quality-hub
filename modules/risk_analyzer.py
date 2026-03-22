import streamlit as st
from google import genai
import os

def display(client):
    st.title("🛡️ Risk Analyzer")
    st.write("Strategic assessment of technical and functional project risks")

    api_key = os.getenv("GOOGLE_API_KEY")
    client = genai.Client(api_key=api_key)

    project_context = st.text_area(
        "Describe the Feature or Change:", 
        placeholder="E.g.: NodeJS Library update...",
        height=150
    )

    if st.button("🚀 Analyze Risks"):
        if project_context:
            with st.spinner("Calculating risk variables..."):
                prompt = (
                    f"As a Senior QA Manager, analyze the risks for this project: {project_context}. "
                    f"Provide: 1. Technical Risks. 2. Business Impact. "
                    f"3. Mitigation Strategies. 4. Suggested Regression Areas. "
                    f"Format the output with professional headers."
                )
                response = client.models.generate_content(
                    model="models/gemini-2.5-flash", contents=prompt
                )
                st.markdown("---")
                st.subheader("⚠️ Risk Assessment Report")
                st.markdown(response.text)
        else:
            st.warning("Please provide context to analyze")