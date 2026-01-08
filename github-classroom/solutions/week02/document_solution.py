"""
Lab 01: Document Class - SOLUTION
=================================
เฉลยพร้อมคำอธิบายโค้ดทุกบรรทัด

ไฟล์นี้เป็นเฉลยสำหรับอาจารย์ ห้ามแจกนักศึกษา!
"""

# =============================================================================
# IMPORTS - การ import libraries ที่จำเป็น
# =============================================================================

from typing import Optional, Dict, Any
# typing: ใช้สำหรับ Type Hints เพื่อบอก type ของตัวแปร
# - Optional[str] หมายถึง str หรือ None ก็ได้
# - Dict[str, Any] หมายถึง dictionary ที่ key เป็น str และ value เป็นอะไรก็ได้

from datetime import datetime
# datetime: ใช้สำหรับจัดการวันที่และเวลา
# - datetime.now() คืนค่าวันเวลาปัจจุบัน


# =============================================================================
# DOCUMENT CLASS - Class หลักสำหรับเก็บข้อมูลเอกสาร
# =============================================================================

class Document:
    """
    Represents a document in the RAG system
    
    Class นี้ใช้เก็บข้อมูลเอกสารในระบบ RAG (Retrieval-Augmented Generation)
    ประกอบด้วย title, content, source, created_at, และ word_count
    
    Attributes:
        title (str): ชื่อเอกสาร
        content (str): เนื้อหาเอกสาร
        source (str): แหล่งที่มาของเอกสาร (optional)
        created_at (datetime): เวลาที่สร้าง
        word_count (int): จำนวนคำในเอกสาร
    """
    
    # =========================================================================
    # __init__ - Constructor Method (เรียกเมื่อสร้าง object ใหม่)
    # =========================================================================
    
    def __init__(self, title: str, content: str, source: Optional[str] = None):
        """
        Initialize a Document
        
        Args:
            title: ชื่อเอกสาร (required)
            content: เนื้อหาเอกสาร (required)
            source: แหล่งที่มา (optional, default=None)
        
        Example:
            >>> doc = Document("Test", "Hello World")
            >>> doc.title
            'Test'
        """
        
        # ----- บันทึก title ลงใน instance variable -----
        # self.title คือ attribute ของ object นี้
        # ใช้ self เพื่ออ้างอิงถึง object ปัจจุบัน
        self.title = title
        
        # ----- บันทึก content ลงใน instance variable -----
        # content คือเนื้อหาหลักของเอกสาร
        self.content = content
        
        # ----- บันทึก source ลงใน instance variable -----
        # source อาจเป็น None ถ้าไม่ได้ระบุ (Optional parameter)
        self.source = source
        
        # ----- บันทึกเวลาที่สร้างเอกสาร -----
        # datetime.now() คืนค่าวันเวลาปัจจุบัน
        # เป็น object ของ class datetime
        self.created_at = datetime.now()
        
        # =====================================================================
        # TODO 1 SOLUTION: คำนวณจำนวนคำ
        # =====================================================================
        # 
        # วิธีทำ:
        # 1. content.split() - แยก string เป็น list ของคำ
        #    - "Hello World" → ["Hello", "World"]
        #    - split() โดย default จะแยกด้วย whitespace (space, tab, newline)
        # 
        # 2. len() - นับจำนวน elements ใน list
        #    - len(["Hello", "World"]) → 2
        # 
        # รวมกัน: len(content.split()) = จำนวนคำ
        # 
        self.word_count = len(content.split())
        # =====================================================================
    
    # =========================================================================
    # get_summary - Method สำหรับสร้างสรุปเนื้อหา
    # =========================================================================
    
    def get_summary(self, max_length: int = 100) -> str:
        """
        สร้างสรุปเนื้อหาเอกสาร
        
        Args:
            max_length: ความยาวสูงสุดของสรุป (default: 100 ตัวอักษร)
        
        Returns:
            str: เนื้อหาที่ถูกตัดให้สั้นลง + "..." (ถ้าจำเป็น)
        
        Example:
            >>> doc = Document("Test", "A" * 200)
            >>> len(doc.get_summary(50))
            53  # 50 ตัวอักษร + 3 ตัวอักษรจาก "..."
        """
        
        # =====================================================================
        # TODO 2 SOLUTION: Implement get_summary
        # =====================================================================
        
        # ----- ตรวจสอบความยาวของ content -----
        # len(self.content) คืนค่าจำนวนตัวอักษรใน content
        if len(self.content) <= max_length:
            # ถ้า content สั้นกว่าหรือเท่ากับ max_length
            # return content ทั้งหมดโดยไม่ต้องตัด
            return self.content
        
        # ----- ถ้า content ยาวกว่า max_length -----
        # ใช้ string slicing: self.content[:max_length]
        # - [:max_length] หมายถึง ตั้งแต่ index 0 ถึง max_length-1
        # - เช่น "Hello"[:3] → "Hel"
        # 
        # แล้วต่อท้ายด้วย "..." เพื่อบอกว่ามีเนื้อหาเพิ่มเติม
        return self.content[:max_length] + "..."
        # =====================================================================
    
    # =========================================================================
    # get_word_count - Method สำหรับคืนค่าจำนวนคำ
    # =========================================================================
    
    def get_word_count(self) -> int:
        """
        คืนค่าจำนวนคำในเอกสาร
        
        Returns:
            int: จำนวนคำ
        
        Example:
            >>> doc = Document("Test", "Hello World Today")
            >>> doc.get_word_count()
            3
        
        Note:
            Method นี้เป็น getter method สำหรับ word_count attribute
            ช่วยให้ encapsulation ดีขึ้น (ซ่อน implementation details)
        """
        
        # =====================================================================
        # TODO 3 SOLUTION: Return word_count
        # =====================================================================
        # 
        # เพียงแค่ return ค่า word_count ที่คำนวณไว้แล้วใน __init__
        # 
        # ทำไมต้องมี method นี้?
        # 1. Encapsulation - ซ่อนการ implement ภายใน
        # 2. อนาคตอาจเปลี่ยนวิธีคำนวณได้โดยไม่กระทบ code ที่เรียกใช้
        # 3. สามารถเพิ่ม logic เพิ่มเติมได้ (เช่น logging, validation)
        # 
        return self.word_count
        # =====================================================================
    
    # =========================================================================
    # to_dict - Method สำหรับแปลง Object เป็น Dictionary
    # =========================================================================
    
    def to_dict(self) -> Dict[str, Any]:
        """
        แปลง Document เป็น Dictionary
        
        Returns:
            dict: Dictionary ที่มี keys: title, content, source, word_count
        
        Example:
            >>> doc = Document("Test", "Hello", "test.md")
            >>> doc.to_dict()
            {'title': 'Test', 'content': 'Hello', 'source': 'test.md', 'word_count': 1}
        
        Use Cases:
            - ส่งข้อมูลผ่าน API (JSON serialization)
            - บันทึกลง database
            - Debug และ logging
        """
        
        # =====================================================================
        # TODO 4 SOLUTION: Return dictionary
        # =====================================================================
        # 
        # สร้าง dictionary ที่มี key-value pairs ของ attributes
        # 
        # Syntax: {key: value, key: value, ...}
        # 
        return {
            "title": self.title,           # ชื่อเอกสาร
            "content": self.content,       # เนื้อหาเอกสาร
            "source": self.source,         # แหล่งที่มา (อาจเป็น None)
            "word_count": self.word_count  # จำนวนคำ
        }
        # =====================================================================
    
    # =========================================================================
    # __repr__ - Method สำหรับแสดงผล Object (ใช้สำหรับ debugging)
    # =========================================================================
    
    def __repr__(self) -> str:
        """
        String representation ของ Document
        
        __repr__ เป็น special method (dunder method) ที่ Python เรียกเมื่อ:
        - พิมพ์ object ใน interpreter
        - ใช้ repr() function
        - Debug
        
        Returns:
            str: String ที่แสดงข้อมูล object
        
        Example:
            >>> doc = Document("Test", "Hello World")
            >>> doc
            Document(title='Test', words=2)
        """
        
        # f-string (formatted string literal)
        # ใช้ f"..." และ {variable} เพื่อแทรกค่าตัวแปรลงใน string
        return f"Document(title='{self.title}', words={self.word_count})"


