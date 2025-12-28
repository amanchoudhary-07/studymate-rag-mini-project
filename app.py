from flask import Flask, render_template, request, jsonify
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import pipeline
import json

app = Flask(__name__)

# Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Vector DB
vector_db = FAISS.load_local(
    "vector_db",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vector_db.as_retriever(search_kwargs={"k": 3})

# Local LLM
qa_model = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_new_tokens=300
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.json.get("question")

    docs = retriever.invoke(question)
    if not docs:
        return jsonify({"answer": "Answer not found in the provided notes."})

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
Answer ONLY from the context below.
If not found, say: Answer not found in the provided notes.

Context:
{context}

Question:
{question}
"""

    result = qa_model(prompt)[0]["generated_text"]
    return jsonify({"answer": result})

@app.route("/feedback", methods=["POST"])
def feedback():
    data = request.json

    record = {
        "question": data["question"],
        "answer": data["answer"],
        "helpful": data["helpful"],
        "rating": int(data["rating"])
    }

    with open("feedback_store.json", "a") as f:
        f.write(json.dumps(record) + "\n")

    return jsonify({"status": "saved"})

if __name__ == "__main__":
    app.run(debug=True)
