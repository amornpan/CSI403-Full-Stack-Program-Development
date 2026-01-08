"""
Test cases for Document Processor
=================================
ใช้สำหรับ auto-grading Week 06

คะแนน: 35 คะแนน
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


class TestCodeStructure:
    """Test code structure"""
    
    def test_class_exists(self):
        """ทดสอบว่า DocumentProcessor class มีอยู่"""
        from document_processor import DocumentProcessor
        assert DocumentProcessor is not None
    
    def test_methods_exist(self):
        """ทดสอบว่า methods ถูก define"""
        from document_processor import DocumentProcessor
        
        assert hasattr(DocumentProcessor, 'chunk_text')
        assert hasattr(DocumentProcessor, 'process_document')
        assert hasattr(DocumentProcessor, 'process_directory')
    
    def test_methods_not_pass(self):
        """ทดสอบว่า methods ไม่ใช่แค่ pass"""
        import inspect
        from document_processor import DocumentProcessor
        
        methods = ['chunk_text', 'process_document', 'process_directory']
        
        for method_name in methods:
            method = getattr(DocumentProcessor, method_name)
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


class TestChunkText:
    """Test chunk_text (TODO 1 - 15 คะแนน)"""
    
    def test_short_text_single_chunk(self):
        """ทดสอบ text สั้นกว่า chunk_size"""
        from document_processor import DocumentProcessor
        
        processor = DocumentProcessor(chunk_size=100, chunk_overlap=20)
        text = "Short text"
        chunks = processor.chunk_text(text)
        
        assert len(chunks) == 1
        assert chunks[0] == text
    
    def test_exact_chunk_size(self):
        """ทดสอบ text ยาวเท่า chunk_size"""
        from document_processor import DocumentProcessor
        
        processor = DocumentProcessor(chunk_size=10, chunk_overlap=2)
        text = "A" * 10
        chunks = processor.chunk_text(text)
        
        assert len(chunks) == 1
    
    def test_multiple_chunks(self):
        """ทดสอบ text ยาวกว่า chunk_size"""
        from document_processor import DocumentProcessor
        
        processor = DocumentProcessor(chunk_size=10, chunk_overlap=2)
        text = "A" * 25
        chunks = processor.chunk_text(text)
        
        assert len(chunks) > 1
    
    def test_overlap_working(self):
        """ทดสอบว่า overlap ทำงาน"""
        from document_processor import DocumentProcessor
        
        processor = DocumentProcessor(chunk_size=10, chunk_overlap=3)
        text = "0123456789ABCDEFGHIJ"  # 20 chars
        chunks = processor.chunk_text(text)
        
        # ตรวจสอบว่า chunks มี overlap
        if len(chunks) >= 2:
            # ตัวท้ายของ chunk 0 ควรอยู่ในต้นของ chunk 1
            end_of_first = chunks[0][-3:]  # last 3 chars
            assert end_of_first in chunks[1], "Overlap not working correctly"
    
    def test_returns_list(self):
        """ทดสอบว่า return list"""
        from document_processor import DocumentProcessor
        
        processor = DocumentProcessor()
        chunks = processor.chunk_text("Hello World")
        
        assert isinstance(chunks, list)


class TestProcessDocument:
    """Test process_document (TODO 2 - 10 คะแนน)"""
    
    def test_process_existing_file(self):
        """ทดสอบ process ไฟล์ที่มีอยู่"""
        from document_processor import DocumentProcessor
        
        processor = DocumentProcessor(chunk_size=500, chunk_overlap=100)
        
        # ใช้ sample file
        docs_dir = os.path.join(os.path.dirname(__file__), '..', 'documents')
        sample_file = os.path.join(docs_dir, 'sample_rag_intro.md')
        
        if os.path.exists(sample_file):
            result = processor.process_document(sample_file)
            
            assert isinstance(result, dict)
            assert "filename" in result
            assert "content" in result
            assert "chunks" in result
            assert "num_chunks" in result
            assert "word_count" in result
    
    def test_process_returns_correct_filename(self):
        """ทดสอบว่า filename ถูกต้อง"""
        from document_processor import DocumentProcessor
        
        processor = DocumentProcessor()
        docs_dir = os.path.join(os.path.dirname(__file__), '..', 'documents')
        sample_file = os.path.join(docs_dir, 'sample_rag_intro.md')
        
        if os.path.exists(sample_file):
            result = processor.process_document(sample_file)
            assert result.get("filename") == "sample_rag_intro.md"


class TestProcessDirectory:
    """Test process_directory (TODO 3 - 10 คะแนน)"""
    
    def test_process_directory_returns_list(self):
        """ทดสอบว่า return list"""
        from document_processor import DocumentProcessor
        
        processor = DocumentProcessor()
        docs_dir = os.path.join(os.path.dirname(__file__), '..', 'documents')
        
        if os.path.exists(docs_dir):
            result = processor.process_directory(docs_dir)
            assert isinstance(result, list)
    
    def test_process_directory_finds_md_files(self):
        """ทดสอบว่าพบ .md files"""
        from document_processor import DocumentProcessor
        
        processor = DocumentProcessor()
        docs_dir = os.path.join(os.path.dirname(__file__), '..', 'documents')
        
        if os.path.exists(docs_dir):
            result = processor.process_directory(docs_dir, extensions=[".md"])
            
            # ควรพบ sample file อย่างน้อย 1 ไฟล์
            assert len(result) >= 1


class TestNewDocuments:
    """Test ว่านักศึกษาสร้าง documents ใหม่ (20 คะแนน)"""
    
    def test_minimum_3_documents(self):
        """ทดสอบว่ามี documents อย่างน้อย 3 ไฟล์ (ไม่นับ sample และ README)"""
        docs_dir = os.path.join(os.path.dirname(__file__), '..', 'documents')
        
        if os.path.exists(docs_dir):
            md_files = [
                f for f in os.listdir(docs_dir)
                if f.endswith('.md')
                and f != 'README.md'
                and f != 'sample_rag_intro.md'
            ]
            
            assert len(md_files) >= 3, f"ต้องมี documents ใหม่อย่างน้อย 3 ไฟล์ (พบ {len(md_files)})"
    
    def test_documents_have_minimum_words(self):
        """ทดสอบว่าแต่ละ document มีอย่างน้อย 200 คำ"""
        docs_dir = os.path.join(os.path.dirname(__file__), '..', 'documents')
        
        if os.path.exists(docs_dir):
            md_files = [
                f for f in os.listdir(docs_dir)
                if f.endswith('.md')
                and f != 'README.md'
                and f != 'sample_rag_intro.md'
            ]
            
            for filename in md_files:
                filepath = os.path.join(docs_dir, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    word_count = len(content.split())
                    
                    assert word_count >= 200, f"{filename} มี {word_count} คำ (ต้องการ >= 200)"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
