from Agents.data_agent import DataAgent
from Agents.analysis_agent import AnalysisAgent
from Agents.insight_agent import InsightAgent

class Coordinator:

    def __init__(self):
        self.data_agent = DataAgent()
        self.analysis_agent = AnalysisAgent()
        self.insight_agent = InsightAgent()

    def run(self, file_path):

        df = self.data_agent.load_data(file_path)

        analysis_results = self.analysis_agent.compute_all(df)

        insights = self.insight_agent.generate_insight(analysis_results)

        return {
            "analysis": analysis_results,
            "insights": insights
        }
    