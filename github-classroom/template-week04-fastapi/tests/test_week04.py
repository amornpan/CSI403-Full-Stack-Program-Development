"""
Test cases for Week 04: FastAPI
===============================
ใช้สำหรับ auto-grading

คะแนน: 80 คะแนน (ไม่รวม screenshots และ README)
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from fastapi.testclient import TestClient


class TestPydanticModels:
    """Test Pydantic Models (30 คะแนน)"""
    
    def test_search_request_valid(self):
        """ทดสอบ SearchRequest ที่ถูกต้อง (10 คะแนน)"""
        from models import SearchRequest
        
        req = SearchRequest(query="test", top_k=5)
        assert req.query == "test"
        assert req.top_k == 5
    
    def test_search_request_default_top_k(self):
        """ทดสอบ SearchRequest default top_k"""
        from models import SearchRequest
        
        req = SearchRequest(query="test")
        assert req.top_k == 5  # default value
    
    def test_search_result_valid(self):
        """ทดสอบ SearchResult (10 คะแนน)"""
        from models import SearchResult
        
        result = SearchResult(
            title="Test",
            content="Content",
            score=0.95,
            source="test.md"
        )
        assert result.title == "Test"
        assert result.score == 0.95
    
    def test_search_response_valid(self):
        """ทดสอบ SearchResponse (10 คะแนน)"""
        from models import SearchResponse, SearchResult
        
        result = SearchResult(title="Test", content="Content", score=0.9)
        resp = SearchResponse(
            query="test",
            results=[result],
            total=1,
            took_ms=10.5
        )
        assert resp.query == "test"
        assert resp.total == 1
        assert len(resp.results) == 1


class TestAPIEndpoints:
    """Test API Endpoints (50 คะแนน)"""
    
    @pytest.fixture
    def client(self):
        """Create test client"""
        from api import app
        return TestClient(app)
    
    def test_root(self, client):
        """ทดสอบ root endpoint"""
        response = client.get("/")
        assert response.status_code == 200
        assert "message" in response.json()
    
    def test_health(self, client):
        """ทดสอบ GET /health (10 คะแนน)"""
        response = client.get("/health")
        assert response.status_code == 200
        
        data = response.json()
        assert data["status"] == "healthy"
        assert "timestamp" in data
        assert data["version"] == "1.0.0"
    
    def test_list_documents(self, client):
        """ทดสอบ GET /documents (10 คะแนน)"""
        response = client.get("/documents")
        assert response.status_code == 200
        
        data = response.json()
        assert "documents" in data
        assert "total" in data
        assert isinstance(data["documents"], list)
    
    def test_create_document(self, client):
        """ทดสอบ POST /documents (10 คะแนน)"""
        response = client.post(
            "/documents",
            json={
                "title": "Test Document",
                "content": "Test content",
                "source": "test.md"
            }
        )
        assert response.status_code == 201
        
        data = response.json()
        assert "document" in data or "id" in data
    
    def test_search(self, client):
        """ทดสอบ POST /search (10 คะแนน)"""
        response = client.post(
            "/search",
            json={"query": "RAG", "top_k": 5}
        )
        assert response.status_code == 200
        
        data = response.json()
        assert "query" in data
        assert "results" in data
        assert "total" in data
    
    def test_delete_document_not_found(self, client):
        """ทดสอบ DELETE /documents/{id} not found (10 คะแนน)"""
        response = client.delete("/documents/nonexistent")
        assert response.status_code == 404


class TestValidation:
    """Test input validation"""
    
    @pytest.fixture
    def client(self):
        from api import app
        return TestClient(app)
    
    def test_search_empty_query(self, client):
        """ทดสอบ search กับ empty query"""
        response = client.post(
            "/search",
            json={"query": "", "top_k": 5}
        )
        # Should return 422 (validation error) if min_length is set
        assert response.status_code in [200, 422]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
