import random

def get_companies(query):
    if not query:
        return []

    query = query.lower()

    fintech = ["Stripe", "Plaid", "Razorpay", "Brex", "Ramp"]
    healthcare = ["Practo", "HealthifyMe", "Doctolib", "Zocdoc", "1mg"]
    edtech = ["Byju's", "Unacademy", "Coursera", "Udemy", "Khan Academy"]
    ai = ["OpenAI", "Anthropic", "Perplexity", "Cohere", "Mistral"]

    # 🔥 simple routing logic
    if "fintech" in query:
        base = fintech
    elif "health" in query:
        base = healthcare
    elif "edtech" in query:
        base = edtech
    elif "ai" in query:
        base = ai
    else:
        base = ["StartupX", "NextGen", "InnovateAI", "FutureTech", "CoreLabs"]

    return [{"name": name} for name in random.sample(base, 5)]