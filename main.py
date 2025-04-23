from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import requests
from dotenv import load_dotenv
from prompt import SYSTEM_PROMPT
from datetime import datetime
import uuid

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev. Lock this down in production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    id: str
    answer: str
    timestamp: datetime

@app.get("/")
async def health_check():
    """Health check endpoint for Render and monitoring"""
    return {
        "status": "live",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "LegalBot Backend"
    }

@app.post("/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    """
    Receives a JSON body {"question": "..."},
    forwards it to OpenRouter, and returns
    a structured QueryResponse.
    """
    try:
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://your-site-url.com",
            "X-Title": "Legal Chatbot",
        }
        payload = {
            "model": "featherless/qwerky-72b:free",
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": request.question}
            ],
            "temperature": 0.2,
            "max_tokens": 1500
        }

        resp = requests.post(OPENROUTER_API_URL, headers=headers, json=payload)
        data = resp.json()

        if resp.status_code != 200:
            # Propagate the error message if available
            error_msg = data.get("error", "Unknown error from OpenRouter")
            raise Exception(error_msg)

        return QueryResponse(
            id=str(uuid.uuid4()),
            answer=data["choices"][0]["message"]["content"],
            timestamp=datetime.utcnow()
        )

    except Exception as e:
        # Any exception becomes a 500 with the exception text
        raise HTTPException(status_code=500, detail=str(e))