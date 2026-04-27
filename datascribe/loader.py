from pathlib import Path
from langchain_core.documents import Document
from datascribe.config import SUPPORTED_EXTENSIONS

def load_repository_files(target_dir):
    docs=[]
    for file in Path(target_dir).rglob("*"):
        if file.is_file() and file.suffix in SUPPORTED_EXTENSIONS:
            docs.append(Document(
                page_content=file.read_text(encoding="utf-8", errors="ignore"),
                metadata={"source": str(file)}
            ))
    return docs
