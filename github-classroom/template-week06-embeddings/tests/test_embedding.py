"""
Test cases for Embedding Model
==============================
ใช้สำหรับ auto-grading Week 06

คะแนน: 35 คะแนน
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Check if model can be loaded (may take time)
MODEL_AVAILABLE = False
try:
    from sentence_transformers import SentenceTransformer
    MODEL_AVAILABLE = True
except ImportError:
    pass


class TestCodeStructure:
    """Test code structure (ไม่ต้องโหลด model)"""
    
    def test_class_exists(self):
        """ทดสอบว่า EmbeddingModel class มีอยู่"""
        from embedding_model import EmbeddingModel
        assert EmbeddingModel is not None
    
    def test_methods_exist(self):
        """ทดสอบว่า methods ถูก define"""
        from embedding_model import EmbeddingModel
        
        assert hasattr(EmbeddingModel, 'encode')
        assert hasattr(EmbeddingModel, 'encode_batch')
        assert hasattr(EmbeddingModel, 'cosine_similarity')
    
    def test_methods_not_pass(self):
        """ทดสอบว่า methods ไม่ใช่แค่ pass"""
        import inspect
        from embedding_model import EmbeddingModel
        
        methods = ['encode', 'encode_batch', 'cosine_similarity']
        
        for method_name in methods:
            method = getattr(EmbeddingModel, method_name)
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


class TestCosineSimilarity:
    """Test cosine_similarity (static method - ไม่ต้องโหลด model)"""
    
    def test_identical_vectors(self):
        """ทดสอบ vectors เหมือนกัน → similarity = 1.0"""
        from embedding_model import EmbeddingModel
        
        vec = [1.0, 2.0, 3.0]
        sim = EmbeddingModel.cosine_similarity(vec, vec)
        
        assert abs(sim - 1.0) < 0.001, f"Expected 1.0, got {sim}"
    
    def test_orthogonal_vectors(self):
        """ทดสอบ vectors ตั้งฉาก → similarity = 0.0"""
        from embedding_model import EmbeddingModel
        
        vec1 = [1.0, 0.0, 0.0]
        vec2 = [0.0, 1.0, 0.0]
        sim = EmbeddingModel.cosine_similarity(vec1, vec2)
        
        assert abs(sim - 0.0) < 0.001, f"Expected 0.0, got {sim}"
    
    def test_opposite_vectors(self):
        """ทดสอบ vectors ตรงข้าม → similarity = -1.0"""
        from embedding_model import EmbeddingModel
        
        vec1 = [1.0, 0.0, 0.0]
        vec2 = [-1.0, 0.0, 0.0]
        sim = EmbeddingModel.cosine_similarity(vec1, vec2)
        
        assert abs(sim - (-1.0)) < 0.001, f"Expected -1.0, got {sim}"
    
    def test_similar_vectors(self):
        """ทดสอบ vectors คล้ายกัน → similarity ใกล้ 1.0"""
        from embedding_model import EmbeddingModel
        
        vec1 = [1.0, 2.0, 3.0]
        vec2 = [1.1, 2.1, 3.1]
        sim = EmbeddingModel.cosine_similarity(vec1, vec2)
        
        assert sim > 0.99, f"Expected > 0.99, got {sim}"


@pytest.mark.skipif(not MODEL_AVAILABLE, reason="sentence-transformers not installed")
class TestEncodeWithModel:
    """Test encode functions (ต้องโหลด model)"""
    
    @pytest.fixture(scope="class")
    def model(self):
        """โหลด model ครั้งเดียว"""
        from embedding_model import EmbeddingModel
        # ใช้ model เล็กๆ สำหรับทดสอบ
        return EmbeddingModel("all-MiniLM-L6-v2")  # 384 dimensions
    
    def test_encode_returns_list(self, model):
        """ทดสอบว่า encode return list"""
        result = model.encode("Hello World")
        assert isinstance(result, list)
    
    def test_encode_correct_dimension(self, model):
        """ทดสอบว่า embedding มี dimension ถูกต้อง"""
        result = model.encode("Hello World")
        assert len(result) == model.dimension
    
    def test_encode_batch_returns_list(self, model):
        """ทดสอบว่า encode_batch return list of lists"""
        texts = ["Hello", "World"]
        result = model.encode_batch(texts)
        
        assert isinstance(result, list)
        assert len(result) == 2
        assert isinstance(result[0], list)
    
    def test_encode_batch_correct_dimensions(self, model):
        """ทดสอบว่า batch embeddings มี dimension ถูกต้อง"""
        texts = ["Hello", "World", "Test"]
        result = model.encode_batch(texts)
        
        for emb in result:
            assert len(emb) == model.dimension


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
