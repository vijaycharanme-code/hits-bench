from rag.database import db
from core.logging import logger
from typing import List, Dict, Any

def retrieve_documents(query: str, top_k: int = 3) -> List[Dict[str, Any]]:
    """Retrieves relevant documents for a given query."""
    logger.info(f"Retrieving documents for: {query}")

    results = db.query(query_texts=[query], n_results=top_k)

    docs = []
    if results and "documents" in results and results["documents"]:
        for i, doc_group in enumerate(results["documents"]):
            for j, doc in enumerate(doc_group):
                docs.append({
                    "content": doc,
                    "metadata": results["metadatas"][i][j] if results.get("metadatas") else {}
                })
    return docs
