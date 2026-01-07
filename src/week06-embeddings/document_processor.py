"""
Week 06: Document Processor
Handles document loading and chunking
"""

import os
from typing import List, Generator
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Chunk:
    """Represents a document chunk"""
    content: str
    chunk_id: int
    title: str
    source: str


@dataclass
class ChunkingConfig:
    chunk_size: int = 1024  # characters
    chunk_overlap: int = 200


class DocumentProcessor:
    """Process and chunk documents"""
    
    def __init__(self, config: ChunkingConfig = None):
        self.config = config or ChunkingConfig()
    
    def load_markdown_files(self, directory: str) -> List[dict]:
        """Load all markdown files from directory"""
        documents = []
        path = Path(directory)
        
        if not path.exists():
            print(f"⚠️ Directory not found: {directory}")
            return documents
        
        for filepath in path.glob("*.md"):
            content = filepath.read_text(encoding="utf-8")
            
            # Extract title from first line
            lines = content.split("\n")
            title = lines[0].replace("#", "").strip() if lines else filepath.stem
            
            documents.append({
                "title": title,
                "content": content,
                "source": str(filepath)
            })
        
        return documents
    
    def chunk_text(self, text: str) -> Generator[str, None, None]:
        """Split text into overlapping chunks"""
        if len(text) <= self.config.chunk_size:
            yield text
            return
        
        start = 0
        while start < len(text):
            end = start + self.config.chunk_size
            
            # Try to break at sentence boundary
            if end < len(text):
                # Look for period, question mark, or newline
                for sep in [". ", "? ", "! ", "\n"]:
                    pos = text.rfind(sep, start, end)
                    if pos > start:
                        end = pos + 1
                        break
            
            chunk = text[start:end].strip()
            if chunk:
                yield chunk
            
            start = end - self.config.chunk_overlap
    
    def process_document(self, doc: dict) -> List[Chunk]:
        """Process a document into chunks"""
        chunks = []
        
        for i, chunk_text in enumerate(self.chunk_text(doc["content"])):
            chunk = Chunk(
                content=chunk_text,
                chunk_id=i,
                title=doc["title"],
                source=doc["source"]
            )
            chunks.append(chunk)
        
        return chunks
    
    def process_directory(self, directory: str) -> List[Chunk]:
        """Process all documents in directory"""
        documents = self.load_markdown_files(directory)
        
        all_chunks = []
        for doc in documents:
            chunks = self.process_document(doc)
            all_chunks.extend(chunks)
            print(f"  {doc['title']}: {len(chunks)} chunks")
        
        return all_chunks


if __name__ == "__main__":
    # Test document processing
    processor = DocumentProcessor()
    
    # Test chunking
    sample_text = """
    # Introduction to RAG
    
    RAG (Retrieval-Augmented Generation) is a powerful technique that combines 
    information retrieval with text generation. It works by first retrieving 
    relevant documents from a knowledge base, then using those documents as 
    context for generating accurate and informed responses.
    
    ## How RAG Works
    
    The RAG pipeline consists of three main steps:
    1. Query embedding: Convert the user's question into a vector
    2. Retrieval: Find similar documents in the vector database
    3. Generation: Use the retrieved context to generate an answer
    
    This approach significantly reduces hallucinations and provides
    up-to-date information beyond the model's training data.
    """
    
    print("=" * 50)
    print("Testing Document Processor")
    print("=" * 50)
    
    chunks = list(processor.chunk_text(sample_text))
    print(f"\nOriginal: {len(sample_text)} chars")
    print(f"Chunks: {len(chunks)}")
    
    for i, chunk in enumerate(chunks):
        print(f"\n--- Chunk {i} ({len(chunk)} chars) ---")
        print(chunk[:100] + "..." if len(chunk) > 100 else chunk)
