import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from utils.rag import create_vectorstore

# Load environment variables
load_dotenv()

# Initialize Groq LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

# Load PDF into vector database
pdf_path = "data/Employee Handbook.pdf"
vectorstore = create_vectorstore(pdf_path)

print("🤖 Employee Handbook Chatbot")
print("Type 'exit' to quit.\n")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    # Retrieve relevant document chunks
    docs = vectorstore.similarity_search(question, k=3)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an HR assistant.

Answer ONLY using the information below.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    print("\nAI:", response.content)
    print("-" * 80)