# MySalesAI

## Adaptive Multi-Agent Business Intelligence System

MySalesAI is an adaptive Multi-Agent AI system designed for real-world business intelligence and sales analytics.  
The system combines deterministic KPI computation, Large Language Models (LLMs), dynamic schema intelligence, and explainable reasoning to generate grounded business insights from heterogeneous business datasets.

The project compares:
- Multi-Agent Architecture
vs
- Single-Agent Baseline

using:
- Accuracy
- Latency
- Hallucination Reduction
- Explainability

---

# Project Objectives

The project aims to:
- Analyze real-world business datasets
- Adapt dynamically to different schemas
- Generate grounded business insights
- Reduce hallucinated explanations
- Benchmark multi-agent vs single-agent reasoning
- Provide explainable AI-driven business analytics

---

# Key Features

## Adaptive Dataset Intelligence
The system automatically adapts to multiple real-world business datasets through:
- Dynamic schema mapping
- Dataset profiling
- Automatic column role detection
- Flexible business entity recognition

Supported business concepts include:
- Revenue / Sales / Weekly_Sales
- Product / Store / Category / Region
- Date / Order_Date / Invoice_Date

---

## Multi-Agent Architecture

The system uses specialized agents:

### Data Agent
- Loads CSV and Excel files
- Validates datasets
- Standardizes schemas

### Dataset Profiler Agent
- Detects:
  - Date columns
  - Numeric metrics
  - Business dimensions
  - Revenue columns
  - Business entities

### Analysis Agent
Performs deterministic KPI computation:
- Total Revenue
- Monthly Trends
- Percentage Changes
- Best/Worst Month
- Revenue Contribution
- Trend Direction
- Executive KPI Summaries

### Insight Agent
Generates:
- Evidence-grounded insights
- Executive summaries
- Strategic interpretations
- Missing evidence disclosure

### Evaluation Layer
Benchmarks:
- Accuracy
- Hallucination Count
- Latency
- Question-aware reasoning

---

# System Workflow

```text
User Dataset
      ↓
Data Agent
      ↓
Dataset Profiler
      ↓
Schema Standardization
      ↓
Analysis Agent
      ↓
Insight Agent
      ↓
Evaluation Framework
      ↓
Dashboard + PDF Reports