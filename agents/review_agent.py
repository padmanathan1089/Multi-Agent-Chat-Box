from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)


def review_agent(answer):
    prompt = f"""
Improve the following answer.
Make it professional and easy to understand.

Answer:
{answer}
"""

    response = llm.invoke(prompt)

    return response.content