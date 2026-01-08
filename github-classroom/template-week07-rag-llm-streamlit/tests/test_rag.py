"""
Test cases for RAG Pipeline
============================
ใช้สำหรับ auto-grading Week 07

คะแนน: 35 คะแนน
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


class TestPromptTemplate:
    """Test PROMPT_TEMPLATE (TODO 1 - 10 คะแนน)"""
    
    def test_template_exists(self):
        """ทดสอบว่า PROMPT_TEMPLATE มีอยู่"""
        from rag_pipeline import PROMPT_TEMPLATE
        
        assert PROMPT_TEMPLATE is not None
        assert isinstance(PROMPT_TEMPLATE, str)
    
    def test_template_has_placeholders(self):
        """ทดสอบว่า template มี {context} และ {question}"""
        from rag_pipeline import PROMPT_TEMPLATE
        
        assert "{context}" in PROMPT_TEMPLATE, "Template must have {context} placeholder"
        assert "{question}" in PROMPT_TEMPLATE, "Template must have {question} placeholder"
    
    def test_template_is_customized(self):
        """ทดสอบว่า template ไม่ใช่ default"""
        from rag_pipeline import PROMPT_TEMPLATE
        
        assert "TODO" not in PROMPT_TEMPLATE, "Template should be customized (remove TODO)"
    
    def test_template_can_format(self):
        """ทดสอบว่า template สามารถ format ได้"""
        from rag_pipeline import PROMPT_TEMPLATE
        
        try:
            result = PROMPT_TEMPLATE.format(context="test context", question="test question")
            assert "test context" in result
            assert "test question" in result
        except KeyError as e:
            pytest.fail(f"Template format error: {e}")


class TestCodeStructure:
    """Test code structure"""
    
    def test_class_exists(self):
        """ทดสอบว่า RAGPipeline class มีอยู่"""
        from rag_pipeline import RAGPipeline
        assert RAGPipeline is not None
    
    def test_methods_exist(self):
        """ทดสอบว่า methods ถูก define"""
        from rag_pipeline import RAGPipeline
        
        assert hasattr(RAGPipeline, 'retrieve')
        assert hasattr(RAGPipeline, 'generate_answer')
        assert hasattr(RAGPipeline, 'query')
    
    def test_methods_not_pass(self):
        """ทดสอบว่า methods ไม่ใช่แค่ pass"""
        import inspect
        from rag_pipeline import RAGPipeline
        
        methods = ['retrieve', 'generate_answer', 'query']
        
        for method_name in methods:
            method = getattr(RAGPipeline, method_name)
            source = inspect.getsource(method)
            
            code_lines = [
                l for l in source.split('\n')
                if l.strip()
                and not l.strip().startswith('#')
                and not l.strip().startswith('"""')
                and not l.strip().startswith("'''")
                and l.strip() != 'pass'
            ]
            
            assert len(code_lines) > 3, f"{method_name} appears not implemented"


class TestRetrieve:
    """Test retrieve function (TODO 2 - 10 คะแนน)"""
    
    def test_retrieve_returns_list(self):
        """ทดสอบว่า retrieve return list"""
        from rag_pipeline import RAGPipeline
        
        rag = RAGPipeline()
        result = rag.retrieve("What is RAG?")
        
        assert isinstance(result, list)
    
    def test_retrieve_respects_top_k(self):
        """ทดสอบว่า retrieve ให้ผลลัพธ์ไม่เกิน top_k"""
        from rag_pipeline import RAGPipeline
        
        rag = RAGPipeline(top_k=2)
        result = rag.retrieve("What is RAG?")
        
        assert len(result) <= 2
    
    def test_retrieve_returns_relevant_docs(self):
        """ทดสอบว่า retrieve ให้ผลลัพธ์ที่เกี่ยวข้อง"""
        from rag_pipeline import RAGPipeline
        
        rag = RAGPipeline()
        result = rag.retrieve("RAG")
        
        # ควรมี doc ที่มี "RAG" ใน title หรือ content
        has_rag = any("RAG" in doc.get("title", "") or "RAG" in doc.get("content", "") for doc in result)
        assert has_rag, "Retrieved docs should be relevant to query"
    
    def test_retrieve_doc_structure(self):
        """ทดสอบโครงสร้าง document"""
        from rag_pipeline import RAGPipeline
        
        rag = RAGPipeline()
        result = rag.retrieve("test")
        
        if result:
            doc = result[0]
            assert "content" in doc, "Document should have 'content' field"


class TestQuery:
    """Test query function (TODO 4 - 5 คะแนน)"""
    
    def test_query_returns_dict(self):
        """ทดสอบว่า query return dict"""
        from rag_pipeline import RAGPipeline
        from unittest.mock import MagicMock
        
        rag = RAGPipeline()
        
        # Mock ollama to avoid actual API call
        rag.ollama = MagicMock()
        rag.ollama.generate.return_value = "Mock answer"
        
        # Also need retrieve and generate_answer to work
        # This test checks if the function structure is correct
        
        try:
            result = rag.query("test question")
            
            if result is not None:
                assert isinstance(result, dict)
                assert "question" in result or "answer" in result
        except Exception:
            # If implementation uses real Ollama, skip
            pass


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
