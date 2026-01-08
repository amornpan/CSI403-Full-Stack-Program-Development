"""
Week 02: RAG Configuration using Dataclasses
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class OpenSearchConfig:
    """OpenSearch connection configuration"""
    host: str = "localhost"
    port: int = 9200
    index_name: str = "documents"
    use_ssl: bool = False
    
    @property
    def url(self) -> str:
        protocol = "https" if self.use_ssl else "http"
        return f"{protocol}://{self.host}:{self.port}"


@dataclass
class OllamaConfig:
    """Ollama LLM configuration"""
    host: str = "localhost"
    port: int = 11434
    model: str = "qwen2.5:7b"
    temperature: float = 0.7
    
    @property
    def url(self) -> str:
        return f"http://{self.host}:{self.port}"
    
    @property
    def generate_url(self) -> str:
        return f"{self.url}/api/generate"


@dataclass
class EmbeddingConfig:
    """Embedding model configuration"""
    model_name: str = "BAAI/bge-m3"
    dimension: int = 1024
    trust_remote_code: bool = True


@dataclass
class RAGConfig:
    """Main RAG system configuration"""
    opensearch: OpenSearchConfig = field(default_factory=OpenSearchConfig)
    ollama: OllamaConfig = field(default_factory=OllamaConfig)
    embedding: EmbeddingConfig = field(default_factory=EmbeddingConfig)
    
    # Chunking settings
    chunk_size: int = 1024
    chunk_overlap: int = 200
    
    # Search settings
    top_k: int = 5
    
    # Paths
    corpus_path: str = "./md_corpus"


if __name__ == "__main__":
    # Create default configuration
    config = RAGConfig()
    
    print("=== RAG Configuration ===")
    print(f"OpenSearch URL: {config.opensearch.url}")
    print(f"Ollama URL: {config.ollama.url}")
    print(f"Model: {config.ollama.model}")
    print(f"Embedding: {config.embedding.model_name}")
    print(f"Chunk size: {config.chunk_size}")
    print(f"Top K: {config.top_k}")
