from datetime import datetime

def generate_markdown_report(sector: str, analysis: dict) -> str:
    """
    Generates a clean, human-readable Markdown report
    from structured analysis content.
    """
    date_str = datetime.utcnow().strftime("%Y-%m-%d")

    return f"""# Trade Opportunity Analysis — {sector.title()} Sector (India)

_Date: {date_str}_

## Market Overview
{analysis.get("overview", "")}

## Current Trends
{analysis.get("trends", "")}

## Trade Opportunities
{analysis.get("opportunities", "")}

## Risks & Considerations
{analysis.get("risks", "")}

---
_Report generated for informational purposes._
"""
