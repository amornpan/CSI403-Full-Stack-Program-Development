"""
Test cases for Week 06
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


class TestEmbeddingModel:
    """Test EmbeddingModel"""
    
    def test_embed_text_method_exists(self):
        """ทดสอบว่ามี method embed_text (20 คะแนน)"""
        from embedding_model import EmbeddingModel
        model = EmbeddingModel()
        assert hasattr(model, 'embed_text')
        assert callable(model.embed_text)
    
    def test_embed_texts_method_exists(self):
        """ทดสอบว่ามี method embed_texts (20 คะแนน)"""
        from embedding_model import EmbeddingModel
        model = EmbeddingModel()
        assert hasattr(model, 'embed_texts')
        assert callable(model.embed_texts)


class TestDocumentProcessor:
    """Test DocumentProcessor"""
    
    def test_chunk_text_method_exists(self):
        """ทดสอบว่ามี method chunk_text (20 คะแนน)"""
        from document_processor import DocumentProcessor
        processor = DocumentProcessor()
        assert hasattr(processor, 'chunk_text')
        assert callable(processor.chunk_text)
    
    def test_process_document_method_exists(self):
        """ทดสอบว่ามี method process_document (20 คะแนน)"""
        from document_processor import DocumentProcessor
        processor = DocumentProcessor()
        assert hasattr(processor, 'process_document')
        assert callable(processor.process_document)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
