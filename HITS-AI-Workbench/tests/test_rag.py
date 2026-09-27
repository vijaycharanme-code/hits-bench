import pytest
from rag.chunking import chunk_text
from rag.embeddings import generate_embeddings

def test_chunking():
    text = "A" * 2000
    chunks = chunk_text(text, chunk_size=1000, overlap=200)
    assert len(chunks) > 1
    assert len(chunks[0]) == 1000

def test_embeddings():
    emb = generate_embeddings(["test"])
    assert len(emb) == 1
    assert len(emb[0]) == 384
