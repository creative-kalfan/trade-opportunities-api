import os
import google.generativeai as genai
from app.utils.logger import logger

def analyze_sector_with_ai(sector: str, items: list[dict]) -> dict:
    """
    Produces a structured market analysis for a given sector.
    Falls back to heuristic analysis if AI is unavailable.
    """
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        logger.warning("GEMINI_API_KEY not set, using fallback analysis")
        return _fallback_analysis(sector)

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")

        context = "\n".join(
            f"- {i.get('title','')}: {i.get('snippet','')}"
            for i in items
        ) or "No recent public market data available."

        prompt = f"""
You are an Indian market analyst.
Write a concise, factual analysis of the '{sector}' sector in India.

Guidelines:
- Professional, neutral tone
- No hype, no emojis
- Avoid mentioning AI or models
- If data is limited, state uncertainty clearly

Context:
{context}

Sections:
Market Overview
Current Trends
Trade Opportunities
Risks & Considerations
"""

        response = model.generate_content(prompt)
        text = response.text or ""

        return {
            "overview": _extract(text, "Market Overview"),
            "trends": _extract(text, "Current Trends"),
            "opportunities": _extract(text, "Trade Opportunities"),
            "risks": _extract(text, "Risks & Considerations"),
        }

    except Exception as exc:
        logger.error(f"AI analysis failed: {exc}")
        return _fallback_analysis(sector)

def _fallback_analysis(sector: str) -> dict:
    return {
        "overview": f"The {sector} sector in India is showing cautious movement with limited recent signals.",
        "trends": "Gradual adoption, operational efficiency, and regulatory alignment are key themes.",
        "opportunities": "Selective investments, partnerships, and niche expansions may offer potential.",
        "risks": "Policy shifts, cost pressures, and global uncertainty remain notable risks.",
    }

def _extract(text: str, heading: str) -> str:
    if heading in text:
        return text.split(heading, 1)[-1].strip().split("\n\n")[0].strip()
    return ""
