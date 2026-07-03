from agents.supervisor import supervisor

print("=" * 60)
print("🤖 Multi-Agent AI Chatbot")
print("=" * 60)

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    response = supervisor(question)

    print("\nAI:")
    print(response)