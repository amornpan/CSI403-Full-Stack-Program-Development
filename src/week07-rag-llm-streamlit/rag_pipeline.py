"""
Week 07: RAG Pipeline
Complete Retrieval-Augmented Generation pipeline
"""

import sys
import os
from typing import List, Dict, Optional
from dataclasses import dataclass

# Add paths for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'week05-opensearch-integration'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'week06-embeddings'))

from opensearch_client import OpenSearchClient
from embedding_model import get_embedding_model
from ollama_client import get_ollama_client


@dataclass
class RAGConfig:
    top_k: int = 5
    max_context_length: int = 3000
    model: str = "qwen2.5:7b"


# Prompt template
PROMPT_TEMPLATE = """คุณเป็นผู้ช่วยที่ชาญฉลาดและเป็นมิตร ใช้ข้อมูลบริบทด้านล่างในการตอบคำถาม
ถ้าไม่พบข้อมูลในบริบท ให้ตอบว่า "ฉันไม่พบข้อมูลที่เกี่ยวข้อง"
ตอบเป็นภาษาเดียวกับคำถาม

บริบท:
{context}

คำถาม: {question}

คำตอบ:"""


class RAGPipeline:
    """Complete RAG pipeline"""
    
    def __init__(self, config: Optional[RAGConfig] = None):
        self.config = config or RAGConfig()
        
        # Initialize components
        self.opensearch = OpenSearchClient()
        self.embed_model = None  # Lazy load
        self.llm = None  # Lazy load
    
    def _get_embed_model(self):
        if self.embed_model is None:
            self.embed_model = get_embedding_model()
        return self.embed_model
    
    def _get_llm(self):
        if self.llm is None:
            self.llm = get_ollama_client()
        return self.llm
    
    def check_components(self) -> Dict[str, bool]:
        """Check if all components are available"""
        return {
            "opensearch": self.opensearch.is_connected(),
            "ollama": self._get_llm().is_available()
        }
    
    def retrieve(self, query: str) -> List[Dict]:
        """Retrieve relevant documents"""
        # Create query embedding
        embed_model = self._get_embed_model()
        query_vector = embed_model.embed_text(query)
        
        # Search
        results = self.opensearch.search_vector(
            vector=query_vector,
            top_k=self.config.top_k
        )
        
        return results
    
    def format_context(self, documents: List[Dict]) -> str:
        """Format documents as context"""
        context_parts = []
        total_length = 0
        
        for i, doc in enumerate(documents, 1):
            content = doc.get("content", "")
            title = doc.get("title", "Unknown")
            
            part = f"[{i}. {title}]\n{content}\n"
            
            if total_length + len(part) > self.config.max_context_length:
                break
            
            context_parts.append(part)
            total_length += len(part)
        
        return "\n".join(context_parts)
    
    def generate(self, query: str, context: str) -> str:
        """Generate answer using LLM"""
        prompt = PROMPT_TEMPLATE.format(
            context=context,
            question=query
        )
        
        llm = self._get_llm()
        response = llm.generate(prompt)
        
        return response
    
    def query(self, question: str) -> Dict:
        """Complete RAG query"""
        # 1. Retrieve
        documents = self.retrieve(question)
        
        # 2. Format context
        context = self.format_context(documents)
        
        # 3. Generate
        answer = self.generate(question, context)
        
        return {
            "question": question,
            "answer": answer,
            "sources": documents,
            "model": self.config.model
        }


# Singleton
_rag_pipeline: Optional[RAGPipeline] = None


def get_rag_pipeline() -> RAGPipeline:
    global _rag_pipeline
    if _rag_pipeline is None:
        _rag_pipeline = RAGPipeline()
    return _rag_pipeline


if __name__ == "__main__":
    print("=" * 60)
    print("Testing RAG Pipeline")
    print("=" * 60)
    
    pipeline = get_rag_pipeline()
    
    # Check components
    print("\n--- Component Check ---")
    status = pipeline.check_components()
    for component, available in status.items():
        icon = "✅" if available else "❌"
        print(f"  {icon} {component}")
    
    if not all(status.values()):
        print("\n⚠️ Some components not available")
        exit(1)
    
    # Test query
    print("\n--- Test Query ---")
    question = "RAG คืออะไร?"
    print(f"Question: {question}")
    
    result = pipeline.query(question)
    
    print(f"\nAnswer: {result['answer']}")
    print(f"\nSources ({len(result['sources'])}):")
    for src in result['sources']:
        print(f"  - {src.get('title', 'Unknown')}")
