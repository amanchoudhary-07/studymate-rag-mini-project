# 📘 StudyMate – Retrieval-Augmented Generation (RAG) Mini Project

StudyMate is an end-to-end **Retrieval-Augmented Generation (RAG)** based Question Answering system that allows users to ask questions from their **own study notes (PDF)**.  
The system retrieves relevant content from the uploaded notes and generates answers **strictly based on that content**, reducing hallucinations and improving reliability.

## 🚀 Project Overview

Traditional Large Language Models (LLMs) do not:
- Understand private documents
- Stay limited to a specific syllabus
- Always provide factual answers (hallucination issue)

**StudyMate solves this using RAG** by combining:
- Vector Databases (FAISS)
- Semantic Embeddings
- Local Open-Source LLMs (HuggingFace)

---

## 🧠 What is RAG?

**Retrieval-Augmented Generation (RAG)** enhances LLMs by:
1. Retrieving relevant information from an external knowledge source
2. Passing that information as context to the language model
3. Generating grounded and accurate answers

## System Architecture
PDF Notes
↓
Text Chunking
↓
Embedding Generation
↓
FAISS Vector Database
↓
Semantic Retrieval
↓
Local LLM (HuggingFace)
↓
final Answer

## Project Structure

studymate-rag-mini-project/
│
├── data/
│ └── notes.pdf
│
├── ingest.py # PDF → chunks → embeddings → FAISS DB
├── qa.py # Question answering using RAG
├── requirements.txt
├── README.md
└── venv/

## Installation & seatup 


---

## ⚙️ Installation & Setup

## 1️⃣ Clone the Repository
```bash
git clone <your-repo-url>
cd studymate-rag-mini-project


2️⃣ Create Virtual Environment
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt
pip install sentence-transformers transformers torch

📥 Ingest the PDF (Vector DB Creation)

Place your PDF inside the data/ folder as notes.pdf.

venv/bin/python ingest.py

❓ Run the Question Answering System
venv/bin/python qa.py

## Example question 

What is sales forecasting?
Explain types of sales forecasting.
What is demand forecasting?


