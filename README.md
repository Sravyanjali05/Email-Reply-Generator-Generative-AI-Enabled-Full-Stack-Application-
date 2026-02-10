# Email-Reply-Generator-Generative-AI-Enabled-Full-Stack-Application-
Built a full-stack AI email reply generator using Python and FastAPI. The system analyzes incoming emails, detects user intent, and generates context-aware responses using a locally hosted LLM. Designed REST APIs, database logging, and an extensible AI pipeline suitable for production-grade GenAI features.
## Features
- Email intent detection (complaint, inquiry, appreciation, general)
- AI-generated email replies using a local LLM
- REST API built with FastAPI
- SQLite database for logging interactions
- Simple web-based UI for testing

## Tech Stack
- Backend: Python, FastAPI
- Frontend: HTML, JavaScript
- Database: SQLite
- Generative AI: Local LLM via Ollama
- Version Control: Git, GitHub

## How It Works
1. User enters an email message in the UI
2. Backend detects intent using NLP logic
3. Email is sent to a local LLM for response generation
4. AI-generated reply is returned and stored in the database

## How to Run Locally

### 1. Create virtual environment
