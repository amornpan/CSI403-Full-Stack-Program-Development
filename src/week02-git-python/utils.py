"""
Week 02: Utility Functions
Common utilities for the RAG system
"""

import os
from typing import List, Generator
from pathlib import Path


def list_markdown_files(directory: str) -> List[str]:
    """List all markdown files in a directory"""
    path = Path(directory)
    if not path.exists():
        return []
    return [str(f) for f in path.glob("*.md")]


def read_file(filepath: str, encoding: str = "utf-8") -> str:
    """Read file content with error handling"""
    try:
        with open(filepath, "r", encoding=encoding) as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return ""
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return ""


def chunk_text(text: str, chunk_size: int = 1024, overlap: int = 200) -> Generator[str, None, None]:
    """
    Split text into overlapping chunks
    
    Args:
        text: Input text to chunk
        chunk_size: Maximum size of each chunk (in characters)
        overlap: Number of overlapping characters between chunks
    
    Yields:
        Text chunks
    """
    if len(text) <= chunk_size:
        yield text
        return
    
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        yield chunk
        start = end - overlap


def clean_text(text: str) -> str:
    """Clean and normalize text"""
    # Remove extra whitespace
    text = " ".join(text.split())
    # Remove markdown headers symbols
    lines = text.split("\n")
    cleaned_lines = [line.lstrip("#").strip() for line in lines]
    return "\n".join(cleaned_lines)


def format_context(documents: List[dict], max_length: int = 3000) -> str:
    """Format retrieved documents as context for LLM"""
    context_parts = []
    total_length = 0
    
    for i, doc in enumerate(documents, 1):
        content = doc.get("content", "")
        part = f"[Document {i}]\n{content}\n"
        
        if total_length + len(part) > max_length:
            break
        
        context_parts.append(part)
        total_length += len(part)
    
    return "\n".join(context_parts)


if __name__ == "__main__":
    # Test utilities
    print("=== Testing Utilities ===")
    
    # Test chunking
    sample_text = "This is a sample text. " * 100
    chunks = list(chunk_text(sample_text, chunk_size=100, overlap=20))
    print(f"Text length: {len(sample_text)}")
    print(f"Number of chunks: {len(chunks)}")
    print(f"First chunk: {chunks[0][:50]}...")
