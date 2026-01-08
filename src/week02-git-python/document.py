"""
Week 02: Document Class
Learn OOP basics with a Document class for RAG system
"""

from typing import Optional
from datetime import datetime


class Document:
    """Represents a document in the RAG system"""
    
    def __init__(self, title: str, content: str, source: Optional[str] = None):
        self.title = title
        self.content = content
        self.source = source
        self.created_at = datetime.now()
        self.word_count = len(content.split())
    
    def get_summary(self, max_length: int = 100) -> str:
        """Return first max_length characters of content"""
        if len(self.content) <= max_length:
            return self.content
        return self.content[:max_length] + "..."
    
    def get_chunks(self, chunk_size: int = 500) -> list[str]:
        """Split content into chunks"""
        words = self.content.split()
        chunks = []
        for i in range(0, len(words), chunk_size):
            chunk = " ".join(words[i:i + chunk_size])
            chunks.append(chunk)
        return chunks
    
    def __repr__(self) -> str:
        return f"Document(title='{self.title}', words={self.word_count})"


class MarkdownDocument(Document):
    """Document loaded from Markdown file"""
    
    def __init__(self, filepath: str):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Extract title from first line
        lines = content.split("\n")
        title = lines[0].replace("#", "").strip() if lines else "Untitled"
        
        super().__init__(title=title, content=content, source=filepath)
        self.filepath = filepath


if __name__ == "__main__":
    # Example usage
    doc = Document(
        title="Introduction to RAG",
        content="RAG (Retrieval-Augmented Generation) is a technique that combines retrieval and generation. "
                "It first retrieves relevant documents from a knowledge base, then uses an LLM to generate answers."
    )
    
    print(doc)
    print(f"Summary: {doc.get_summary(50)}")
    print(f"Chunks: {len(doc.get_chunks(10))} chunks")
