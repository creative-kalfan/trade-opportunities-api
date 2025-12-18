import antigravity

from fastapi import FastAPI
from app.core.config import settings
from app.utils.logger import logger
from app.api.analyze import router as analyze_router

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG
)

@app.get("/")
async def health_check():
    return {
        "status": "ok",
        "service": settings.APP_NAME,
        "env": settings.ENV
    }

app.include_router(analyze_router)

logger.info("FastAPI application initialized")
