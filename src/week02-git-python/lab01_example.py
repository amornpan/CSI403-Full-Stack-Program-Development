"""
Lab 01: สร้าง Document class ของตัวเอง
"""

from typing import List, Dict, Optional
from datetime import datetime


class Document:
    """Document class สำหรับระบบ RAG"""
    
    def __init__(self, title: str, content: str, source: Optional[str] = None):
        self.title = title
        self.content = content
        self.source = source
        self.created_at = datetime.now()
        self.word_count = len(content.split())
    
    def get_summary(self, max_length: int = 100) -> str:
        """สร้างสรุปเนื้อหา"""
        if len(self.content) <= max_length:
            return self.content
        return self.content[:max_length] + "..."
    
    def get_word_count(self) -> int:
        """คืนค่าจำนวนคำ"""
        return self.word_count
    
    def to_dict(self) -> Dict:
        """แปลงเป็น Dictionary"""
        return {
            "title": self.title,
            "content": self.content,
            "source": self.source,
            "word_count": self.word_count
        }
    
    def __repr__(self) -> str:
        return f"Document(title='{self.title}', words={self.word_count})"


def process_documents(documents: List[Document]) -> Dict:
    """ประมวลผลรายการเอกสาร"""
    total_documents = len(documents)
    total_words = sum(doc.word_count for doc in documents)
    average_words = total_words / total_documents if total_documents > 0 else 0
    titles = [doc.title for doc in documents]
    
    return {
        "total_documents": total_documents,
        "total_words": total_words,
        "average_words": average_words,
        "titles": titles
    }


def search_documents(documents: List[Document], query: str) -> List[Document]:
    """ค้นหาเอกสารที่มี query (case-insensitive)"""
    query_lower = query.lower()
    return [doc for doc in documents if query_lower in doc.content.lower()]


# ทดสอบ
if __name__ == "__main__":
    print("=" * 50)
    print("Lab 01: Document Class Demo")
    print("=" * 50)
    
    # สร้างเอกสาร
    docs = [
        Document("RAG Introduction", "RAG combines retrieval and generation."),
        Document("OpenSearch Guide", "OpenSearch is a search engine for RAG."),
        Document("Python OOP", "Object-oriented programming in Python.")
    ]
    
    # แสดงเอกสาร
    print("\n📄 Documents:")
    for doc in docs:
        print(f"   {doc}")
    
    # ค้นหา
    print("\n🔍 Search 'RAG':")
    results = search_documents(docs, "RAG")
    for doc in results:
        print(f"   - {doc.title}")
    
    # สรุป
    print("\n📊 Statistics:")
    stats = process_documents(docs)
    print(f"   Total: {stats['total_documents']} docs")
    print(f"   Words: {stats['total_words']} words")
    print(f"   Average: {stats['average_words']:.1f} words/doc")