"""
Week 06: Embedding Model Wrapper
Local embedding using HuggingFace bge-m3
"""

from typing import List, Optional
from dataclasses import dataclass


@dataclass
class EmbeddingConfig:
    model_name: str = "BAAI/bge-m3"
    dimension: int = 1024
    trust_remote_code: bool = True
    device: str = "cpu"  # or "cuda"


class EmbeddingModel:
    """
    Wrapper for HuggingFace embedding model
    Uses bge-m3 for multilingual support (Thai/English)
    """
    
    def __init__(self, config: Optional[EmbeddingConfig] = None):
        self.config = config or EmbeddingConfig()
        self._model = None
    
    def _load_model(self):
        """Lazy load model"""
        if self._model is None:
            try:
                from llama_index.embeddings.huggingface import HuggingFaceEmbedding
                
                print(f"Loading embedding model: {self.config.model_name}")
                self._model = HuggingFaceEmbedding(
                    model_name=self.config.model_name,
                    trust_remote_code=self.config.trust_remote_code
                )
                print("✅ Model loaded")
            except ImportError:
                print("⚠️ llama-index not installed, using sentence-transformers")
                from sentence_transformers import SentenceTransformer
                self._model = SentenceTransformer(self.config.model_name)
    
    def embed_text(self, text: str) -> List[float]:
        """Embed a single text"""
        self._load_model()
        
        if hasattr(self._model, 'get_text_embedding'):
            # llama-index style
            return self._model.get_text_embedding(text)
        else:
            # sentence-transformers style
            return self._model.encode(text).tolist()
    
    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        """Embed multiple texts"""
        self._load_model()
        
        if hasattr(self._model, 'get_text_embedding_batch'):
            return self._model.get_text_embedding_batch(texts)
        else:
            return self._model.encode(texts).tolist()
    
    @property
    def dimension(self) -> int:
        return self.config.dimension


# Singleton instance
_embedding_model: Optional[EmbeddingModel] = None


def get_embedding_model() -> EmbeddingModel:
    """Get singleton embedding model instance"""
    global _embedding_model
    if _embedding_model is None:
        _embedding_model = EmbeddingModel()
    return _embedding_model


if __name__ == "__main__":
    # Test embedding
    print("=" * 50)
    print("Testing Embedding Model")
    print("=" * 50)
    
    model = get_embedding_model()
    
    # Test texts
    texts = [
        "What is RAG?",
        "RAG คืออะไร?",
        "Embeddings convert text to vectors"
    ]
    
    for text in texts:
        vector = model.embed_text(text)
        print(f"\n'{text}'")
        print(f"  Dimension: {len(vector)}")
        print(f"  First 5: {vector[:5]}")
