import os
import time

from dotenv import load_dotenv
from openai import OpenAI

from Agents.data_agent import DataAgent
from Agents.analysis_agent import AnalysisAgent


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class SingleAgent:

    def run(self, file_path, question):

        start_time = time.time()

        data_agent = DataAgent()
        analysis_agent = AnalysisAgent()

        df = data_agent.load_data(file_path)

        analysis_results = analysis_agent.compute_all(df, question)

        prompt = f"""
You are a business analytics assistant.

The user asked:
"{question}"

Verified business metrics:
{analysis_results}

Rules:
- Use ONLY the verified metrics above
- Do not invent unsupported claims
- If information is missing, clearly state limitations
- Provide professional business insights
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a business intelligence assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3
        )

        end_time = time.time()

        return {
            "mode": "single_agent",
            "analysis": analysis_results,
            "insights": response.choices[0].message.content,
            "latency_seconds": round(end_time - start_time, 2)
        }