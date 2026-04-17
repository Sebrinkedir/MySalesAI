from Agents.data_agent import DataAgent
from Agents.analysis_agent import AnalysisAgent
from Agents.insight_agent import InsightAgent

def main():
    print("MySalesAI starting...")

    data_agent = DataAgent()
    analysis_agent = AnalysisAgent()
    insight_agent = InsightAgent()

    data = data_agent.run()
    results = analysis_agent.run(data)
    insights = insight_agent.run(results)

    print("Final Insights:", insights)

if __name__ == "__main__":
    main()