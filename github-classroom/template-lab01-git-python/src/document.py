"""
Lab 01: Document Class
======================
เรียนรู้ OOP พื้นฐานด้วยการสร้าง Document class สำหรับระบบ RAG

นักศึกษาต้องทำตาม TODO ที่กำหนด
"""

from typing import Optional, Dict, Any
from datetime import datetime


class Document:
    """
    Represents a document in the RAG system
    
    Attributes:
        title (str): ชื่อเอกสาร
        content (str): เนื้อหาเอกสาร
        source (str): แหล่งที่มาของเอกสาร (optional)
        created_at (datetime): เวลาที่สร้าง
        word_count (int): จำนวนคำในเอกสาร
    
    Example:
        >>> doc = Document("Test", "Hello World")
        >>> doc.title
        'Test'
        >>> doc.word_count
        2
    """
    
    def __init__(self, title: str, content: str, source: Optional[str] = None):
        """
        Initialize a Document
        
        Args:
            title: ชื่อเอกสาร
            content: เนื้อหาเอกสาร
            source: แหล่งที่มา (optional)
        """
        self.title = title
        self.content = content
        self.source = source
        self.created_at = datetime.now()
        
        # TODO 1: คำนวณจำนวนคำและเก็บใน self.word_count
        # Hint: ใช้ content.split() เพื่อแยกคำ แล้วนับจำนวน
        # เขียนโค้ดด้านล่างนี้ (1 บรรทัด):
        self.word_count = 0  # แก้บรรทัดนี้
    
    def get_summary(self, max_length: int = 100) -> str:
        """
        สร้างสรุปเนื้อหาเอกสาร
        
        Args:
            max_length: ความยาวสูงสุดของสรุป (default: 100)
        
        Returns:
            str: เนื้อหา max_length ตัวอักษรแรก + "..." (ถ้าเนื้อหายาวกว่า max_length)
                 หรือ เนื้อหาทั้งหมด (ถ้าเนื้อหาสั้นกว่า max_length)
        
        Example:
            >>> doc = Document("Test", "A" * 200)
            >>> len(doc.get_summary(50))
            53  # 50 + len("...")
        """
        # TODO 2: Implement method นี้
        # - ถ้า content สั้นกว่าหรือเท่ากับ max_length → return content ทั้งหมด
        # - ถ้า content ยาวกว่า max_length → return content[:max_length] + "..."
        # เขียนโค้ดด้านล่างนี้:
        pass  # ลบบรรทัดนี้แล้วเขียนโค้ด
    
    def get_word_count(self) -> int:
        """
        คืนค่าจำนวนคำในเอกสาร
        
        Returns:
            int: จำนวนคำ
        
        Example:
            >>> doc = Document("Test", "Hello World Today")
            >>> doc.get_word_count()
            3
        """
        # TODO 3: Implement method นี้
        # Hint: return self.word_count
        # เขียนโค้ดด้านล่างนี้:
        pass  # ลบบรรทัดนี้แล้วเขียนโค้ด
    
    def to_dict(self) -> Dict[str, Any]:
        """
        แปลง Document เป็น Dictionary
        
        Returns:
            dict: Dictionary ที่มี keys: title, content, source, word_count
        
        Example:
            >>> doc = Document("Test", "Hello", "test.md")
            >>> doc.to_dict()
            {'title': 'Test', 'content': 'Hello', 'source': 'test.md', 'word_count': 1}
        """
        # TODO 4: Implement method นี้
        # return dictionary ที่มี keys: title, content, source, word_count
        # เขียนโค้ดด้านล่างนี้:
        pass  # ลบบรรทัดนี้แล้วเขียนโค้ด
    
    def __repr__(self) -> str:
        """String representation ของ Document"""
        return f"Document(title='{self.title}', words={self.word_count})"


# ==========================================
# ส่วนนี้สำหรับทดสอบด้วยตัวเอง
# รัน: python src/document.py
# ==========================================
if __name__ == "__main__":
    print("=" * 50)
    print("Testing Document Class")
    print("=" * 50)
    
    # สร้าง Document
    doc = Document(
        title="Introduction to RAG",
        content="RAG (Retrieval-Augmented Generation) is a technique that combines retrieval and generation.",
        source="intro.md"
    )
    
    print(f"\n1. Document: {doc}")
    print(f"2. Word count: {doc.get_word_count()}")
    print(f"3. Summary: {doc.get_summary(50)}")
    print(f"4. To dict: {doc.to_dict()}")
    
    # ทดสอบเพิ่มเติม
    print("\n" + "=" * 50)
    print("Additional Tests")
    print("=" * 50)
    
    # ทดสอบเอกสารสั้น
    short_doc = Document("Short", "Hi")
    print(f"\nShort doc summary: '{short_doc.get_summary(100)}'")
    
    # ทดสอบเอกสารยาว
    long_doc = Document("Long", "Word " * 100)
    print(f"Long doc word count: {long_doc.get_word_count()}")
