from utils.rag import create_vectorstore

# Your PDF path
pdf_path = "data/Employee Handbook.pdf"

vectorstore = create_vectorstore(pdf_path)

print("✅ Vector Database Created Successfully!")

query = "What is this document about?"

docs = vectorstore.similarity_search(query, k=2)

print("\nTop Results:\n")

for doc in docs:
    print(doc.page_content)
    print("-" * 80)