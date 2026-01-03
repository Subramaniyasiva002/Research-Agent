AI Research Digest Agent

An autonomous multi-agent research system that periodically collects the latest AI & technology updates, summarizes them using LLMs, categorizes insights, and delivers a structured digest automatically via Discord.

🚀 Project Overview

The AI Research Digest Agent acts as a personal AI research analyst.
It continuously monitors selected AI/tech topics and produces a concise, structured research digest every 48 hours, without any manual intervention.

The agent is built using LangGraph for orchestration, Tavily for real-time web search, and OpenRouter LLMs for reasoning and summarization.

✨ Key Capabilities

🔍 Automated Web Research
Fetches real-time AI & tech articles using Tavily API.

🧠 LLM-Powered Summarization
Uses OpenRouter models to generate high-quality technical summaries.

🗂 Intelligent Categorization
Automatically groups articles into domains like LLMs, RAG, Agents, Industry News, etc.

📝 Structured Markdown Digest
Generates a readable research report (daily_research_digest.md).

📤 Discord Notifications
Sends the complete digest directly to a Discord channel using webhooks.

🔁 Fully Automated Execution
Runs every 48 hours using GitHub Actions (cron-based scheduling).

🧠 Why This Is an AI Agent

This project qualifies as a real AI agent system because it:

Perceives → fetches live web data

Reasons → uses LLMs for summarization & classification

Acts → writes files & sends notifications

Operates autonomously → scheduled execution without human input

Memory and self-learning are optional enhancements, not requirements.

🏗️ System Architecture
GitHub Actions (Every 48 Hours)
            |
            v
      LangGraph StateGraph
            |
------------------------------------------------
|                |                |            |
v                v                v            v
Search Agent   Summarizer Agent  Categorizer  Report Agent
(Tavily API)   (OpenRouter LLM)     (LLM)     (Discord Webhook)

🔄 Multi-Agent Workflow
1️⃣ Search Agent

Queries Tavily with predefined topics

Collects latest article titles, URLs, and content

2️⃣ Summarizer Agent

Uses OpenRouter LLM

Produces concise, technical summaries

3️⃣ Categorizer Agent

Classifies articles into logical domains

4️⃣ Report Agent

Generates a Markdown digest

Sends the digest to Discord

📁 Project Structure
Research_Agent/
│
├── main.py                  # LangGraph workflow definition
├── agents.py                # Search, summarize, categorize, report agents
├── tavily_search.py         # Tavily API integration
├── mailer.py                # Discord webhook notifier
├── run_agent.py             # Entry point for automation
├── requirements.txt         # Dependencies
└── daily_research_digest.md # Auto-generated output

⚙️ Tech Stack
Component	Technology
Orchestration	LangGraph
Web Search	Tavily API
LLM Provider	OpenRouter
Notifications	Discord Webhook
Automation	GitHub Actions
Language	Python
🔐 Environment Variables

Set these as GitHub Secrets or in a local .env file:

TAVILY_API_KEY=your_tavily_api_key
OPENROUTER_API_KEY=your_openrouter_api_key
DISCORD_WEBHOOK=https://discord.com/api/webhooks/xxxx

▶️ Run Locally
git clone https://github.com/yourusername/research-agent.git
cd research-agent
pip install -r requirements.txt
python run_agent.py

☁️ Automated Deployment (GitHub Actions)

The agent is automated using GitHub Actions with a cron schedule.

✔ Runs in GitHub’s cloud
✔ No server or VPS required
✔ Free for public repositories
✔ Executes every 48 hours
Workflow File
.github/workflows/agent.yml

Cron Configuration
on:
  schedule:
    - cron: "0 0 */2 * *"


The workflow:

Installs Python & dependencies

Executes run_agent.py

Sends digest to Discord

📌 Output Example
# 🧠 AI Research Digest

### LangGraph & Agentic AI
Summary...
🔗 https://example.com

### RAG Systems
Summary...
🔗 https://example.com

## Categories
{
  "Agents": [...],
  "RAG": [...],
  "Industry": [...]
}

🌱 Future Improvements

Topic memory to avoid duplicate articles

Vector database for long-term knowledge

Trend analysis & keyword tracking

Telegram / Slack integration

Web dashboard (Streamlit / Vue)

Self-reflection & agent planning loop
