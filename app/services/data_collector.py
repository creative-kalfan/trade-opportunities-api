import requests
from bs4 import BeautifulSoup
from app.utils.logger import logger

_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def fetch_sector_news(sector: str) -> list[dict]:
    """
    Fetch recent market/news snippets for a given sector in India.
    Returns a list of dicts with title, snippet, source.
    """
    query = f"{sector} sector India market news"
    url = "https://duckduckgo.com/html/"

    try:
        response = requests.post(
            url,
            data={"q": query},
            headers=_HEADERS,
            timeout=10
        )
        response.raise_for_status()
    except Exception as exc:
        logger.error(f"Data fetch failed for sector={sector}: {exc}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    results = []

    for item in soup.select(".result__body")[:5]:
        title_el = item.select_one(".result__title")
        snippet_el = item.select_one(".result__snippet")
        source_el = item.select_one(".result__url")

        results.append({
            "title": title_el.get_text(strip=True) if title_el else "",
            "snippet": snippet_el.get_text(strip=True) if snippet_el else "",
            "source": source_el.get_text(strip=True) if source_el else ""
        })

    logger.info(f"Collected {len(results)} items for sector={sector}")
    return results
