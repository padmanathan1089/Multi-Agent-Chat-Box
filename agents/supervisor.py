from agents.document_agent import document_agent
from agents.general_agent import general_agent
from agents.review_agent import review_agent


def supervisor(question):
    """
    Simple routing logic.
    HR/document questions go to Document Agent.
    Everything else goes to General Agent.
    """

    keywords = [
        "employee",
        "leave",
        "policy",
        "salary",
        "attendance",
        "holiday",
        "benefits",
        "handbook",
        "working hours"
    ]

    if any(word in question.lower() for word in keywords):
        print("\n📄 Supervisor: Routing to Document Agent...\n")
        answer = document_agent(question)
    else:
        print("\n🌍 Supervisor: Routing to General Agent...\n")
        answer = general_agent(question)

    print("✅ Sending answer to Review Agent...\n")

    final_answer = review_agent(answer)

    return final_answer