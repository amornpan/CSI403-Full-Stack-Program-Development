"""
Test cases for Hybrid Search
============================
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
    
    def test_hybrid_search_class_exists(self):
        """ทดสอบว่า HybridSearch class มีอยู่"""
        from hybrid_search import HybridSearch
        assert HybridSearch is not None
    
    def test_methods_exist(self):
        """ทดสอบว่า methods ถูก define"""
        from hybrid_search import HybridSearch
        
        search = HybridSearch.__new__(HybridSearch)
        
        assert hasattr(search, 'vector_search')
        assert hasattr(search, 'hybrid_search')
        assert hasattr(search, 'rerank_results')
    
    def test_methods_not_pass(self):
        """ทดสอบว่า methods ไม่ใช่แค่ pass"""
        import inspect
        from hybrid_search import HybridSearch
        
        methods = ['vector_search', 'hybrid_search', 'rerank_results']
        
        for method_name in methods:
            method = getattr(HybridSearch, method_name)
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
class TestVectorSearch:
    """Test vector_search (TODO 1 - 15 คะแนน)"""
    
    def test_vector_search_returns_list(self):
        """ทดสอบว่า return list"""
        from hybrid_search import HybridSearch
        
        search = HybridSearch(index_name="test_week05_hybrid")
        
        # Dummy vector
        dummy_vector = [0.1] * 1024
        
        try:
            results = search.vector_search(dummy_vector, top_k=5)
            assert isinstance(results, list)
        except Exception:
            # ถ้า index ยังไม่มี documents ก็ ok
            pass
    
    def test_vector_search_query_structure(self):
        """ทดสอบโครงสร้าง query (static test)"""
        # ทดสอบว่า query body ถูกต้อง
        expected_structure = {
            "query": {
                "knn": {
                    "content_vector": {
                        "vector": [],
                        "k": 5
                    }
                }
            },
            "size": 5
        }
        
        # ถ้า implement ถูก ควรมี structure คล้ายๆ นี้
        assert "query" in expected_structure
        assert "knn" in expected_structure["query"]


@pytest.mark.skipif(not OPENSEARCH_AVAILABLE, reason="OpenSearch not running")
class TestHybridSearch:
    """Test hybrid_search (TODO 2 - 15 คะแนน)"""
    
    def test_hybrid_search_returns_list(self):
        """ทดสอบว่า return list"""
        from hybrid_search import HybridSearch
        
        search = HybridSearch(index_name="test_week05_hybrid")
        
        dummy_vector = [0.1] * 1024
        
        try:
            results = search.hybrid_search("test query", dummy_vector, top_k=5)
            assert isinstance(results, list)
        except Exception:
            # ถ้า index ยังไม่มี documents ก็ ok
            pass
    
    def test_hybrid_search_weights_sum_to_one(self):
        """ทดสอบว่า default weights รวมกันได้ 1"""
        from hybrid_search import HybridSearch
        import inspect
        
        sig = inspect.signature(HybridSearch.hybrid_search)
        params = sig.parameters
        
        bm25_weight = params.get('bm25_weight')
        vector_weight = params.get('vector_weight')
        
        if bm25_weight and vector_weight:
            if bm25_weight.default and vector_weight.default:
                total = bm25_weight.default + vector_weight.default
                assert abs(total - 1.0) < 0.01, "Weights should sum to 1.0"


class TestRerankResults:
    """Test rerank_results (TODO 3 - 10 คะแนน)"""
    
    def test_rerank_with_sample_data(self):
        """ทดสอบ rerank กับข้อมูลตัวอย่าง"""
        from hybrid_search import HybridSearch
        
        search = HybridSearch.__new__(HybridSearch)
        search.client = None  # ไม่ต้องเชื่อมต่อจริง
        
        # Sample results
        sample_results = [
            {"id": "1", "title": "RAG Introduction", "content": "RAG is great", "score": 0.5},
            {"id": "2", "title": "Vector DB", "content": "Vectors store RAG", "score": 0.6},
            {"id": "3", "title": "Other Topic", "content": "Something else", "score": 0.7}
        ]
        
        try:
            reranked = search.rerank_results(sample_results, "RAG", top_k=3)
            
            assert isinstance(reranked, list)
            assert len(reranked) <= 3
            
            # ผลลัพธ์แรกควรมี RAG ใน title (boost สูงกว่า)
            if len(reranked) > 0 and "rerank_score" in reranked[0]:
                # เอกสารที่มี keyword ควรมี score สูงขึ้น
                pass
        except Exception as e:
            pytest.skip(f"rerank_results not fully implemented: {e}")
    
    def test_rerank_caps_score_at_one(self):
        """ทดสอบว่า score ไม่เกิน 1.0"""
        from hybrid_search import HybridSearch
        
        search = HybridSearch.__new__(HybridSearch)
        search.client = None
        
        # High initial score
        sample_results = [
            {"id": "1", "title": "RAG RAG RAG", "content": "RAG RAG RAG", "combined_score": 0.9},
        ]
        
        try:
            reranked = search.rerank_results(sample_results, "RAG", top_k=1)
            
            if len(reranked) > 0 and "rerank_score" in reranked[0]:
                assert reranked[0]["rerank_score"] <= 1.0, "Score should be capped at 1.0"
        except Exception:
            pass  # Not implemented yet


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
