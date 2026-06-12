# MySalesAI

## Adaptive Multi-Format Business Intelligence System

MySalesAI is an adaptive multi-agent business intelligence platform designed to analyze real-world business datasets across multiple file formats. The system automatically profiles datasets, detects schemas dynamically, generates business insights, visualizes trends, evaluates reasoning quality, and produces explainable reports.

The project compares a Multi-Agent architecture against a Single-Agent baseline using evaluation metrics such as accuracy, latency, and hallucination count.

---

# Features

* Multi-Agent Business Intelligence Architecture
* Single-Agent Baseline Comparison
* Adaptive Dataset Profiling
* Automatic Schema Detection
* Revenue Trend Analysis
* Executive Summary Generation
* Explainable AI Insights
* Hallucination Detection Framework
* Automated Evaluation Pipeline
* Streamlit Interactive Dashboard
* PDF Report Generation
* Revenue Trend Visualization

---

# Supported File Types

The system supports multiple structured business dataset formats:

* CSV (.csv)
* Excel (.xlsx)
* SQLite Databases (.db, .sqlite)
* Word Documents (.docx)
* PDF Business Reports with Structured Tables (.pdf)

---

# Supported Business Analytics

The platform automatically performs:

* Revenue Analysis
* Monthly Trend Analysis
* Entity Contribution Analysis
* Best/Worst Period Detection
* Percentage Change Analysis
* Executive Summary Generation
* Evidence-Based Insights
* KPI Summarization

---

# System Architecture

The project contains:

## Multi-Agent System

The Multi-Agent pipeline consists of:

* DataAgent
* AnalysisAgent
* InsightAgent
* VerificationAgent
* Coordinator

Each agent performs a specialized task in the business intelligence workflow.

## Single-Agent Baseline

A simplified baseline system used for comparative evaluation.

---

# Adaptive Intelligence Features

The system includes:

* Automatic Column Mapping
* Dynamic Revenue Column Detection
* Intelligent SQLite Table Selection
* Structured PDF Table Extraction
* Word Table Extraction
* Flexible Business Schema Adaptation
* Real-World Dataset Compatibility

---

# Dashboard Features

The Streamlit dashboard provides:

* File Upload Interface
* Multi-Agent vs Single-Agent Selection
* Interactive Revenue Charts
* Evaluation Dashboard
* Downloadable PDF Reports
* Business Insights Visualization

---

# Evaluation Metrics

The evaluation framework measures:

* Accuracy
* Latency
* Hallucination Count
* Comparative System Performance

---

# Project Structure

```bash
MySalesAI/
│
├── Agents/
│   ├── analysis_agent.py
│   ├── coordinator.py
│   ├── data_agent.py
│   ├── dataset_profiler.py
│   ├── insight_agent.py
│   ├── single_agent.py
│   └── verification_agent.py
│
├── charts/
├── data/
├── logs/
├── reports/
│
├── app.py
├── evaluation.py
├── streamlit_app.py
├── report_generator.py
├── chart_generator.py
└── requirements.txt
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Sebrinkedir/MySalesAI.git
cd MySalesAI
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the CLI System

```bash
python app.py
```

---

# Running the Streamlit Dashboard

```bash
python -m streamlit run streamlit_app.py
```

---

# Example Questions

```text
Provide an executive summary of business performance.
```

```text
What business dimensions and metrics are available in this dataset?
```

```text
Which business entity contributed most to revenue?
```

```text
What are the major revenue trends?
```

```text
What additional evidence would improve the analysis?
```

---

# Example Datasets

Recommended datasets for testing:

* Superstore Sales Dataset
* Walmart Sales Dataset
* Supermarket Sales Dataset
* Chinook SQLite Database
* Invoice PDF Datasets
* Business Sales Report PDFs

---

# Research Contribution

This project demonstrates:

* Adaptive multi-format business intelligence
* Multi-agent reasoning for enterprise analytics
* Explainable business insight generation
* Hallucination-aware analytics pipelines
* Automated business dataset understanding

---

# Future Improvements

Potential future enhancements include:

* OCR for scanned PDFs
* NLP-based financial report understanding
* SQL query generation
* Forecasting and predictive analytics
* LLM-powered conversational querying
* Real-time dashboard streaming
* Cloud deployment support

---


---

# License

This project is intended for academic and research purposes.
