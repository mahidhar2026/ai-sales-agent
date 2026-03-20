#  AI Sales Agent

An AI-powered tool that generates company leads and personalized cold emails from a simple niche query.

##  Problem

Startups and sales teams spend significant time:
- Finding relevant leads manually
- Writing repetitive cold emails
- Using expensive tools for outreach automation

## Solution

This project builds an **AI Sales Agent** that:
- Takes a niche query (e.g., "fintech startups")
- Generates relevant company leads
- Creates personalized outreach emails using LLMs
- Displays results in a clean UI
- Allows CSV export for real-world usage

---

##  Tech Stack

- **Backend:** FastAPI
- **Frontend:** Streamlit
- **LLM:** Groq API (Llama models)
- **Language:** Python

---

##  Architecture
User Input (niche)
↓
Query-aware Data Layer (simulated API)
↓
LLM (Groq API)
↓
FastAPI Backend
↓
Streamlit UI
↓
CSV Export

---

##  Features

-  Query-based lead generation
-  AI-generated personalized cold emails
-  Fast API backend
-  Simple and interactive UI
-  CSV export for leads
-  Simulated email sending workflow

---

##  Example

**Input:**
fintech startups


**Output:**
- Stripe → Personalized email
- Plaid → Personalized email
- Razorpay → Personalized email

---



## 🚀 How to Run Locally

### 1. Clone repo
```bash
git clone https://github.com/your-username/ai-sales-agent.git
cd ai-sales-agent
2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
3. Install dependencies
pip install -r requirements.txt
4. Add environment variables

Create .env file:

GROQ_API_KEY=your_api_key_here
5. Run backend
uvicorn app:app --reload
6. Run frontend
streamlit run ui.py
```


## Acknowledgements

Groq API for fast LLM inference

Streamlit for rapid UI development

FastAPI for lightweight backend

## Contact

Feel free to connect or reach out!


