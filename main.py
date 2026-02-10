from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from database import SessionLocal, EmailLog
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class EmailInput(BaseModel):
    message: str


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Intent detection
def detect_intent(text):
    text = text.lower()

    if "not happy" in text or "complaint" in text or "bad" in text or "delay" in text:
        return "complaint"
    elif "price" in text or "cost" in text or "details" in text:
        return "inquiry"
    elif "thank" in text or "great" in text:
        return "appreciation"
    else:
        return "general"


# LLM-based reply generator
def generate_reply(intent, message):
    prompt = f"""
You are a professional customer support agent.

Customer email:
{message}

Intent: {intent}

Write a polite and helpful reply in 2–3 sentences.
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi3:mini",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"].strip()


@app.post("/generate")
def generate_email(data: EmailInput):
    intent = detect_intent(data.message)
    reply = generate_reply(intent, data.message)

    # Save to database
    db = SessionLocal()
    log = EmailLog(original=data.message, reply=reply)
    db.add(log)
    db.commit()
    db.close()

    return {
        "intent": intent,
        "reply": reply
    }
