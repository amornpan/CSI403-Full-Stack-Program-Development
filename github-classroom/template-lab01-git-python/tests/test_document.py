"""
Test cases for Document class
=============================
ใช้สำหรับ auto-grading Lab 01

คะแนน: 40 คะแนน (10 คะแนนต่อ test)
"""

import pytest
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from document import Document


class TestDocumentInit:
    """Test Document initialization (TODO 1)"""
    
    def test_word_count_simple(self):
        """ทดสอบนับคำง่ายๆ (10 คะแนน)"""
        doc = Document("Test", "Hello World")
        assert doc.word_count == 2, f"Expected 2, got {doc.word_count}"
    
    def test_word_count_longer(self):
        """ทดสอบนับคำหลายคำ"""
        doc = Document("Test", "One Two Three Four Five")
        assert doc.word_count == 5, f"Expected 5, got {doc.word_count}"
    
    def test_word_count_single(self):
        """ทดสอบนับคำเดียว"""
        doc = Document("Test", "Hello")
        assert doc.word_count == 1, f"Expected 1, got {doc.word_count}"


class TestGetSummary:
    """Test get_summary method (TODO 2)"""
    
    def test_summary_short_content(self):
        """ทดสอบ summary กับเนื้อหาสั้น (10 คะแนน)"""
        doc = Document("Test", "Short")
        summary = doc.get_summary(100)
        assert summary == "Short", f"Expected 'Short', got '{summary}'"
    
    def test_summary_long_content(self):
        """ทดสอบ summary กับเนื้อหายาว"""
        doc = Document("Test", "A" * 200)
        summary = doc.get_summary(50)
        assert len(summary) == 53, f"Expected length 53, got {len(summary)}"
        assert summary.endswith("..."), "Summary should end with '...'"
    
    def test_summary_exact_length(self):
        """ทดสอบ summary กับเนื้อหายาวเท่า max_length"""
        doc = Document("Test", "A" * 100)
        summary = doc.get_summary(100)
        assert summary == "A" * 100, "Should return full content when equal to max_length"


class TestGetWordCount:
    """Test get_word_count method (TODO 3)"""
    
    def test_get_word_count_returns_correct_value(self):
        """ทดสอบ get_word_count (10 คะแนน)"""
        doc = Document("Test", "One Two Three")
        result = doc.get_word_count()
        assert result == 3, f"Expected 3, got {result}"
    
    def test_get_word_count_matches_attribute(self):
        """ทดสอบว่า get_word_count() ตรงกับ word_count attribute"""
        doc = Document("Test", "Hello World Today")
        assert doc.get_word_count() == doc.word_count


class TestToDict:
    """Test to_dict method (TODO 4)"""
    
    def test_to_dict_basic(self):
        """ทดสอบ to_dict พื้นฐาน (10 คะแนน)"""
        doc = Document("Test Title", "Test Content", "test.md")
        result = doc.to_dict()
        
        assert isinstance(result, dict), "to_dict should return a dictionary"
        assert result["title"] == "Test Title"
        assert result["content"] == "Test Content"
        assert result["source"] == "test.md"
        assert result["word_count"] == 2
    
    def test_to_dict_has_all_keys(self):
        """ทดสอบว่า to_dict มี keys ครบ"""
        doc = Document("Test", "Content")
        result = doc.to_dict()
        
        required_keys = ["title", "content", "source", "word_count"]
        for key in required_keys:
            assert key in result, f"Missing key: {key}"
    
    def test_to_dict_none_source(self):
        """ทดสอบ to_dict เมื่อไม่มี source"""
        doc = Document("Test", "Content")
        result = doc.to_dict()
        assert result["source"] is None


# ==========================================
# รันไฟล์นี้โดยตรงเพื่อทดสอบ
# ==========================================
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