# =============================================================================
# MAIN BLOCK - ส่วนทดสอบ (รันเมื่อเรียกไฟล์โดยตรง)
# =============================================================================

# __name__ == "__main__" เป็น True เมื่อรันไฟล์นี้โดยตรง
# แต่เป็น False เมื่อ import ไฟล์นี้จากที่อื่น
if __name__ == "__main__":
    
    # ----- Header -----
    print("=" * 60)
    print("Testing Document Class - SOLUTION")
    print("=" * 60)
    
    # ----- สร้าง Document object -----
    # เรียก constructor (__init__) โดยส่ง arguments
    doc = Document(
        title="Introduction to RAG",
        content="RAG (Retrieval-Augmented Generation) is a technique that combines retrieval and generation.",
        source="intro.md"
    )
    
    # ----- ทดสอบ methods ต่างๆ -----
    print(f"\n1. Document repr: {doc}")
    # Output: Document(title='Introduction to RAG', words=12)
    
    print(f"2. Word count: {doc.get_word_count()}")
    # Output: Word count: 12
    
    print(f"3. Summary (50 chars): {doc.get_summary(50)}")
    # Output: Summary: RAG (Retrieval-Augmented Generation) is a te...
    
    print(f"4. To dict: {doc.to_dict()}")
    # Output: {'title': 'Introduction to RAG', 'content': '...', 'source': 'intro.md', 'word_count': 12}
    
    # ----- ทดสอบเพิ่มเติม -----
    print("\n" + "=" * 60)
    print("Additional Tests")
    print("=" * 60)
    
    # ทดสอบ get_summary กับ content สั้น
    short_doc = Document("Short", "Hi")
    print(f"\nShort doc summary: '{short_doc.get_summary(100)}'")
    # Output: 'Hi' (ไม่มี ... เพราะสั้นกว่า max_length)
    
    # ทดสอบ get_summary กับ content ยาว
    long_doc = Document("Long", "Word " * 100)
    print(f"Long doc word count: {long_doc.get_word_count()}")
    # Output: 100
    
    # ทดสอบ to_dict กับ source = None
    no_source_doc = Document("No Source", "Content without source")
    print(f"No source doc: {no_source_doc.to_dict()}")
    # Output: {'title': 'No Source', 'content': '...', 'source': None, 'word_count': 3}
    
    print("\n" + "=" * 60)
    print("All tests passed! ✅")
    print("=" * 60)
