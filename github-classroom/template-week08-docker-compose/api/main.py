"""
Week 08: API Main
=================
FastAPI application สำหรับ RAG system
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import os

app = FastAPI(
    title="RAG API",
    description="Week 08 - Docker Compose Lab",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Models
class HealthResponse(BaseModel):
    status: str
    timestamp: datetime
    version: str
    opensearch_status: str


class QueryRequest(BaseModel):
    question: str
    top_k: int = 3


class QueryResponse(BaseModel):
    question: str
    answer: str
    sources: List[str]


# Environment
OPENSEARCH_HOST = os.getenv("OPENSEARCH_HOST", "localhost")
OPENSEARCH_PORT = int(os.getenv("OPENSEARCH_PORT", "9200"))


def check_opensearch() -> str:
    """Check OpenSearch connection"""
    try:
        import requests
        response = requests.get(
            f"http://{OPENSEARCH_HOST}:{OPENSEARCH_PORT}",
            timeout=5
        )
        if response.status_code == 200:
            return "connected"
        return "error"
    except Exception:
        return "disconnected"


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        timestamp=datetime.now(),
        version="1.0.0",
        opensearch_status=check_opensearch()
    )


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "RAG API",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest):
    """
    Query the RAG system
    
    This is a mock implementation for the Docker Compose lab.
    """
    # Mock response
    return QueryResponse(
        question=request.question,
        answer=f"This is a mock answer for: {request.question}",
        sources=["mock_source_1.md", "mock_source_2.md"]
    )


@app.get("/config")
async def get_config():
    """Get current configuration"""
    return {
        "opensearch_host": OPENSEARCH_HOST,
        "opensearch_port": OPENSEARCH_PORT
    }
