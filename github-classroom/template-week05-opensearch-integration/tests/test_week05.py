"""
Test cases for Week 05
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


class TestOpenSearchClient:
    """Test OpenSearchClient class"""
    
    def test_class_exists(self):
        """ทดสอบว่ามี class OpenSearchClient"""
        from opensearch_client import OpenSearchClient
        assert OpenSearchClient is not None
    
    def test_is_connected_method_exists(self):
        """ทดสอบว่ามี method is_connected (10 คะแนน)"""
        from opensearch_client import OpenSearchClient
        client = OpenSearchClient()
        assert hasattr(client, 'is_connected')
        assert callable(client.is_connected)
    
    def test_index_document_method_exists(self):
        """ทดสอบว่ามี method index_document (10 คะแนน)"""
        from opensearch_client import OpenSearchClient
        client = OpenSearchClient()
        assert hasattr(client, 'index_document')
        assert callable(client.index_document)
    
    def test_search_keyword_method_exists(self):
        """ทดสอบว่ามี method search_keyword (10 คะแนน)"""
        from opensearch_client import OpenSearchClient
        client = OpenSearchClient()
        assert hasattr(client, 'search_keyword')
        assert callable(client.search_keyword)
    
    def test_search_vector_method_exists(self):
        """ทดสอบว่ามี method search_vector (10 คะแนน)"""
        from opensearch_client import OpenSearchClient
        client = OpenSearchClient()
        assert hasattr(client, 'search_vector')
        assert callable(client.search_vector)
    
    def test_delete_document_method_exists(self):
        """ทดสอบว่ามี method delete_document (10 คะแนน)"""
        from opensearch_client import OpenSearchClient
        client = OpenSearchClient()
        assert hasattr(client, 'delete_document')
        assert callable(client.delete_document)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
