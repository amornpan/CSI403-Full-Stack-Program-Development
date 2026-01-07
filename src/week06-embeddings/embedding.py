"""
Week 06: Main Embedding Script
Index documents with embeddings to OpenSearch
"""

import sys
import os

# Add parent directory for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'week05-opensearch-integration'))

from typing import List
from embedding_model import get_embedding_model
from document_processor import DocumentProcessor, Chunk
from opensearch_client import OpenSearchClient, OpenSearchConfig


def create_sample_documents(directory: str):
    """Create sample markdown documents"""
    os.makedirs(directory, exist_ok=True)
    
    documents = {
        "01-rag-intro.md": """# Introduction to RAG

RAG (Retrieval-Augmented Generation) is a technique that enhances Large Language Models 
by providing them with relevant context from external knowledge sources.

## Why RAG?

Traditional LLMs have limitations:
- Knowledge cutoff date
- No access to private data
- Can hallucinate

RAG solves these by retrieving relevant documents before generating answers.
""",
        "02-embeddings.md": """# Understanding Embeddings

Embeddings are numerical representations of text that capture semantic meaning.

## How Embeddings Work

Text is converted into high-dimensional vectors (e.g., 1024 dimensions).
Similar texts have similar vectors, enabling semantic search.

## Popular Models

- BAAI/bge-m3: Multilingual, 1024 dimensions
- OpenAI ada-002: 1536 dimensions (API required)
- sentence-transformers: Various sizes
""",
        "03-opensearch.md": """# OpenSearch Vector Database

OpenSearch is a distributed search engine that supports vector search.

## Key Features

- k-NN search using HNSW algorithm
- Hybrid search combining BM25 and vectors
- Scalable and self-hosted

## Setup

Run OpenSearch with Docker:
```bash
docker-compose up -d
```
""",
        "04-ollama.md": """# Local LLM with Ollama

Ollama allows running LLMs locally without API keys.

## Installation

Download from https://ollama.ai and install.

## Models

- qwen2.5:7b - Good for Thai/English
- llama3.2 - Fast and capable
- mistral - Efficient

## Usage

```bash
ollama pull qwen2.5:7b
ollama run qwen2.5:7b
```
""",
        "05-thai-rag.md": """# การสร้างระบบ RAG ภาษาไทย

ระบบ RAG สามารถทำงานกับภาษาไทยได้ดี โดยใช้ embedding model ที่รองรับหลายภาษา

## ข้อดีของ Local LLM

- ไม่ต้องเสียค่า API
- ข้อมูลอยู่ในเครื่อง ปลอดภัย
- ทำงานได้แม้ไม่มี Internet

## Model ที่แนะนำ

- BAAI/bge-m3 สำหรับ embedding (รองรับภาษาไทย)
- qwen2.5:7b สำหรับ LLM (ตอบภาษาไทยได้)
"""
    }
    
    for filename, content in documents.items():
        filepath = os.path.join(directory, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
    
    return len(documents)


def index_documents(chunks: List[Chunk], client: OpenSearchClient, embed_model):
    """Index chunks with embeddings"""
    documents = []
    
    for chunk in chunks:
        # Create embedding
        vector = embed_model.embed_text(chunk.content)
        
        doc = {
            "content": chunk.content,
            "content_vector": vector,
            "title": chunk.title,
            "source": chunk.source,
            "chunk_id": chunk.chunk_id
        }
        documents.append(doc)
    
    # Bulk index
    count = client.bulk_index(documents)
    return count


def main():
    print("=" * 60)
    print("Week 06: Document Embedding & Indexing")
    print("=" * 60)
    
    # Configuration
    corpus_dir = "./md_corpus"
    
    # Create sample documents
    print("\n--- Creating sample documents ---")
    num_docs = create_sample_documents(corpus_dir)
    print(f"✅ Created {num_docs} sample documents in {corpus_dir}")
    
    # Initialize components
    print("\n--- Initializing components ---")
    
    # OpenSearch client
    client = OpenSearchClient()
    if not client.is_connected():
        print("❌ OpenSearch not connected!")
        print("   Run: cd ../week03-docker-opensearch && docker-compose up -d")
        return
    print("✅ OpenSearch connected")
    
    # Embedding model
    print("Loading embedding model (this may take a while first time)...")
    embed_model = get_embedding_model()
    print(f"✅ Embedding model loaded (dim={embed_model.dimension})")
    
    # Document processor
    processor = DocumentProcessor()
    
    # Reset index
    print("\n--- Setting up index ---")
    client.delete_index()
    client.create_index(dimension=embed_model.dimension)
    print("✅ Index created")
    
    # Process documents
    print("\n--- Processing documents ---")
    chunks = processor.process_directory(corpus_dir)
    print(f"Total chunks: {len(chunks)}")
    
    # Index with embeddings
    print("\n--- Indexing with embeddings ---")
    indexed = index_documents(chunks, client, embed_model)
    print(f"✅ Indexed {indexed} chunks")
    
    # Verify
    print("\n--- Verification ---")
    count = client.count_documents()
    print(f"Documents in index: {count}")
    
    # Test search
    print("\n--- Test Search ---")
    query = "RAG คืออะไร"
    print(f"Query: '{query}'")
    
    query_vector = embed_model.embed_text(query)
    results = client.search_vector(query_vector, top_k=3)
    
    for r in results:
        print(f"  [{r['score']:.4f}] {r['title']}")
        print(f"           {r['content'][:80]}...")
    
    print("\n" + "=" * 60)
    print("✅ Week 06 completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
