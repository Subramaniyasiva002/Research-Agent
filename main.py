from typing import TypedDict, List, Dict
from langgraph.graph import StateGraph, END
from agents import search_agent, summarizer_agent, categorizer_agent, report_agent

# Define the state schema
class ResearchState(TypedDict, total=False):
    topics: str
    articles: List[Dict[str, str]]
    summaries: List[Dict[str, str]]
    categories: str
    status: str

# Create workflow with state schema
workflow = StateGraph(ResearchState)

# Add nodes (agents)
workflow.add_node("search", search_agent)
workflow.add_node("summarizer", summarizer_agent)
workflow.add_node("categorizer", categorizer_agent)
workflow.add_node("report", report_agent)

# Define edges (connections)
workflow.add_edge("search", "summarizer")
workflow.add_edge("summarizer", "categorizer")
workflow.add_edge("categorizer", "report")
workflow.add_edge("report", END)

# Entry point
workflow.set_entry_point("search")

# Compile graph
graph = workflow.compile()

# Input
input_state = {"topics": "AI Trend,LLMs,Agents"}

# Run
result = graph.invoke(input_state)
print("✅ Done:", result)
