from langgraph_workflow import app

print("=" * 60)
print("🤖 LangGraph Multi-Agent Chatbot")
print("=" * 60)

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    result = app.invoke({
        "question": question,
        "answer": ""
    })

    print("\nAI:")
    print(result["answer"])
    print("-" * 60)