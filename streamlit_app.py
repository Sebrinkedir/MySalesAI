import os
import streamlit as st
import pandas as pd
import tempfile

from Agents.coordinator import Coordinator
from Agents.single_agent import SingleAgent
from chart_generator import generate_revenue_chart
from report_generator import generate_pdf_report


st.set_page_config(page_title="MySalesAI", layout="wide")

st.title("📊 MySalesAI")
st.subheader("Multi-Agent LLM System for Sales Data Analysis")

tab1, tab2 = st.tabs(["Sales Analysis", "Evaluation Dashboard"])


with tab1:
    uploaded_file = st.file_uploader(
        "Upload Sales File",
        type=["csv", "xlsx"]
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
            st.warning("Please upload a CSV or Excel file.")

        elif question.strip() == "":
            st.warning("Please enter a question.")

        else:
            try:
                suffix = ".xlsx" if uploaded_file.name.endswith(".xlsx") else ".csv"

                with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
                    tmp_file.write(uploaded_file.read())
                    temp_path = tmp_file.name

                if mode == "Multi-Agent":
                    system = Coordinator()
                else:
                    system = SingleAgent()

                result = system.run(temp_path, question)

                st.success("Analysis completed.")

                st.subheader("Key Metrics")

                col1, col2, col3 = st.columns(3)

                analysis = result["analysis"]

                with col1:
                    if "total_revenue" in analysis:
                        st.metric("Total Revenue", analysis["total_revenue"])

                with col2:
                    if "top_product" in analysis:
                        st.metric("Top Product", analysis["top_product"])

                with col3:
                    if "latency_seconds" in result:
                        st.metric("Latency", f"{result['latency_seconds']} sec")

                st.subheader("Analysis Results")
                st.json(analysis)

                chart_path = None

                if "monthly_trend" in analysis:
                    chart_path = generate_revenue_chart(analysis["monthly_trend"])

                    st.subheader("Revenue Trend Chart")
                    st.image(chart_path)

                st.subheader("Generated Insights")
                st.write(result["insights"])

                pdf_path = generate_pdf_report(
                    mode=mode,
                    question=question,
                    analysis=analysis,
                    insights=result["insights"],
                    latency=result.get("latency_seconds", None),
                    chart_path=chart_path
                )

                with open(pdf_path, "rb") as pdf_file:
                    st.download_button(
                        label="Download PDF Report",
                        data=pdf_file,
                        file_name=os.path.basename(pdf_path),
                        mime="application/pdf"
                    )

            except Exception as e:
                st.error(f"Error: {e}")


with tab2:
    st.header("Research Evaluation Dashboard")

    evaluation_path = "logs/automated_evaluation.csv"

    if not os.path.exists(evaluation_path):
        st.warning("No evaluation results found. Run evaluation.py first.")

    else:
        df = pd.read_csv(evaluation_path)

        st.subheader("Evaluation Summary")

        summary = df.groupby("mode").agg({
            "latency_seconds": "mean",
            "accuracy_percent": "mean",
            "hallucination_count": "mean"
        }).reset_index()

        st.dataframe(summary)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("Average Latency")
            st.bar_chart(summary.set_index("mode")["latency_seconds"])

        with col2:
            st.subheader("Average Accuracy")
            st.bar_chart(summary.set_index("mode")["accuracy_percent"])

        with col3:
            st.subheader("Average Hallucination Count")
            st.bar_chart(summary.set_index("mode")["hallucination_count"])

        st.subheader("Raw Evaluation Results")
        st.dataframe(df) 