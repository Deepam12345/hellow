import streamlit as st
from pdf_reader import extract_text
from summerizer import summarize_report
from extractor import extract_information

st.set_page_config(
    page_title="AI Medical Report Summarizer",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 AI Medical Report Summarizer")

st.write("Upload a medical report and generate an AI-powered summary.")

uploaded_file = st.file_uploader(
    "Upload Medical Report",
    type=["pdf"]
)

if uploaded_file:

    with st.spinner("Reading Report..."):
        text = extract_text(uploaded_file)

    st.success("Report Uploaded")

    with st.expander("Original Report"):
        st.write(text)

    if st.button("Generate Summary"):

        summary = summarize_report(text)

        st.subheader("Patient Summary")

        st.success(summary)

        data = extract_information(text)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Diagnosis")
            st.write(data["diagnosis"])

        with col2:
            st.subheader("Medicines")
            st.write(data["medicines"])

        st.subheader("Lab Results")

        st.write(data["lab_results"])

