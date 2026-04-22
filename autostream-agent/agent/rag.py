from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document

def load_knowledge():
    docs = [
        "Basic Plan: $29/month, 10 videos per month, 720p resolution",
        "Pro Plan: $79/month, unlimited videos, 4K resolution, AI captions",
        "No refunds after 7 days",
        "24/7 support available only on Pro plan"
    ]

    documents = [Document(page_content=d) for d in docs]

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    db = FAISS.from_documents(documents, embeddings)
    return db


def retrieve_answer(query, db):
    results = db.similarity_search(query, k=2)
    return " ".join([r.page_content for r in results])