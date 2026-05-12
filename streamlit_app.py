import streamlit as st
import pandas as pd
import tempfile

from Agents.coordinator import Coordinator
from Agents.single_agent import SingleAgent


st.set_page_config(page_title="MySalesAI", layout="wide")

st.title("📊 MySalesAI")
st.subheader("Multi-Agent Sales Analysis System")


uploaded_file = st.file_uploader(
    "Upload Sales CSV File",
    type=["csv"]
)

question = st.text_input(
    "Ask a business question",
    placeholder="Why did revenue decrease in March?"
)

mode = st.radio(
    "Choose System Mode",
    ["Multi-Agent", "Single-Agent"]
)


if st.button("Run Analysis"):

    if uploaded_file is None:
        st.warning("Please upload a CSV file.")
    
    elif question.strip() == "":
        st.warning("Please enter a question.")

    else:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp_file:
            tmp_file.write(uploaded_file.read())
            temp_path = tmp_file.name

        if mode == "Multi-Agent":
            system = Coordinator()
        else:
            system = SingleAgent()

        result = system.run(temp_path, question)

        st.success("Analysis completed.")

        st.subheader("Analysis Results")
        st.json(result["analysis"])

        st.subheader("Generated Insights")
        st.write(result["insights"])

        if "latency_seconds" in result:
            st.subheader("Latency")
            st.write(f"{result['latency_seconds']} seconds")
            