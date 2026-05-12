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

1. **Data Agent**
   - Loads and validates CSV/Excel files

2. **Analysis Agent**
   - Computes KPIs, trends, and revenue changes

3. **Insight Agent**
   - Uses OpenAI GPT models to generate business insights

4. **Coordinator Agent**
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
- Evaluation logging
- Single-Agent baseline
- Multi-Agent architecture

---

## Example Questions

- Why did revenue decrease in March?
- Which product performed best?
- What is the monthly revenue trend?
- Did sales improve over time?

---

## Technologies Used

- Python
- OpenAI API
- Pandas
- Git/GitHub

---

## Evaluation Metrics

The project evaluates:

- Numerical accuracy
- Trend detection
- Hallucination rate
- Latency
- User interpretability

---

## Project Status

Current Progress:
- Multi-Agent system operational
- Single-Agent baseline operational
- Dynamic routing implemented
- Evaluation logging implemented

Next Steps:
- Hallucination evaluation
- Streamlit UI
- PDF report generation
- Automated experiments
- User testing

---

## Setup Instructions

### Install dependencies

```bash
pip install pandas openai python-dotenv
