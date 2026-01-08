"""
Test cases for Week 05
======================
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


class TestOpenSearchClient:
    """Test OpenSearchClient methods"""
    
    def test_is_connected_returns_bool(self):
        """ทดสอบว่า is_connected return bool (10 คะแนน)"""
        from opensearch_client import OpenSearchClient
        client = OpenSearchClient()
        result = client.is_connected()
        assert isinstance(result, bool)
    
    def test_create_index_returns_bool(self):
        """ทดสอบว่า create_index return bool (10 คะแนน)"""
        from opensearch_client import OpenSearchClient
        client = OpenSearchClient()
        if not client.is_connected():
            pytest.skip("OpenSearch not running")
        
        client.delete_index()
        result = client.create_index()
        assert isinstance(result, bool)
    
    def test_index_document_returns_id(self):
        """ทดสอบว่า index_document return id (10 คะแนน)"""
        from opensearch_client import OpenSearchClient
        client = OpenSearchClient()
        if not client.is_connected():
            pytest.skip("OpenSearch not running")
        
        client.delete_index()
        client.create_index()
        
        doc = {
            "content": "Test content",
            "content_vector": [0.1] * 1024,
            "title": "Test",
            "source": "test.md"
        }
        result = client.index_document(doc)
        assert result is not None
        assert isinstance(result, str)
    
    def test_search_keyword_returns_list(self):
        """ทดสอบว่า search_keyword return list (10 คะแนน)"""
        from opensearch_client import OpenSearchClient
        client = OpenSearchClient()
        if not client.is_connected():
            pytest.skip("OpenSearch not running")
        
        result = client.search_keyword("test")
        assert isinstance(result, list)
    
    def test_search_vector_returns_list(self):
        """ทดสอบว่า search_vector return list (10 คะแนน)"""
        from opensearch_client import OpenSearchClient
        client = OpenSearchClient()
        if not client.is_connected():
            pytest.skip("OpenSearch not running")
        
        vector = [0.1] * 1024
        result = client.search_vector(vector)
        assert isinstance(result, list)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
