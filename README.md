# 📘 StudyMate – RAG + RLHF Based Intelligent Study Assistant

StudyMate is an end-to-end **Retrieval-Augmented Generation (RAG)** based Question Answering system that allows users to ask questions from their own study notes (PDF files). The system retrieves relevant content from the uploaded notes and generates answers strictly based on that content, reducing hallucinations and improving reliability.

The project is further extended with **Reinforcement Learning from Human Feedback (RLHF)** to continuously improve answer quality, clarity, and alignment with user expectations.

---

## 🚀 Project Overview
Traditional Large Language Models (LLMs):
* Do not understand private documents
* Cannot stay limited to a specific syllabus
* May generate hallucinated or irrelevant answers

**StudyMate** solves these problems using RAG + RLHF, combining:
* **Vector Databases** (FAISS)
* **Semantic Embeddings**
* **Local Open-Source LLMs** (HuggingFace)
* **Human feedback–driven optimization**

---

## 🧠 What is Retrieval-Augmented Generation (RAG)?
RAG improves LLM responses by:
1. **Retrieving** relevant information from a knowledge source (PDF notes).
2. **Supplying** only that information as context to the model.
3. **Generating** accurate, grounded answers.

### 📐 System Architecture
`PDF Notes` → `Text Chunking` → `Embedding Generation` → `FAISS Vector Database` → `Semantic Retrieval` → `Local LLM (HuggingFace)` → `Answer`

---

## 📂 Project Structure
```text
studymate-rag-mini-project/
│
├── data/
│   └── notes.pdf
├── ingest.py           # PDF → chunks → embeddings → FAISS DB
├── qa.py               # RAG-based Q&A + RLHF loop
├── feedback.py         # Human feedback collection
├── reward_model.py     # Reward computation logic
├── rlhf_loop.py        # Prompt optimization logic
├── feedback_store.json # Stored human feedback
├── requirements.txt
├── README.md
└── venv/

⚙️ Installation & Setup

1️⃣ Clone the Repository
git clone <your-repo-link>
cd studymate-rag-mini-project

2️⃣ Create Virtual Environment
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt
pip install sentence-transformers transformers torch

📥 PDF Ingestion (Vector Database Creation)
Place your study PDF inside the data/ folder as: data/notes.pdf

python ingest.py

✔ This step:

Reads the PDF

Splits text into chunks

Generates embeddings

Stores them in FAISS vector database

❓ Run the Question Answering System
python qa.py

You can now ask questions related only to your PDF content.

🧪 Example Questions
What is sales forecasting?
Explain types of sales forecasting.
What is demand forecasting?

🧠 RLHF Extension (Human Feedback Learning)
🔍 Why RLHF?
While RAG ensures correct answers, it does not guarantee:

Clarity

Conciseness

Human satisfaction

🔁 RLHF Workflow
Answer Generation (RAG): The system generates an answer using retrieved PDF context.

Human Feedback Collection: The user provides a rating (1–5). Feedback is stored in feedback_store.json.

Reward Modeling: Ratings are converted into numerical rewards.

Prompt Optimization: Low reward triggers prompt refinement; high reward retains the current strategy.

📊 Industry Mapping

Industry Concept, This Project Implementation
Human Labelers, Students / Users
Reward Model, Rule-based logic
PPO Fine-tuning, Prompt optimization logic
Preference Dataset, feedback_store.json

🎓 Learning Outcomes
Why RAG is required for private data.

How Vector Databases (FAISS) manage semantic search.

How Embeddings capture meaning.

How RLHF aligns AI behavior with human intent.






