from dotenv import load_dotenv

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import pipeline

from feedback import collect_feedback
from reward_model import compute_reward
from rlhf_loop import optimize_prompt

load_dotenv()

print("Initializing StudyMate – Sales Forecast RAG + RLHF System...\n")

# 1️⃣ Load embeddings
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

# 4️⃣ Local HuggingFace LLM (NO API, NO COST)
qa_model = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_new_tokens=300
)

# 5️⃣ Base prompt (this will evolve via RLHF)
base_prompt = """
You are a helpful assistant.
Answer strictly using the provided context.
Be clear, concise, and accurate.
"""

print("StudyMate is ready!")
print("Ask questions related to SALES FORECASTING.")
print("Type 'exit' to quit.\n")

# 6️⃣ Main RLHF loop
while True:
    query = input("Ask your question: ")

    if query.lower() in ["exit", "quit"]:
        print("Goodbye 👋 Hope you found this helpful!")
        break

    # Retrieve relevant documents
    docs = retriever.invoke(query)

    if not docs:
        print("\nAnswer:")
        print("Answer not found in the provided notes.")
        print("-" * 60)
        continue

    # Build context
    context = "\n\n".join(doc.page_content for doc in docs)

    # Build prompt
    prompt = f"""
{base_prompt}

Context:
{context}

Question:
{query}
"""

    # Generate answer
    result = qa_model(prompt)[0]["generated_text"]

    print("\nAnswer:")
    print(result)
    print("-" * 60)

    # 🔁 RLHF: Collect human feedback
    try:
        rating = int(input("Rate the answer (1-5): "))
        if rating < 1 or rating > 5:
            raise ValueError
    except ValueError:
        print("Invalid rating. Skipping feedback.\n")
        continue

    # Store feedback
    collect_feedback(query, result, rating)

    # Compute reward
    reward = compute_reward(rating)

    # Optimize prompt (learning step)
    base_prompt = optimize_prompt(base_prompt, reward)

    print("Feedback recorded. System updated.\n")
