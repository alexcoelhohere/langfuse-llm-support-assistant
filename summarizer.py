import sys
sys.path.insert(0, "libs")  
from langfuse import Langfuse
from langfuse.decorators import observe
from langfuse.openai import openai

#  Hardcode Langfuse credentials
langfuse = Langfuse(
    public_key="",
    secret_key="",
    host=""
)

#  Hardcode OpenAI API key
openai.api_key = ""

#  Auto-summarize + categorize a support ticket
@observe()
def analyze_ticket(ticket_text):
    prompt = f"""
You are a customer support assistant.

1. Summarize the issue briefly.
2. Categorize it into one of: Billing, Login, Delivery, Refund, Technical, Other.

Ticket: {ticket_text}
"""

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Respond in two parts: Summary and Category."},
            {"role": "user", "content": prompt}
        ]
    )

    result = response.choices[0].message.content.strip()
    print(f"\n📩 Ticket:\n{ticket_text}")
    print(f"\n🧾 Analysis:\n{result}")
    return result

if __name__ == "__main__":
    analyze_ticket("The checkout page keeps freezing whenever I try to add my card details. I’ve tried 3 browsers.")