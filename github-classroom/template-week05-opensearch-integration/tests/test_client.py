"""
Test cases for OpenSearch Client
================================
ใช้สำหรับ auto-grading Week 05

คะแนน: 40 คะแนน
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Check if OpenSearch is available
OPENSEARCH_AVAILABLE = False
try:
    import requests
    response = requests.get("http://localhost:9200", timeout=2)
    OPENSEARCH_AVAILABLE = response.status_code == 200
except:
    pass


class TestCodeStructure:
    """Test code structure (ไม่ต้องการ OpenSearch)"""
    
    def test_client_class_exists(self):
        """ทดสอบว่า OpenSearchClient class มีอยู่"""
        from opensearch_client import OpenSearchClient
        assert OpenSearchClient is not None
    
    def test_methods_exist(self):
        """ทดสอบว่า methods ถูก define"""
        from opensearch_client import OpenSearchClient
        
        client = OpenSearchClient.__new__(OpenSearchClient)
        
        assert hasattr(client, 'index_document')
        assert hasattr(client, 'get_document')
        assert hasattr(client, 'delete_document')
        assert hasattr(client, 'search_bm25')
    
    def test_methods_not_pass(self):
        """ทดสอบว่า methods ไม่ใช่แค่ pass"""
        import inspect
        from opensearch_client import OpenSearchClient
        
        methods = ['index_document', 'get_document', 'delete_document', 'search_bm25']
        
        for method_name in methods:
            method = getattr(OpenSearchClient, method_name)
            source = inspect.getsource(method)
            
            # นับบรรทัดที่มี code จริง
            code_lines = [
                l for l in source.split('\n')
                if l.strip()
                and not l.strip().startswith('#')
                and not l.strip().startswith('"""')
                and not l.strip().startswith("'''")
                and l.strip() != 'pass'
            ]
            
            assert len(code_lines) > 3, f"{method_name} appears not implemented"


@pytest.mark.skipif(not OPENSEARCH_AVAILABLE, reason="OpenSearch not running")
class TestIndexDocument:
    """Test index_document (TODO 1 - 10 คะแนน)"""
    
    def test_index_document_returns_bool(self):
        """ทดสอบว่า return boolean"""
        from opensearch_client import OpenSearchClient
        
        client = OpenSearchClient(index_name="test_week05")
        client.create_index()
        
        result = client.index_document(
            "test_001",
            {"title": "Test", "content": "Hello World"}
        )
        
        assert isinstance(result, bool)
        
        # Cleanup
        client.delete_document("test_001")
    
    def test_index_document_success(self):
        """ทดสอบ index สำเร็จ"""
        from opensearch_client import OpenSearchClient
        
        client = OpenSearchClient(index_name="test_week05")
        client.create_index()
        
        result = client.index_document(
            "test_002",
            {"title": "Test", "content": "Hello World", "source": "test.md"}
        )
        
        assert result == True
        
        # Verify
        doc = client.get_document("test_002")
        assert doc is not None
        
        # Cleanup
        client.delete_document("test_002")


@pytest.mark.skipif(not OPENSEARCH_AVAILABLE, reason="OpenSearch not running")
class TestGetDocument:
    """Test get_document (TODO 2 - 10 คะแนน)"""
    
    def test_get_existing_document(self):
        """ทดสอบดึง document ที่มีอยู่"""
        from opensearch_client import OpenSearchClient
        
        client = OpenSearchClient(index_name="test_week05")
        client.create_index()
        
        # Create
        client.index_document("test_get_001", {"title": "Test Get", "content": "Content"})
        
        # Get
        doc = client.get_document("test_get_001")
        
        assert doc is not None
        assert doc["title"] == "Test Get"
        
        # Cleanup
        client.delete_document("test_get_001")
    
    def test_get_nonexistent_document(self):
        """ทดสอบดึง document ที่ไม่มี"""
        from opensearch_client import OpenSearchClient
        
        client = OpenSearchClient(index_name="test_week05")
        
        doc = client.get_document("nonexistent_id_12345")
        
        assert doc is None


@pytest.mark.skipif(not OPENSEARCH_AVAILABLE, reason="OpenSearch not running")
class TestDeleteDocument:
    """Test delete_document (TODO 3 - 10 คะแนน)"""
    
    def test_delete_existing_document(self):
        """ทดสอบลบ document ที่มีอยู่"""
        from opensearch_client import OpenSearchClient
        
        client = OpenSearchClient(index_name="test_week05")
        client.create_index()
        
        # Create
        client.index_document("test_del_001", {"title": "To Delete", "content": "Delete me"})
        
        # Delete
        result = client.delete_document("test_del_001")
        
        assert result == True
        
        # Verify deleted
        doc = client.get_document("test_del_001")
        assert doc is None
    
    def test_delete_nonexistent_document(self):
        """ทดสอบลบ document ที่ไม่มี"""
        from opensearch_client import OpenSearchClient
        
        client = OpenSearchClient(index_name="test_week05")
        
        result = client.delete_document("nonexistent_id_12345")
        
        assert result == False


@pytest.mark.skipif(not OPENSEARCH_AVAILABLE, reason="OpenSearch not running")
class TestSearchBM25:
    """Test search_bm25 (TODO 4 - 10 คะแนน)"""
    
    def test_search_returns_list(self):
        """ทดสอบว่า return list"""
        from opensearch_client import OpenSearchClient
        
        client = OpenSearchClient(index_name="test_week05")
        client.create_index()
        
        # Add some documents
        client.index_document("search_001", {"title": "RAG Introduction", "content": "RAG is great"})
        client.index_document("search_002", {"title": "Vector DB", "content": "Vectors are useful"})
        
        results = client.search_bm25("RAG", top_k=5)
        
        assert isinstance(results, list)
        
        # Cleanup
        client.delete_document("search_001")
        client.delete_document("search_002")
    
    def test_search_result_structure(self):
        """ทดสอบโครงสร้างผลลัพธ์"""
        from opensearch_client import OpenSearchClient
        
        client = OpenSearchClient(index_name="test_week05")
        client.create_index()
        
        # Add document
        client.index_document("search_003", {"title": "Test Search", "content": "Search content"})
        
        results = client.search_bm25("Search", top_k=1)
        
        if len(results) > 0:
            result = results[0]
            assert "id" in result
            assert "score" in result
            assert "title" in result
        
        # Cleanup
        client.delete_document("search_003")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
