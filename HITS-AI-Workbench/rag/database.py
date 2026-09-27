import chromadb
from chromadb.config import Settings
from core.config import DB_DIR
from core.logging import logger

class VectorDB:
    def __init__(self):
        try:
            self.client = chromadb.PersistentClient(path=str(DB_DIR / "chroma"))
            self.collection = self.client.get_or_create_collection(name="documents")
            logger.info("ChromaDB initialized.")
        except Exception as e:
            logger.error(f"Failed to initialize ChromaDB: {e}")
            self.client = None
            self.collection = None

    def add_texts(self, texts: list, ids: list, metadatas: list = None):
        if not self.collection:
            return False
        try:
            self.collection.add(
                documents=texts,
                ids=ids,
                metadatas=metadatas
            )
            return True
        except Exception as e:
            logger.error(f"Error adding to ChromaDB: {e}")
            return False

    def query(self, query_texts: list, n_results: int = 3):
        if not self.collection:
            return {"documents": [], "metadatas": []}
        try:
            results = self.collection.query(
                query_texts=query_texts,
                n_results=n_results
            )
            return results
        except Exception as e:
            logger.error(f"Error querying ChromaDB: {e}")
            return {"documents": [], "metadatas": []}

# Global DB instance
db = VectorDB()
