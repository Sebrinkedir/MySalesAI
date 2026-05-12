import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class InsightAgent:
    """
    Converts numerical analysis into AI-generated business insights.
    """

    def generate_insight(self, analysis_results, question):

        total_revenue = analysis_results["total_revenue"]
        top_product = analysis_results["top_product"]
        trend = analysis_results["monthly_trend"]

        prompt = f"""
You are a professional sales analyst.

The user asked:
"{question}"

Analyze the following verified business metrics and answer the user's question.

DATA:
- Total Revenue: {total_revenue}
- Top Product: {top_product}
- Monthly Revenue Trend: {trend}

Rules:
- Use only the provided data
- Do not invent numbers
- If the data is insufficient, say what additional data is needed
- Keep the answer clear and professional
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert sales analytics assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3
        )

        insight = response.choices[0].message.content

        return insight
    