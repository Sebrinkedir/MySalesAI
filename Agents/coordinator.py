import time
from Agents.data_agent import DataAgent
from Agents.analysis_agent import AnalysisAgent
from Agents.insight_agent import InsightAgent


class Coordinator:

    def __init__(self):
        self.data_agent = DataAgent()
        self.analysis_agent = AnalysisAgent()
        self.insight_agent = InsightAgent()

    def run(self, file_path, question):
        start_time = time.time()

        df = self.data_agent.load_data(file_path)

        analysis_results = self.analysis_agent.compute_all(df, question)

        insights = self.insight_agent.generate_insight(analysis_results, question)

        end_time = time.time()

        return {
            "mode": "multi_agent",
            "analysis": analysis_results,
            "insights": insights,
            "latency_seconds": round(end_time - start_time, 2)
        }
    