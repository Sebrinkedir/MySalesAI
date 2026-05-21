from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import os


def generate_pdf_report(mode, question, analysis, insights, latency=None, chart_path=None):
    file_name = f"reports/mysalesai_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

    c = canvas.Canvas(file_name, pagesize=A4)
    width, height = A4

    y = height - 50

    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, y, "MySalesAI Sales Analysis Report")

    y -= 40
    c.setFont("Helvetica", 11)
    c.drawString(50, y, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    y -= 25
    c.drawString(50, y, f"System Mode: {mode}")

    y -= 25
    c.drawString(50, y, f"Question: {question}")

    y -= 40
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Analysis Results")

    y -= 25
    c.setFont("Helvetica", 10)

    for key, value in analysis.items():
        c.drawString(50, y, f"{key}: {value}")
        y -= 18

    if latency is not None:
        y -= 10
        c.drawString(50, y, f"Latency: {latency} seconds")
        y -= 25

    if chart_path is not None and os.path.exists(chart_path):
        y -= 10
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, y, "Revenue Trend Chart")

        y -= 230
        c.drawImage(chart_path, 50, y, width=480, height=220)

        y -= 40

    if y < 150:
        c.showPage()
        y = height - 50

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Generated Insights")

    y -= 25
    c.setFont("Helvetica", 10)

    for line in insights.split("\n"):
        if y < 60:
            c.showPage()
            y = height - 50
            c.setFont("Helvetica", 10)

        c.drawString(50, y, line[:95])
        y -= 15

    c.save()

    return file_name