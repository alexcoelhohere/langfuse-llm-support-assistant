import sys
import uuid
import json
import csv

sys.path.insert(0, "libs")

from langfuse import Langfuse
from langfuse.openai import openai

#  Langfuse Initialization
langfuse = Langfuse(
    public_key="",
    secret_key="",
    host=""
)

#  OpenAI API key
openai.api_key = ""  

#  Function to analyze and tag ticket
def analyze_ticket(ticket_text):
    trace = langfuse.trace(
        trace_id=str(uuid.uuid4()),
        name="ticket_analysis"
    )

    prompt = f"""
You are a customer support assistant.

Given the following support ticket, return a *valid* JSON object with the following fields:
- "summary": A 1-sentence summary of the user's issue
- "category": One of ["Billing", "Login", "Delivery", "Refund", "Technical", "Other"]

Ticket: {ticket_text}

⚠️ Respond only with raw JSON. No explanation, no markdown, no prose.
"""

    span = trace.span(name="analyze_ticket", input=prompt)

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Respond in JSON format."},
            {"role": "user", "content": prompt}
        ]
    )

    raw_output = response.choices[0].message.content.strip()
    span.output = raw_output
    span.end()

    try:
        parsed = json.loads(raw_output)
    except json.JSONDecodeError:
        parsed = {"summary": "", "category": "Other"}

    print(f"\n📩 Ticket:\n{ticket_text}")
    print(f"\n🧾 Summary:\n{parsed['summary']}")
    print(f"🏷️ Category: {parsed['category']}")

    return {
        "ticket_id": str(uuid.uuid4()),
        "ticket": ticket_text,
        "summary": parsed["summary"],
        "category": parsed["category"]
    }

#  Function to save to CSV
def save_to_csv(data, filename="training_data.csv"):
    fieldnames = ["ticket_id", "ticket", "summary", "category"]
    file_exists = False
    try:
        with open(filename, "r"):
            file_exists = True
    except FileNotFoundError:
        pass

    with open(filename, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

#  Run it
if __name__ == "__main__":
    ticket = "I was charged twice for my last payment and haven't heard back from support."
    parsed_result = analyze_ticket(ticket)
    save_to_csv(parsed_result)
