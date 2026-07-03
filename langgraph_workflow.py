from typing import TypedDict
from langgraph.graph import StateGraph, END

from agents.document_agent import document_agent
from agents.general_agent import general_agent
from agents.review_agent import review_agent


class AgentState(TypedDict):
    question: str
    answer: str


# -------- Document Node --------
def document_node(state: AgentState):
    answer = document_agent(state["question"])
    return {
        "question": state["question"],
        "answer": answer
    }


# -------- General Node --------
def general_node(state: AgentState):
    answer = general_agent(state["question"])
    return {
        "question": state["question"],
        "answer": answer
    }


# -------- Review Node --------
def review_node(state: AgentState):
    final = review_agent(state["answer"])
    return {
        "question": state["question"],
        "answer": final
    }


# -------- Router --------
def router(state: AgentState):

    question = state["question"].lower()

    keywords = [
        "leave",
        "policy",
        "employee",
        "attendance",
        "salary",
        "benefits",
        "holiday"
    ]

    if any(word in question for word in keywords):
        return "document"

    return "general"


graph = StateGraph(AgentState)

graph.add_node("document", document_node)
graph.add_node("general", general_node)
graph.add_node("review", review_node)

graph.set_conditional_entry_point(
    router,
    {
        "document": "document",
        "general": "general",
    },
)

graph.add_edge("document", "review")
graph.add_edge("general", "review")
graph.add_edge("review", END)

app = graph.compile()