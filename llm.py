import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_email(company_name):
    prompt = f"""
You are a startup founder writing a cold email.

Write a highly personalized cold email to {company_name}.

Rules:
- Max 60 words
- No generic phrases like "I came across your company"
- Be specific and confident
- Sound like a real human, not AI
- End with a simple CTA

Return ONLY the email text (no extra explanations).
"""

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama-3.1-8b-instant",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )

    print("STATUS:", response.status_code)
    print("RESPONSE:",response.text)

    if response.status_code != 200:
        return f"Error: {response.text}"

    data = response.json()

    return data.get("choices", [{}])[0].get("message",{}).get("content","No response")