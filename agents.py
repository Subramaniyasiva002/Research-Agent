import os
import requests
from dotenv import load_dotenv
from tavily_search import search_latest_articles

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = "openai/gpt-oss-20b:free"   # You can change model here

def query_openrouter(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://openrouter.ai",   # REQUIRED by OpenRouter
        "X-Title": "Research Agent"                # Custom title (mandatory)
    }
    data = {
        "model": "openai/gpt-oss-20b:free",  # ✅ free model
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        res_json = response.json()

        # Handle API errors safely
        if "choices" in res_json:
            return res_json["choices"][0]["message"]["content"]
        elif "error" in res_json:
            print("🚨 OpenRouter Error:", res_json["error"])
            return f"[Error: {res_json['error'].get('message', 'Unknown error')}]"
        else:
            print("⚠️ Unexpected Response:", res_json)
            return "[Error: Unexpected API response]"

    except Exception as e:
        print("❌ Exception calling OpenRouter:", e)
        return f"[Exception: {str(e)}]"


# --- AGENT 1: Search ---
def search_agent(state):
    topics = state.get("topics", "")
    print(f"🔍 Searching for: {topics}")
    articles = search_latest_articles(topics)
    return {"articles": articles}

# --- AGENT 2: Summarizer ---
def summarizer_agent(state):
    summaries = []
    for article in state["articles"]:
        text = article.get("content", "")[:4000]
        prompt = f"Summarize this AI-related article in 3 lines, focusing on innovation and tech relevance:\n\n{text}"
        summary = query_openrouter(prompt)
        summaries.append({"title": article["title"], "summary": summary, "url": article["url"]})
    return {"summaries": summaries}

# --- AGENT 3: Categorizer ---
def categorizer_agent(state):
    prompt = (
        "Classify these summaries into categories like LLMs, RAG, Edge AI, Agents, or Others:\n"
        f"{state['summaries']}\n"
        "Return a JSON structure mapping category -> list of titles."
    )
    categories = query_openrouter(prompt)
    return {"categories": categories}

# --- AGENT 4: Report ---
from mailer import send_alert

def report_agent(state):
    file_path = "daily_research_digest.md"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("# 🧠 AI Research Digest\n\n")
        for s in state["summaries"]:
            f.write(f"### {s['title']}\n{s['summary']}\n🔗 {s['url']}\n\n")
        f.write("\n## Categories\n")
        f.write(state.get("categories", "No categories generated."))

    print(f"✅ Report saved to {file_path}")

    # Send to Discord
    with open(file_path, "r", encoding="utf-8") as f:
        digest_text = f.read()

    send_alert("Daily Research Digest", digest_text)

    return {"status": "saved"}


