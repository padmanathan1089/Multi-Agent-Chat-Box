import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load .env file
load_dotenv()

# Create Groq LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

# Ask a question
response = llm.invoke("Introduce yourself in three lines.")

print(response.content)