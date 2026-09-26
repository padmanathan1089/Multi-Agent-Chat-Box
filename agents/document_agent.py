from utils.rag import create_vectorstore
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

pdf_path = "data/Employee Handbook.pdf"
vectorstore = create_vectorstore(pdf_path)


def document_agent(question):
    docs = vectorstore.similarity_search(question, k=3)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an HR Assistant.

Answer the question only from the employee handbook below.

Employee Handbook:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content