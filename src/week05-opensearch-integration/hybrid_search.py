"""
Week 05: Hybrid Search Demo
Demonstrates keyword, vector, and hybrid search
"""

import random
from opensearch_client import OpenSearchClient


def generate_fake_vector(dimension: int = 1024) -> list:
    """Generate fake vector for demo (will use real embeddings in Week 06)"""
    return [random.uniform(-1, 1) for _ in range(dimension)]


def main():
    print("=" * 50)
    print("Week 05: Hybrid Search Demo")
    print("=" * 50)
    
    # Initialize client
    client = OpenSearchClient()
    
    if not client.is_connected():
        print("❌ OpenSearch not connected!")
        print("   Run: docker-compose up -d")
        return
    
    print("✅ Connected to OpenSearch")
    
    # Create/recreate index
    print("\n--- Setting up index ---")
    client.delete_index()
    client.create_index(dimension=1024)
    print("✅ Index created")
    
    # Sample documents
    documents = [
        {
            "title": "Introduction to RAG",
            "content": "RAG (Retrieval-Augmented Generation) is a technique that combines retrieval and generation. It first retrieves relevant documents, then uses an LLM to generate answers based on that context.",
            "source": "intro.md",
            "chunk_id": 0
        },
        {
            "title": "What are Embeddings",
            "content": "Embeddings are numerical representations of text. They convert words and sentences into vectors that capture semantic meaning. Similar texts have similar vectors.",
            "source": "embeddings.md",
            "chunk_id": 0
        },
        {
            "title": "Vector Database",
            "content": "OpenSearch is a distributed search and analytics engine. It supports vector search using k-NN algorithm, enabling semantic similarity search.",
            "source": "vectordb.md",
            "chunk_id": 0
        },
        {
            "title": "Local LLM with Ollama",
            "content": "Ollama allows running large language models locally. Popular models include Llama, Mistral, and Qwen. No API key required, data stays private.",
            "source": "ollama.md",
            "chunk_id": 0
        },
        {
            "title": "Hybrid Search",
            "content": "Hybrid search combines keyword search (BM25) with vector search. This approach leverages the strengths of both methods for better results.",
            "source": "hybrid.md",
            "chunk_id": 0
        }
    ]
    
    # Add fake vectors
    for doc in documents:
        doc["content_vector"] = generate_fake_vector()
    
    # Index documents
    print("\n--- Indexing documents ---")
    count = client.bulk_index(documents)
    print(f"✅ Indexed {count} documents")
    
    # Test keyword search
    print("\n--- Keyword Search ---")
    query = "RAG"
    results = client.search_keyword(query, top_k=3)
    print(f"Query: '{query}'")
    for r in results:
        print(f"  [{r['score']:.2f}] {r['title']}")
    
    # Test vector search (with fake vector)
    print("\n--- Vector Search ---")
    fake_query_vector = generate_fake_vector()
    results = client.search_vector(fake_query_vector, top_k=3)
    print(f"Query: [vector...]")
    for r in results:
        print(f"  [{r['score']:.2f}] {r['title']}")
    
    # Note about hybrid search
    print("\n--- Hybrid Search ---")
    print("⚠️ Hybrid search requires the search pipeline.")
    print("   Will be tested with real embeddings in Week 06.")
    
    print("\n" + "=" * 50)
    print("✅ Week 05 completed!")
    print("=" * 50)


if __name__ == "__main__":
    main()
