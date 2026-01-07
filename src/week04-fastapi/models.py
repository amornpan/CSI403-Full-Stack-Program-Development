"""
Week 04: Pydantic Models
Request/Response models for the RAG API
"""

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


# === Request Models ===

class SearchRequest(BaseModel):
    """Search request model"""
    query: str = Field(..., min_length=1, description="Search query")
    top_k: int = Field(default=5, ge=1, le=20, description="Number of results")
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {"query": "What is RAG?", "top_k": 5}
            ]
        }
    }


class QueryRequest(BaseModel):
    """RAG query request model"""
    query: str = Field(..., min_length=1, description="User question")
    top_k: int = Field(default=5, ge=1, le=20)
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "query": "อธิบายเกี่ยวกับ RAG",
                    "top_k": 5,
                    "temperature": 0.7
                }
            ]
        }
    }


class DocumentInput(BaseModel):
    """Document input for indexing"""
    title: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)
    source: Optional[str] = None


# === Response Models ===

class HealthResponse(BaseModel):
    """Health check response"""
    status: str
    timestamp: datetime
    version: str = "1.0.0"


class SearchResult(BaseModel):
    """Single search result"""
    title: str
    content: str
    score: float
    source: Optional[str] = None


class SearchResponse(BaseModel):
    """Search response with results"""
    query: str
    results: List[SearchResult]
    total: int
    took_ms: float


class QueryResponse(BaseModel):
    """RAG query response"""
    query: str
    answer: str
    sources: List[SearchResult]
    model: str


class ErrorResponse(BaseModel):
    """Error response"""
    error: str
    detail: Optional[str] = None
