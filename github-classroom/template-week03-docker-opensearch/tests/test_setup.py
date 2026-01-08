"""
Test cases for setup_opensearch.py
==================================
ใช้สำหรับ auto-grading Week 03

คะแนน: 30 คะแนน

หมายเหตุ: Tests เหล่านี้จะ skip ถ้า OpenSearch ไม่ได้รัน
"""

import pytest
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Check if OpenSearch is available
OPENSEARCH_AVAILABLE = False
try:
    import requests
    response = requests.get("http://localhost:9200", timeout=2)
    OPENSEARCH_AVAILABLE = response.status_code == 200
except:
    pass


class TestCheckConnection:
    """Test check_connection function (TODO 1 - 10 คะแนน)"""
    
    @pytest.mark.skipif(not OPENSEARCH_AVAILABLE, reason="OpenSearch not running")
    def test_check_connection_returns_bool(self):
        """ทดสอบว่า function return boolean (5 คะแนน)"""
        from setup_opensearch import get_client, check_connection
        
        client = get_client()
        result = check_connection(client)
        
        assert isinstance(result, bool), "check_connection should return bool"
    
    @pytest.mark.skipif(not OPENSEARCH_AVAILABLE, reason="OpenSearch not running")
    def test_check_connection_returns_true(self):
        """ทดสอบว่า return True เมื่อ connected (5 คะแนน)"""
        from setup_opensearch import get_client, check_connection
        
        client = get_client()
        result = check_connection(client)
        
        assert result == True, "check_connection should return True when connected"


class TestHybridSearchPipeline:
    """Test setup_hybrid_search_pipeline function (TODO 2 - 10 คะแนน)"""
    
    @pytest.mark.skipif(not OPENSEARCH_AVAILABLE, reason="OpenSearch not running")
    def test_pipeline_returns_bool(self):
        """ทดสอบว่า function return boolean (5 คะแนน)"""
        from setup_opensearch import setup_hybrid_search_pipeline
        
        result = setup_hybrid_search_pipeline()
        
        assert isinstance(result, bool), "setup_hybrid_search_pipeline should return bool"
    
    @pytest.mark.skipif(not OPENSEARCH_AVAILABLE, reason="OpenSearch not running")
    def test_pipeline_created(self):
        """ทดสอบว่า pipeline ถูกสร้าง (5 คะแนน)"""
        from setup_opensearch import setup_hybrid_search_pipeline
        import requests
        
        # Run setup
        setup_hybrid_search_pipeline()
        
        # Check pipeline exists
        response = requests.get(
            "http://localhost:9200/_search/pipeline/hybrid-search-pipeline"
        )
        
        assert response.status_code == 200, "Pipeline should be created"


class TestCreateIndex:
    """Test create_index function (TODO 3 - 10 คะแนน)"""
    
    @pytest.mark.skipif(not OPENSEARCH_AVAILABLE, reason="OpenSearch not running")
    def test_create_index_returns_bool(self):
        """ทดสอบว่า function return boolean (5 คะแนน)"""
        from setup_opensearch import get_client, create_index
        
        client = get_client()
        
        # Delete index first if exists
        try:
            client.indices.delete(index="documents")
        except:
            pass
        
        result = create_index(client)
        
        assert isinstance(result, bool), "create_index should return bool"
    
    @pytest.mark.skipif(not OPENSEARCH_AVAILABLE, reason="OpenSearch not running")
    def test_index_has_correct_mappings(self):
        """ทดสอบว่า index มี mappings ถูกต้อง (5 คะแนน)"""
        from setup_opensearch import get_client, create_index
        import requests
        
        client = get_client()
        
        # Delete and recreate
        try:
            client.indices.delete(index="documents")
        except:
            pass
        
        create_index(client)
        
        # Check mappings
        response = requests.get("http://localhost:9200/documents/_mapping")
        
        if response.status_code == 200:
            mappings = response.json()
            props = mappings.get('documents', {}).get('mappings', {}).get('properties', {})
            
            assert 'content' in props, "Index should have 'content' field"
            assert 'content_vector' in props, "Index should have 'content_vector' field"


# ==========================================
# Tests ที่ไม่ต้องการ OpenSearch
# ==========================================
class TestCodeStructure:
    """Test code structure"""
    
    def test_functions_exist(self):
        """ทดสอบว่า functions ถูก define"""
        from setup_opensearch import (
            get_client,
            check_connection,
            setup_hybrid_search_pipeline,
            create_index
        )
        
        assert callable(get_client)
        assert callable(check_connection)
        assert callable(setup_hybrid_search_pipeline)
        assert callable(create_index)
    
    def test_functions_not_pass(self):
        """ทดสอบว่า functions ไม่ใช่แค่ pass"""
        import inspect
        from setup_opensearch import (
            check_connection,
            setup_hybrid_search_pipeline,
            create_index
        )
        
        # Get source code
        for func in [check_connection, setup_hybrid_search_pipeline, create_index]:
            source = inspect.getsource(func)
            # ถ้ามีแค่ pass และ docstring แสดงว่ายังไม่ได้ implement
            lines = [l.strip() for l in source.split('\n') if l.strip() and not l.strip().startswith('#') and not l.strip().startswith('"""') and not l.strip().startswith("'''")]
            
            # ต้องมีมากกว่า def และ pass
            assert len(lines) > 2, f"{func.__name__} appears to not be implemented"


# ==========================================
# รันไฟล์นี้โดยตรงเพื่อทดสอบ
# ==========================================
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
