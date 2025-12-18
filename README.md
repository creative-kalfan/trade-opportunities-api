# Trade Opportunities API

A FastAPI-based backend service that analyzes trade opportunities for key Indian market sectors and generates a structured, human-readable **Markdown report**.  
The service is designed to be simple to run, easy to test, and safe against misuse.

This project was built as part of a **Python Developer (0–2 Years Experience)** technical assignment.

---

## 🚀 Features

- Sector-based trade opportunity analysis
- Real-time market/news data collection
- AI-powered analysis with graceful fallback logic
- Clean, readable **Markdown reports**
- Optional **report download** as `.md` file
- API-key based authentication
- In-memory rate limiting to prevent abuse
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
│   ├── api/
│   │   └── analyze.py
│   ├── services/
│   │   ├── data_collector.py
│   │   ├── ai_analyzer.py
│   │   └── report_generator.py
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── rate_limiter.py
│   ├── utils/
│   │   ├── validators.py
│   │   └── logger.py
│   └── main.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ (Optional) Configure AI key

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

The application works even **without** an AI key using fallback analysis.

---

## ▶️ Running the Application

```bash
python -m uvicorn app.main:app --port 8001
```

Server starts at:

```
http://127.0.0.1:8001
```

---

## 🔐 Authentication

All protected endpoints require an API key passed via header:

```
X-API-Key: demo-key-123
```

---

## 📊 Analyze Sector

**Endpoint**

```
GET /analyze/{sector}
```

**Example**

```
GET /analyze/technology
```

**Response**

- Markdown-formatted trade analysis report
- Displayed as plain text in the browser

---

## ⬇️ Download Report as File

Append `?download=true` to download the report.

```
GET /analyze/{sector}?download=true
```

**Example**

```
GET /analyze/technology?download=true
```

**Result**

- Browser downloads a file named `technology_trade_report.md`

---

## 📄 Report Structure

Each generated report contains:

1. Market Overview  
2. Current Trends  
3. Trade Opportunities  
4. Risks & Considerations  

---

## 🚦 Rate Limiting

- **60 requests per 5 minutes per IP**

Exceeded limit response:

```json
{
  "detail": "Rate limit exceeded. Try again later."
}
```

---

## ❗ Error Handling

- Invalid sector → `400 Bad Request`
- Missing / invalid API key → `401 Unauthorized`
- Too many requests → `429 Too Many Requests`
- External data or AI failures are handled gracefully

---

## 🧪 Testing

You can test the API using:

- Browser
- Swagger UI (`/docs`)
- Postman
- curl

**curl example**

```bash
curl -H "X-API-Key: demo-key-123" \
"http://127.0.0.1:8001/analyze/technology?download=true" \
-o report.md
```

---

## 📝 Notes

- No external database is used
- Rate limiting and session tracking are in-memory
- Designed for demo / assignment purposes
- Clean architecture allows easy extension

---

## 👤 Author

Built as part of a Python Developer technical assignment to demonstrate:

- Backend API design
- Authentication and rate limiting
- Error handling
- Clean architecture
- Practical problem-solving
