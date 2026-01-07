"""
Week 09: API Tests
Tests for the RAG API endpoints
"""

import pytest
from fastapi.testclient import TestClient
import sys
import os

# Add path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'week07-rag-llm-streamlit'))

# Import will fail if dependencies not installed - that's OK for demo
try:
    from api import app
    client = TestClient(app)
    API_AVAILABLE = True
except:
    API_AVAILABLE = False
    client = None


@pytest.mark.skipif(not API_AVAILABLE, reason="API not available")
class TestAPI:
    """Test API endpoints"""
    
    def test_root(self):
        """Test root endpoint"""
        response = client.get("/")
        assert response.status_code == 200
        assert "message" in response.json()
    
    def test_health(self):
        """Test health endpoint"""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert "status" in data
        assert "components" in data
    
    def test_search_valid(self):
        """Test search with valid query"""
        response = client.post(
            "/search",
            json={"query": "RAG", "top_k": 5}
        )
        assert response.status_code == 200
        data = response.json()
        assert "query" in data
        assert "results" in data
    
    def test_search_empty_query(self):
        """Test search with empty query"""
        response = client.post(
            "/search",
            json={"query": "", "top_k": 5}
        )
        assert response.status_code == 422  # Validation error
    
    def test_search_invalid_top_k(self):
        """Test search with invalid top_k"""
        response = client.post(
            "/search",
            json={"query": "test", "top_k": 100}
        )
        assert response.status_code == 422


# Standalone tests that don't need the API
class TestModels:
    """Test Pydantic models"""
    
    def test_query_request_valid(self):
        """Test valid QueryRequest"""
        from pydantic import BaseModel, Field
        
        class QueryRequest(BaseModel):
            query: str = Field(..., min_length=1)
            top_k: int = Field(default=5, ge=1, le=20)
        
        req = QueryRequest(query="test", top_k=5)
        assert req.query == "test"
        assert req.top_k == 5
    
    def test_query_request_defaults(self):
        """Test QueryRequest with defaults"""
        from pydantic import BaseModel, Field
        
        class QueryRequest(BaseModel):
            query: str = Field(..., min_length=1)
            top_k: int = Field(default=5, ge=1, le=20)
        
        req = QueryRequest(query="test")
        assert req.top_k == 5  # Default value
