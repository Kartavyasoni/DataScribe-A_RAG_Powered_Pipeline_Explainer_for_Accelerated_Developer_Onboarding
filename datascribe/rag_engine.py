from langchain_google_genai import ChatGoogleGenerativeAI
from datascribe.loader import load_repository_files
from datascribe.chunker import chunk_documents
from datascribe.vector_store import build_vector_store
from datascribe.prompts import PERSONA_PROMPTS
from datascribe.config import GOOGLE_API_KEY, GEMINI_MODEL

class DataScribeRAG:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model=GEMINI_MODEL,
            google_api_key=GOOGLE_API_KEY
        )
        self.vector_store=None

    def ingest(self, target_dir):
        docs = load_repository_files(target_dir)
        chunks = chunk_documents(docs)
        self.vector_store = build_vector_store(chunks)

    def explain(self, query, persona):
        docs = self.vector_store.similarity_search(query, k=5)
        context = "\n".join([d.page_content for d in docs])
        prompt = f"{PERSONA_PROMPTS[persona]}\n\nQuery:{query}\n\nContext:{context}"
        response = self.llm.invoke(prompt)
        return response.content
