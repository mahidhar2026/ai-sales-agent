from fastapi import FastAPI
from scraper import get_companies
from llm import generate_email

app = FastAPI()

@app.get("/")
def home():
    return {"message":"AI Sales Agent Running"}

@app.get("/leads")
def get_leads(query: str =""):
    companies = get_companies(query)

    output = []

    for c in companies:
        email = generate_email(c["name"])

        output.append({
            "company": c["name"],
            "email": email 
        })
    return output