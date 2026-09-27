from pathlib import Path
from core.logging import logger

def ingest_document(file_path: str) -> bool:
    """Simulates ingesting a document into the RAG system."""
    path = Path(file_path)
    if not path.exists():
        logger.error(f"Cannot ingest, file not found: {file_path}")
        return False

    logger.info(f"Ingesting document: {file_path}")
    # Simulate extraction -> chunking -> embedding -> storing
    return True
