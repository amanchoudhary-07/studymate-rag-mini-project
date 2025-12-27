from flask import Flask, render_template, request, jsonify
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import pipeline

app = Flask(__name__)

# Load embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load vector DB
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
    data = request.get_json()
    question = data.get("question")

    docs = retriever.invoke(question)

    if not docs:
        return jsonify({"answer": "Answer not found in the provided notes."})

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
Answer the question ONLY using the context below.
If not found, say: Answer not found in the provided notes.

Context:
{context}

Question:
{question}
"""

    result = qa_model(prompt)[0]["generated_text"]

    return jsonify({"answer": result})

if __name__ == "__main__":
    app.run(debug=True)
