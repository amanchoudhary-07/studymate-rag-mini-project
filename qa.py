from dotenv import load_dotenv

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from transformers import pipeline

load_dotenv()

print("Initializing StudyMate  Sales Forecast RAG System...\n")

# 1️⃣ Load embeddings (same as ingest.py)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 2️⃣ Load vector database
vector_db = FAISS.load_local(
    "vector_db",
    embeddings,
    allow_dangerous_deserialization=True
)

# 3️⃣ Retriever
retriever = vector_db.as_retriever(search_kwargs={"k": 3})

# 4️⃣ Local HuggingFace LLM (NO API)
qa_model = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_new_tokens=300
)

print("StudyMate is ready!")
print("Ask questions related to SALES FORECASTING.")
print("Type 'exit' to quit.\n")

# 5️⃣ Question loop
while True:
    query = input("Ask your question: ")

    if query.lower() in ["exit", "quit"]:
        print("Goodbye 👋 hope you are satisfied")
        break

    # Retrieve documents
    docs = retriever.invoke(query)

    if not docs:
        print("\nAnswer:")
        print("Answer not found in the provided notes.")
        print("-" * 60)
        continue

    # Build context
    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
Answer the question ONLY using the context below.
If the answer is not present, say:
"Answer not found in the provided notes."

Context:
{context}

Question:
{query}
"""

    result = qa_model(prompt)[0]["generated_text"]

    print("\nAnswer:")
    print(result)
    print("-" * 60)



