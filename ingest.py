from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv(".env")

print("Starting ingestion...")

# Load PDF
loader = PyPDFLoader("data/notes.pdf")
documents = loader.load()
print(f"Loaded {len(documents)} pages")

# Split text
splitter = RecursiveCharacterTextSplitter(
    chunk_size=600,
    chunk_overlap=100
)
chunks = splitter.split_documents(documents)
print(f"Created {len(chunks)} chunks")

# HuggingFace embeddings (FREE)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
print("HuggingFace embeddings initialized")

# Store in FAISS
vector_db = FAISS.from_documents(chunks, embeddings)
vector_db.save_local("vector_db")

print("Ingestion completed. Vector DB created.")

