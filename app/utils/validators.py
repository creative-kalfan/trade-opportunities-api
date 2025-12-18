import re
from fastapi import HTTPException

_ALLOWED_SECTORS = {
    "pharmaceuticals",
    "technology",
    "agriculture",
    "energy",
    "finance",
    "automobile",
    "infrastructure"
}

def validate_sector(sector: str) -> str:
    if not sector:
        raise HTTPException(status_code=400, detail="Sector is required")

    sector_clean = sector.strip().lower()

    if not re.fullmatch(r"[a-z]+", sector_clean):
        raise HTTPException(
            status_code=400,
            detail="Sector must contain only lowercase alphabets"
        )

    if sector_clean not in _ALLOWED_SECTORS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported sector. Allowed: {sorted(_ALLOWED_SECTORS)}"
        )

    return sector_clean
