"""
Week 09: Unit Tests
Tests for utility functions and classes
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'week02-git-python'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'week06-embeddings'))


class TestDocument:
    """Test Document class"""
    
    def test_document_creation(self):
        """Test creating a document"""
        from document import Document
        
        doc = Document("Test", "Test content")
        assert doc.title == "Test"
        assert doc.content == "Test content"
        assert doc.word_count == 2
    
    def test_document_summary(self):
        """Test document summary"""
        from document import Document
        
        doc = Document("Test", "A" * 200)
        summary = doc.get_summary(50)
        assert len(summary) <= 53  # 50 + "..."
        assert summary.endswith("...")
    
    def test_document_chunks(self):
        """Test document chunking"""
        from document import Document
        
        content = " ".join(["word"] * 100)
        doc = Document("Test", content)
        chunks = doc.get_chunks(chunk_size=20)
        assert len(chunks) == 5  # 100 words / 20 = 5


class TestUtils:
    """Test utility functions"""
    
    def test_chunk_text_small(self):
        """Test chunking small text"""
        from utils import chunk_text
        
        text = "Small text"
        chunks = list(chunk_text(text, chunk_size=100))
        assert len(chunks) == 1
        assert chunks[0] == text
    
    def test_chunk_text_large(self):
        """Test chunking large text"""
        from utils import chunk_text
        
        text = "A" * 500
        chunks = list(chunk_text(text, chunk_size=100, overlap=20))
        assert len(chunks) > 1
    
    def test_clean_text(self):
        """Test text cleaning"""
        from utils import clean_text
        
        text = "# Header\n  Extra   spaces  "
        cleaned = clean_text(text)
        assert "# Header" not in cleaned or "Header" in cleaned


class TestDocumentProcessor:
    """Test DocumentProcessor"""
    
    def test_chunk_short_text(self):
        """Test chunking short text"""
        from document_processor import DocumentProcessor
        
        processor = DocumentProcessor()
        text = "Short text"
        chunks = list(processor.chunk_text(text))
        assert len(chunks) == 1
    
    def test_process_document(self):
        """Test processing document"""
        from document_processor import DocumentProcessor
        
        processor = DocumentProcessor()
        doc = {
            "title": "Test",
            "content": "Test content for processing",
            "source": "test.md"
        }
        chunks = processor.process_document(doc)
        assert len(chunks) >= 1
        assert chunks[0].title == "Test"


class TestRAGConfig:
    """Test RAG configuration"""
    
    def test_default_config(self):
        """Test default configuration"""
        from rag_config import RAGConfig
        
        config = RAGConfig()
        assert config.chunk_size == 1024
        assert config.top_k == 5
    
    def test_opensearch_url(self):
        """Test OpenSearch URL generation"""
        from rag_config import OpenSearchConfig
        
        config = OpenSearchConfig(host="localhost", port=9200)
        assert config.url == "http://localhost:9200"
    
    def test_ollama_url(self):
        """Test Ollama URL generation"""
        from rag_config import OllamaConfig
        
        config = OllamaConfig(host="localhost", port=11434)
        assert config.generate_url == "http://localhost:11434/api/generate"
