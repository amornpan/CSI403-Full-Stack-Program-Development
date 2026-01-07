"""
Week 02: Main Entry Point
Demonstrates Python fundamentals for RAG
"""

from document import Document, MarkdownDocument
from rag_config import RAGConfig
from utils import chunk_text, clean_text, format_context


def main():
    print("=" * 50)
    print("Week 02: Python Fundamentals for RAG")
    print("=" * 50)
    
    # 1. Create configuration
    print("\n1. Configuration:")
    config = RAGConfig()
    print(f"   OpenSearch: {config.opensearch.url}")
    print(f"   Ollama: {config.ollama.url}")
    print(f"   Model: {config.ollama.model}")
    
    # 2. Create documents
    print("\n2. Documents:")
    docs = [
        Document("RAG Introduction", 
                 "RAG combines retrieval and generation for accurate answers."),
        Document("Embeddings", 
                 "Embeddings convert text to vectors for similarity search."),
        Document("Vector Database", 
                 "OpenSearch stores vectors for fast retrieval.")
    ]
    
    for doc in docs:
        print(f"   - {doc}")
    
    # 3. Chunking
    print("\n3. Chunking:")
    long_text = "This is a long document. " * 50
    chunks = list(chunk_text(long_text, chunk_size=100, overlap=20))
    print(f"   Original: {len(long_text)} chars")
    print(f"   Chunks: {len(chunks)}")
    
    # 4. Format context
    print("\n4. Context Formatting:")
    sample_docs = [
        {"content": "Document 1 content about RAG"},
        {"content": "Document 2 content about LLM"},
        {"content": "Document 3 content about embeddings"}
    ]
    context = format_context(sample_docs)
    print(f"   Context length: {len(context)} chars")
    
    print("\n" + "=" * 50)
    print("✅ Python fundamentals completed!")
    print("=" * 50)


if __name__ == "__main__":
    main()
