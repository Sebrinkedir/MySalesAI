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

You are given ONLY verified results computed by the Analysis Agent.

VERIFIED DATA:
{analysis_summary}

Your task:
Answer the user's question using only the verified data above.

Strict rules:
1. Do not invent causes.
2. Do not assume marketing, competition, seasonality, customer behavior, or inventory issues unless they are present in the verified data.
3. Separate facts from missing evidence.
4. If the reason cannot be fully determined from the data, clearly say so.
5. Keep the answer concise and professional.

Required response format:

Verified Findings:
- ...

Answer:
- ...

Missing Evidence:
- ...
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
    