import os
import time
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class SingleAgent:
    """
    Baseline system:
    One agent handles loading, analysis, and explanation.
    """

    def run(self, file_path, question):
        start_time = time.time()

        df = pd.read_csv(file_path)

        total_revenue = int(df["revenue"].sum())

        top_product = df.groupby("product")["revenue"].sum().idxmax()

        df["date"] = pd.to_datetime(df["date"])
        monthly = df.groupby(df["date"].dt.to_period("M"))["revenue"].sum()

        monthly_trend = {
            str(month): int(value)
            for month, value in monthly.items()
        }

        monthly_percentage_change = monthly.pct_change() * 100

        monthly_percentage_change = {
            str(month): round(value, 2) if pd.notna(value) else None
            for month, value in monthly_percentage_change.items()
        }

        analysis_results = {
            "total_revenue": total_revenue,
            "top_product": top_product,
            "monthly_trend": monthly_trend,
            "monthly_percentage_change": monthly_percentage_change
        }

        prompt = f"""
You are a single AI sales analyst.

The user asked:
"{question}"

You are responsible for:
1. Understanding the data
2. Computing insights
3. Explaining results

Verified calculated metrics:
{analysis_results}

Rules:
- Use only the verified calculated metrics above
- Do not invent numbers
- If the data is insufficient, say what additional data is needed
- Keep the answer clear and professional
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a single-agent sales analytics assistant."
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