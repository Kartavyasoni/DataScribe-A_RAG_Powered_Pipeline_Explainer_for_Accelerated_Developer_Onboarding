from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from datascribe.config import CHROMA_DIR, COLLECTION_NAME

def build_vector_store(chunks):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=CHROMA_DIR,
        collection_name=COLLECTION_NAME
    )
