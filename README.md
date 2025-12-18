# Trade Opportunities API

A FastAPI-based backend service that analyzes trade opportunities for key Indian market sectors and generates a structured, human-readable **Markdown report**.  
The service is designed to be simple to run, easy to test, and safe against misuse.

This project was built as part of a **Python Developer (0–2 Years Experience)** assignment.

---

## 🚀 Features

- Sector-based trade opportunity analysis
- Real-time market/news data collection
- AI-powered analysis with graceful fallback
- Clean, readable **Markdown reports**
- Optional **report download** as `.md` file
- API-key based authentication
- Rate limiting to prevent abuse
- Clear project structure and documentation

---

## 🛠 Tech Stack

- **Python 3.10+**
- **FastAPI**
- **Uvicorn**
- **Requests + BeautifulSoup** (data collection)
- **Gemini API (optional)** with fallback logic
- In-memory rate limiting
- Markdown report generation

---

## 📁 Project Structure

```
trade_opportunities_api/
│
├── app/
│ ├── api/
│ │ └── analyze.py
│ ├── services/
│ │ ├── data_collector.py
│ │ ├── ai_analyzer.py
│ │ └── report_generator.py
│ ├── core/
│ │ ├── config.py
│ │ ├── security.py
│ │ └── rate_limiter.py
│ ├── utils/
│ │ ├── validators.py
│ │ └── logger.py
│ └── main.py
│
├── .env
├── requirements.txt
└── README.md



---

## ⚙️ Setup Instructions

### 1️⃣ Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate

#installing dependencies

pip install -r requirements.txt

(Optional) Configure AI key

Create a .env file:

GEMINI_API_KEY=your_api_key_here


The application works even without an AI key using fallback analysis.

##▶️ Running the Application
python -m uvicorn app.main:app --port 8001

Server will start at:

http://127.0.0.1:8001

Analyze Sector (Protected)
GET /analyze/{sector}


Example:

GET /analyze/technology


Returns:

A Markdown-formatted trade analysis report

Displayed as plain text in the browser


##⬇️ Download Report as File

You can also download the report as a .md file.

GET /analyze/{sector}?download=true


Example:

GET /analyze/technology?download=true


Result:

Browser downloads a file named:

technology_trade_report.md


This allows easy sharing, saving, or further editing of the report.

##📄 Report Structure

Each generated report contains:

1. Market Overview

2. Current Trends

3. Trade Opportunities

4. Risks & Considerations

##🚦 Rate Limiting

60 requests per 5 minutes per IP

Exceeding the limit returns:

{
  "detail": "Rate limit exceeded. Try again later."
}



##❗ Error Handling

1.Invalid sector → 400 Bad Request

2.Missing / invalid API key → 401 Unauthorized

3.Too many requests → 429 Too Many Requests

4.External data or AI failures are handled gracefully (no crashes)


##🧪 Testing

You can test all endpoints using:

1.Browser

2.Swagger UI (/docs)

3.Postman

4.curl

Example with curl:

curl -H "X-API-Key: demo-key-123" \
     "http://127.0.0.1:8001/analyze/technology?download=true" \
     -o report.md

##📝 Notes

1.No external database is used

2.Rate limiting and session tracking are in-memory

3.Designed for demo / assignment purposes

4.Clean architecture for easy extension

##👤 Author

Built as part of a Python Developer technical assignment to demonstrate:

1.Backend API design

2.Error handling

3.Clean architecture

4.Practical problem-solving

