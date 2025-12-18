from fastapi import APIRouter, Query, Response
from fastapi.responses import PlainTextResponse, StreamingResponse
from app.utils.validators import validate_sector
from app.services.data_collector import fetch_sector_news
from app.services.ai_analyzer import analyze_sector_with_ai
from app.services.report_generator import generate_markdown_report
import io

router = APIRouter(prefix="/analyze", tags=["Analyze"])

@router.get("/{sector}")
async def analyze_sector(
    sector: str,
    download: bool = Query(False, description="Download report as file")
):
    sector_clean = validate_sector(sector)
    items = fetch_sector_news(sector_clean)
    analysis = analyze_sector_with_ai(sector_clean, items)
    report = generate_markdown_report(sector_clean, analysis)

    # 🔹 DOWNLOAD MODE
    if download:
        filename = f"{sector_clean}_trade_report.md"
        file_like = io.BytesIO(report.encode("utf-8"))

        return StreamingResponse(
            file_like,
            media_type="text/markdown",
            headers={
                "Content-Disposition": f'attachment; filename="{filename}"'
            }
        )

    # 🔹 NORMAL VIEW MODE
    return PlainTextResponse(report)
