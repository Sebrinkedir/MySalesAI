# MySalesAI

## Functional Requirements

1. Upload CSV/Excel file
2. Ask a question (e.g. "Why did revenue drop?")
3. System analyzes data
4. System gives insights
5. System shows charts
6. Support single-agent and multi-agent modes

## Non-Functional Requirements

- Should be accurate
- Should be easy to use
- Should not crash on bad data
- Should give clear explanations

## Architecture

The system has two versions:

1. Single-Agent:
One AI does everything (data + analysis + explanation)

2. Multi-Agent:
- Data Agent → loads and cleans data
- Analysis Agent → calculates results
- Insight Agent → explains results
- Coordinator → connects everything

This separation helps reduce errors and improve clarity.

## Current Progress (April 17)

- Requirements finalized
- Architecture defined and diagram created
- Project structure initialized
- Multi-agent skeleton implemented
- Basic system flow running

Next: Implement data processing and UI