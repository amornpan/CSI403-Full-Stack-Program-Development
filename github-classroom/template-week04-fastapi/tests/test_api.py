"""
Test cases for FastAPI Endpoints
================================
ใช้สำหรับ auto-grading Week 04

คะแนน: 50 คะแนน
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from fastapi.testclient import TestClient

# Import app
try:
    from api import app
    client = TestClient(app)
    API_AVAILABLE = True
except Exception as e:
    API_AVAILABLE = False
    client = None
    print(f"Warning: Could not import API: {e}")


@pytest.mark.skipif(not API_AVAILABLE, reason="API not available")
class TestHealthEndpoint:
    """Test GET /health endpoint (TODO 1 - 10 คะแนน)"""
    
    def test_health_returns_200(self):
        """ทดสอบว่า /health return 200"""
        response = client.get("/health")
        assert response.status_code == 200
    
    def test_health_has_status(self):
        """ทดสอบว่า response มี status"""
        response = client.get("/health")
        data = response.json()
        assert "status" in data
        assert data["status"] == "healthy"
    
    def test_health_has_timestamp(self):
        """ทดสอบว่า response มี timestamp"""
        response = client.get("/health")
        data = response.json()
        assert "timestamp" in data
    
    def test_health_has_version(self):
        """ทดสอบว่า response มี version"""
        response = client.get("/health")
        data = response.json()
        assert "version" in data


@pytest.mark.skipif(not API_AVAILABLE, reason="API not available")
class TestListDocuments:
    """Test GET /documents endpoint (TODO 2 - 10 คะแนน)"""
    
    def test_list_returns_200(self):
        """ทดสอบว่า /documents return 200"""
        response = client.get("/documents")
        assert response.status_code == 200
    
    def test_list_returns_array(self):
        """ทดสอบว่า response เป็น array"""
        response = client.get("/documents")
        data = response.json()
        assert isinstance(data, list)
    
    def test_list_has_initial_documents(self):
        """ทดสอบว่ามี documents เริ่มต้น"""
        response = client.get("/documents")
        data = response.json()
        assert len(data) >= 2  # มี 2 documents เริ่มต้น


@pytest.mark.skipif(not API_AVAILABLE, reason="API not available")
class TestCreateDocument:
    """Test POST /documents endpoint (TODO 3 - 10 คะแนน)"""
    
    def test_create_returns_201(self):
        """ทดสอบว่า POST /documents return 201"""
        response = client.post(
            "/documents",
            json={"title": "Test Doc", "content": "Test content"}
        )
        assert response.status_code == 201
    
    def test_create_returns_document(self):
        """ทดสอบว่า response มีข้อมูล document"""
        response = client.post(
            "/documents",
            json={"title": "Test Doc 2", "content": "Test content 2"}
        )
        data = response.json()
        assert "id" in data
        assert data["title"] == "Test Doc 2"
        assert data["content"] == "Test content 2"
    
    def test_create_has_word_count(self):
        """ทดสอบว่า response มี word_count"""
        response = client.post(
            "/documents",
            json={"title": "Test", "content": "One Two Three"}
        )
        data = response.json()
        assert "word_count" in data
        assert data["word_count"] == 3
    
    def test_create_invalid_empty_title(self):
        """ทดสอบว่า title ว่างไม่ได้"""
        response = client.post(
            "/documents",
            json={"title": "", "content": "Test"}
        )
        assert response.status_code == 422  # Validation error


@pytest.mark.skipif(not API_AVAILABLE, reason="API not available")
class TestGetDocument:
    """Test GET /documents/{doc_id} endpoint (TODO 4 - 10 คะแนน)"""
    
    def test_get_existing_document(self):
        """ทดสอบดึง document ที่มีอยู่"""
        response = client.get("/documents/doc_001")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == "doc_001"
    
    def test_get_nonexistent_document(self):
        """ทดสอบดึง document ที่ไม่มี"""
        response = client.get("/documents/nonexistent_id")
        assert response.status_code == 404


@pytest.mark.skipif(not API_AVAILABLE, reason="API not available")
class TestDeleteDocument:
    """Test DELETE /documents/{doc_id} endpoint (TODO 5 - 10 คะแนน)"""
    
    def test_delete_existing_document(self):
        """ทดสอบลบ document ที่มีอยู่"""
        # สร้าง document ใหม่ก่อน
        create_response = client.post(
            "/documents",
            json={"title": "To Delete", "content": "Delete me"}
        )
        doc_id = create_response.json()["id"]
        
        # ลบ
        delete_response = client.delete(f"/documents/{doc_id}")
        assert delete_response.status_code == 200
        
        # ตรวจสอบว่าลบแล้ว
        get_response = client.get(f"/documents/{doc_id}")
        assert get_response.status_code == 404
    
    def test_delete_nonexistent_document(self):
        """ทดสอบลบ document ที่ไม่มี"""
        response = client.delete("/documents/nonexistent_id")
        assert response.status_code == 404


@pytest.mark.skipif(not API_AVAILABLE, reason="API not available")
class TestSearchEndpoint:
    """Test POST /search endpoint (ให้แล้ว - ตรวจว่าทำงานได้)"""
    
    def test_search_returns_200(self):
        """ทดสอบว่า /search return 200"""
        response = client.post(
            "/search",
            json={"query": "RAG"}
        )
        assert response.status_code == 200
    
    def test_search_response_structure(self):
        """ทดสอบโครงสร้าง response"""
        response = client.post(
            "/search",
            json={"query": "RAG"}
        )
        data = response.json()
        assert "query" in data
        assert "results" in data
        assert "total" in data
        assert "took_ms" in data


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
