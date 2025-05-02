# Langfuse LLM Support Summarizer 🧾

A lightweight, Langfuse-instrumented tool that summarizes and categorizes customer support tickets using OpenAI’s GPT-4o.

This project showcases how LLMs can reduce agent workload, accelerate onboarding, and help surface high-volume support themes — all with traceability and observability via Langfuse.

---

## ✨ Features

- 🔍 **Summarize** customer support tickets into concise summaries
- 🏷️ **Categorize** tickets into predefined categories:
  `Billing, Login, Delivery, Refund, Technical, Other`
- 🎓 Use output as **training material** for onboarding new agents
- 📈 Full **LLM observability** with [Langfuse](https://langfuse.com) via `@observe()` and `langfuse.openai`

---

## 💼 Business Use Cases

- 📉 **Reduce average handle time (AHT)** by giving agents auto-generated summaries
- 🎓 **Train new agents faster** using categorized summaries as examples
- 🧠 **Discover support hotspots** by tagging high-volume issues
