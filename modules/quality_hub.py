import streamlit as st
from google import genai
import os

def display(client):

    st.title("🧪 Quality Hub")
    st.write("Streamline your QA workflow with AI-powered reporting and test design")

    api_key = os.getenv("GOOGLE_API_KEY")
    client = genai.Client(api_key=api_key)

    module = st.selectbox("Choose a tool:", ["Report Assistant", "Test Case Generator"])

    if module == "Report Assistant":
        st.subheader("📝 Report Assistant")
        user_input = st.text_area("Paste your messy notes here:", height=150)
        
        if st.button("Generate Professional Report"):
            if user_input:
                with st.spinner("Aurora is processing the bug report..."):
                    prompt = (
                    f"Act as a Senior QA Engineer. Convert the following description into a formal bug report in Markdown. "
                    f"Include: Title, Severity (Suggest one), Steps to Reproduce, Actual Result, and Expected Result. "
                    f"Input: {user_input}"
                    )
                    response = client.models.generate_content(model="models/gemini-2.5-flash", contents=prompt)
                    st.markdown("---")
                    st.subheader("✨ Aurora's Draft")
                    st.markdown(response.text)
            else:
                st.warning("Please enter some notes first")


    elif module == "Test Case Generator":
        st.subheader("💻 Test Case Generator")
        feature = st.text_area("Feature Description:", height=150)
        
        if st.button("Generate Test Suite"):
            if feature:
                with st.spinner("Designing scenarios..."):
                    
                    prompt = (
                    f"As a Senior QA Expert, generate a structured list of test cases for the following feature. "
                    f"IMPORTANT: Use a clean Markdown table with only these columns: ID, Title, Description,Type (Happy/Edge), Test Steps, Preconditions and Expected Result. "
                    f"Keep descriptions concise to avoid formatting issues. "
                    f"Feature: {feature}"
                    )
                    response = client.models.generate_content(model="models/gemini-2.5-flash", contents=prompt)
                    st.markdown("---")
                    st.subheader("✨ Aurora's Test Suite")
                    st.markdown(response.text)

                    with st.container():
                        st.markdown(response.text)
                        st.download_button("📥 Download Test Suite", response.text, file_name="test_cases.md")
            else:
                st.warning("Please describe the feature first")