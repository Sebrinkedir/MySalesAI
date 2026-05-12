# MySalesAI
A Multi-Agent LLM System for Automated Sales Data Analysis

---

## Project Overview

MySalesAI is a research-focused AI analytics system designed to compare:

- Single-Agent LLM systems
vs
- Multi-Agent LLM architectures

for automated sales data analysis.

The system accepts CSV sales data and natural-language business questions, then generates analytical insights using GPT-powered agents.

---

## Research Question

Does a role-separated multi-agent architecture produce more accurate, reliable, and user-interpretable sales insights than a single-agent approach, and at what cost in latency or complexity?

---

## System Architecture

### Multi-Agent System

The system contains four specialized agents:

1. Data Agent
   - Loads and validates CSV/Excel files

2. Analysis Agent
   - Computes KPIs, trends, and revenue changes

3. Insight Agent
   - Uses OpenAI GPT models to generate grounded business insights

4. Coordinator Agent
   - Orchestrates communication between all agents

---

## Single-Agent Baseline

A baseline architecture is also implemented where one agent handles:
- data loading
- analysis
- reasoning
- explanation

This enables experimental comparison between:
- modular multi-agent reasoning
- monolithic single-agent reasoning

---

## Features Implemented

- CSV sales data ingestion
- Natural-language business questions
- GPT-powered insight generation
- Dynamic question-aware analysis routing
- Monthly trend analysis
- Revenue change detection
- Latency tracking
- Automated evaluation pipeline
- Numerical accuracy scoring
- Hallucination detection
- Evaluation summaries
- Streamlit web UI
- Single-Agent baseline
- Multi-Agent architecture

---

## Evaluation Metrics

The system currently evaluates:

- Numerical Accuracy
- Latency
- Hallucination Count
- Trend Detection Reliability

---

## Automated Evaluation

The project includes:
- `evaluation.py`
- `results_summary.py`

These scripts automatically:
- run benchmark questions
- compare architectures
- calculate metrics
- generate evaluation summaries

---

## Streamlit UI

The project includes a Streamlit-based UI for:
- CSV upload
- natural-language question input
- architecture selection
- insight visualization

Run the UI using:

```bash
python -m streamlit run streamlit_app.py