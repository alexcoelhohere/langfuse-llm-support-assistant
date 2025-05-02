# 🧾 LLM-Powered Support Assitant

This project uses **GPT-4o** and **Langfuse** to automatically summarize and categorize customer support tickets. It's designed to help support teams onboard agents faster, improve triage, and build datasets for future training and QA workflows.

## 🚀 What It Does

For any given support ticket (e.g., a customer complaint or issue), this script:

1. Generates a **concise summary** using GPT-4o
2. Automatically assigns a **category** (Billing, Login, Delivery, etc.)
3. Logs the result to a `.csv` file with a **unique ticket ID**
4. Optionally tracks each interaction using **Langfuse** for observability

## 💡 Why It Matters

- Build a **training set** for onboarding support agents
- Enable **tag-based analytics** across ticket types
- Use clean, structured LLM outputs in real operations
- Gain **traceability** and debugging visibility with Langfuse

---

## 🛠️ Tech Stack

- **[OpenAI GPT-4o](https://platform.openai.com/)** — For generating summaries and tags
- **[Langfuse](https://langfuse.com/)** — To trace prompt/response behavior and monitor outputs
- **Python** — Scripting and CSV generation
