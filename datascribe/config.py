import os
from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
CHROMA_DIR = "chroma_db"
COLLECTION_NAME = "datascribe_codebase"
SUPPORTED_EXTENSIONS = {".py",".sql",".md"}
