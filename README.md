A legal assistant to help a user navigate legal issues, powered by FastAPI and OpenRouter AI. This README covers setup, configuration, usage, and project structure.

Table of Contents
Features

Prerequisites

Installation

Configuration

Running the Server

API Endpoints

Project Structure

Prompt Customization

Contributing

License

Features
FastAPI-based HTTP server for low-latency AI calls 
GitHub

OpenRouter integration for chat completions 
GitHub
GitHub

CORS middleware enabled for development 
GitHub

Pydantic models for request/response validation 
GitHub

UUID-tagged responses with timestamps 
GitHub

Markdown-formatted answers via a customizable system prompt 
GitHub

Prerequisites
Python 3.10+ installed locally

An OpenRouter API key (sign up at openrouter.ai)

Git installed to clone the repository

Installation
Clone the repo

bash
Copy
Edit
git clone https://github.com/Masterkimaru/LegalBot-Backend.git
cd LegalBot-Backend
GitHub

Create and activate a virtual environment

bash
Copy
Edit
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
Install dependencies

bash
Copy
Edit
pip install --upgrade pip
pip install -r requirements.txt
GitHub

Configuration
Copy .env.example (if present) to .env, or create a new .env in the project root.

Set the following variables:

env
Copy
Edit
OPENROUTER_API_KEY=your_openrouter_api_key_here
GitHub

Running the Server
Start the API using Uvicorn:

bash
Copy
Edit
uvicorn main:app --reload --port 8000
--reload enables hot-reload for development.

Default port is 8000, change via --port flag. 
GitHub

API Endpoints
POST /query
Description: Send a legal question; returns a structured response.

Request Body (application/json):

json
Copy
Edit
{
  "question": "What are the requirements for a valid will in California?"
}
Response (200 OK):

json
Copy
Edit
{
  "id": "a1b2c3d4-5678-90ab-cdef-1234567890ab",
  "answer": "## Legal Requirements\n1. The testator must be at least 18...\n",
  "timestamp": "2025-04-23T12:34:56.789Z"
}
Error (500 Internal Server Error):

json
Copy
Edit
{ "detail": "Error message..." }
GitHub

Project Structure
graphql
Copy
Edit
LegalBot-Backend/
├── main.py            # FastAPI app and /query endpoint :contentReference[oaicite:11]{index=11}
├── prompt.py          # SYSTEM_PROMPT template for AI context :contentReference[oaicite:12]{index=12}
├── requirements.txt   # All Python dependencies :contentReference[oaicite:13]{index=13}
├── .gitignore
└── README.md          # ← You are here
Prompt Customization
The SYSTEM_PROMPT in prompt.py defines how the AI formats answers:

python
Copy
Edit
SYSTEM_PROMPT = """
You are an expert legal assistant specializing in international law…
# Legal Requirements
# Documentation
# Jurisdiction-Specific Advice
# Important Considerations
…
"""
Edit headings or instructions here to adjust AI behavior and Markdown structure. 
GitHub

Contributing
Fork this repository.

Create a feature branch: git checkout -b feature/YourFeature

Commit your changes: git commit -m 'Add YourFeature'

Push to your branch: git push origin feature/YourFeature

Open a Pull Request.

Please ensure new code includes tests and follows PEP 8.

License
This project is open-source under the MIT License.
