"""
Test cases for Pydantic Models
==============================
ใช้สำหรับ auto-grading Week 04

คะแนน: 30 คะแนน
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from pydantic import ValidationError


class TestDocumentCreate:
    """Test DocumentCreate model (TODO 1 - 7.5 คะแนน)"""
    
    def test_valid_document(self):
        """ทดสอบสร้าง DocumentCreate ที่ถูกต้อง"""
        from models import DocumentCreate
        
        doc = DocumentCreate(title="Test", content="Hello World")
        assert doc.title == "Test"
        assert doc.content == "Hello World"
    
    def test_with_source(self):
        """ทดสอบ DocumentCreate พร้อม source"""
        from models import DocumentCreate
        
        doc = DocumentCreate(title="Test", content="Hello", source="test.md")
        assert doc.source == "test.md"
    
    def test_source_optional(self):
        """ทดสอบว่า source เป็น optional"""
        from models import DocumentCreate
        
        doc = DocumentCreate(title="Test", content="Hello")
        assert doc.source is None
    
    def test_empty_title_fails(self):
        """ทดสอบว่า title ว่างไม่ได้"""
        from models import DocumentCreate
        
        with pytest.raises(ValidationError):
            DocumentCreate(title="", content="Hello")
    
    def test_empty_content_fails(self):
        """ทดสอบว่า content ว่างไม่ได้"""
        from models import DocumentCreate
        
        with pytest.raises(ValidationError):
            DocumentCreate(title="Test", content="")


class TestDocumentResponse:
    """Test DocumentResponse model (TODO 2 - 7.5 คะแนน)"""
    
    def test_valid_response(self):
        """ทดสอบสร้าง DocumentResponse ที่ถูกต้อง"""
        from models import DocumentResponse
        from datetime import datetime
        
        doc = DocumentResponse(
            id="doc_001",
            title="Test",
            content="Hello",
            source="test.md",
            created_at=datetime.now(),
            word_count=1
        )
        assert doc.id == "doc_001"
        assert doc.word_count == 1
    
    def test_has_all_fields(self):
        """ทดสอบว่ามี fields ครบ"""
        from models import DocumentResponse
        
        fields = DocumentResponse.model_fields
        required_fields = ['id', 'title', 'content', 'created_at', 'word_count']
        
        for field in required_fields:
            assert field in fields, f"Missing field: {field}"


class TestSearchRequest:
    """Test SearchRequest model (TODO 3 - 7.5 คะแนน)"""
    
    def test_valid_search(self):
        """ทดสอบสร้าง SearchRequest ที่ถูกต้อง"""
        from models import SearchRequest
        
        search = SearchRequest(query="test")
        assert search.query == "test"
    
    def test_default_top_k(self):
        """ทดสอบว่า top_k มีค่า default = 5"""
        from models import SearchRequest
        
        search = SearchRequest(query="test")
        assert search.top_k == 5
    
    def test_custom_top_k(self):
        """ทดสอบกำหนด top_k เอง"""
        from models import SearchRequest
        
        search = SearchRequest(query="test", top_k=10)
        assert search.top_k == 10
    
    def test_empty_query_fails(self):
        """ทดสอบว่า query ว่างไม่ได้"""
        from models import SearchRequest
        
        with pytest.raises(ValidationError):
            SearchRequest(query="")
    
    def test_top_k_min(self):
        """ทดสอบว่า top_k ต้อง >= 1"""
        from models import SearchRequest
        
        with pytest.raises(ValidationError):
            SearchRequest(query="test", top_k=0)
    
    def test_top_k_max(self):
        """ทดสอบว่า top_k ต้อง <= 20"""
        from models import SearchRequest
        
        with pytest.raises(ValidationError):
            SearchRequest(query="test", top_k=21)


class TestSearchResponse:
    """Test SearchResponse model (TODO 4 - 7.5 คะแนน)"""
    
    def test_valid_response(self):
        """ทดสอบสร้าง SearchResponse ที่ถูกต้อง"""
        from models import SearchResponse, SearchResult
        
        response = SearchResponse(
            query="test",
            results=[],
            total=0,
            took_ms=10.5
        )
        assert response.query == "test"
        assert response.total == 0
    
    def test_with_results(self):
        """ทดสอบ SearchResponse พร้อม results"""
        from models import SearchResponse, SearchResult
        
        results = [
            SearchResult(title="Doc1", content="Hello", score=0.9),
            SearchResult(title="Doc2", content="World", score=0.8)
        ]
        
        response = SearchResponse(
            query="test",
            results=results,
            total=2,
            took_ms=15.3
        )
        assert len(response.results) == 2
        assert response.results[0].score == 0.9


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
