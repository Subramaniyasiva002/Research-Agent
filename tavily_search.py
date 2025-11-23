import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_latest_articles(topics, max_results=5):
    query = f"latest research papers, AI news or blog posts on {topics}"
    response = tavily.search(query=query, max_results=max_results)
    articles = []
    for r in response.get("results", []):
        articles.append({
            "title": r.get("title", "Untitled"),
            "url": r.get("url", ""),
            "content": r.get("content", "")
        })
    return articles
