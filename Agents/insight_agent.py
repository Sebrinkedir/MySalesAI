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

        analysis_summary = "\n".join(
    [f"- {key}: {value}" for key, value in analysis_results.items()]
)

        prompt = f"""
You are a professional sales analyst.

The user asked:
"{question}"

Analyze the following verified business metrics and answer the user's question.

DATA:
{analysis_summary}

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
    