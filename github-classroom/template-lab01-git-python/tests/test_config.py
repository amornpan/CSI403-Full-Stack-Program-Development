"""
Test cases for RAG Configuration
=================================
ใช้สำหรับ auto-grading Lab 01

คะแนน: 30 คะแนน (15 คะแนนต่อ TODO)
"""

import pytest
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from rag_config import OpenSearchConfig, OllamaConfig, RAGConfig


class TestOpenSearchConfig:
    """Test OpenSearchConfig (TODO 1)"""
    
    def test_url_http(self):
        """ทดสอบ URL แบบ HTTP (15 คะแนน)"""
        config = OpenSearchConfig(host="localhost", port=9200, use_ssl=False)
        assert config.url == "http://localhost:9200", f"Expected 'http://localhost:9200', got '{config.url}'"
    
    def test_url_https(self):
        """ทดสอบ URL แบบ HTTPS"""
        config = OpenSearchConfig(host="search.example.com", port=443, use_ssl=True)
        assert config.url == "https://search.example.com:443", f"Got '{config.url}'"
    
    def test_url_custom_port(self):
        """ทดสอบ URL กับ port อื่น"""
        config = OpenSearchConfig(host="192.168.1.100", port=9201, use_ssl=False)
        assert config.url == "http://192.168.1.100:9201"
    
    def test_default_values(self):
        """ทดสอบค่า default"""
        config = OpenSearchConfig()
        assert config.host == "localhost"
        assert config.port == 9200
        assert config.use_ssl == False


class TestOllamaConfig:
    """Test OllamaConfig (TODO 2)"""
    
    def test_generate_url_default(self):
        """ทดสอบ generate_url กับค่า default (15 คะแนน)"""
        config = OllamaConfig()
        expected = "http://localhost:11434/api/generate"
        assert config.generate_url == expected, f"Expected '{expected}', got '{config.generate_url}'"
    
    def test_generate_url_custom(self):
        """ทดสอบ generate_url กับค่าที่กำหนดเอง"""
        config = OllamaConfig(host="ollama.example.com", port=8080)
        expected = "http://ollama.example.com:8080/api/generate"
        assert config.generate_url == expected, f"Got '{config.generate_url}'"
    
    def test_base_url(self):
        """ทดสอบ base_url"""
        config = OllamaConfig(host="localhost", port=11434)
        assert config.base_url == "http://localhost:11434"
    
    def test_default_model(self):
        """ทดสอบ model default"""
        config = OllamaConfig()
        assert config.model == "qwen2.5:7b"


class TestRAGConfig:
    """Test RAGConfig (ไม่มี TODO - แค่ตรวจสอบว่าทำงานได้)"""
    
    def test_rag_config_initialization(self):
        """ทดสอบการสร้าง RAGConfig"""
        config = RAGConfig()
        assert config.opensearch is not None
        assert config.ollama is not None
        assert config.embedding is not None
    
    def test_rag_config_defaults(self):
        """ทดสอบค่า default ของ RAGConfig"""
        config = RAGConfig()
        assert config.chunk_size == 1024
        assert config.top_k == 5


# ==========================================
# รันไฟล์นี้โดยตรงเพื่อทดสอบ
# ==========================================
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
