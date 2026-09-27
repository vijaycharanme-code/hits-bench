from typing import List

def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 200) -> List[str]:
    """Simulates splitting text into chunks."""
    if not text:
        return []

    # Very basic dummy chunking for simulation
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunks.append(text[i:i + chunk_size])
    return chunks
