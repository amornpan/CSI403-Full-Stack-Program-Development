"""
Week 07: FastAPI with RAG
Complete API with retrieval and generation
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import time
import uvicorn

from rag_pipeline import get_rag_pipeline


# === Models ===

class QueryRequest(BaseModel):
    query: str = Field(..., min_length=1)
    top_k: int = Field(default=5, ge=1, le=20)


class SourceDocument(BaseModel):
    title: str
    content: str
    score: float
    source: Optional[str] = None


class QueryResponse(BaseModel):
    query: str
    answer: str
    sources: List[SourceDocument]
    model: str
    took_ms: float


class HealthResponse(BaseModel):
    status: str
    components: dict
    timestamp: datetime


# === App ===

app = FastAPI(
    title="RAG API",
    description="Full Stack RAG with Local LLM - Week 07",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# === Endpoints ===

@app.get("/")
async def root():
    return {
        "message": "RAG API with Local LLM",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health", response_model=HealthResponse)
async def health():
    pipeline = get_rag_pipeline()
    components = pipeline.check_components()
    
    all_healthy = all(components.values())
    
    return HealthResponse(
        status="healthy" if all_healthy else "degraded",
        components=components,
        timestamp=datetime.now()
    )


@app.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest):
    """
    RAG Query endpoint
    
    Retrieves relevant documents and generates answer using local LLM
    """
    start_time = time.time()
    
    pipeline = get_rag_pipeline()
    
    # Check components
    status = pipeline.check_components()
    if not status["opensearch"]:
        raise HTTPException(500, "OpenSearch not available")
    if not status["ollama"]:
        raise HTTPException(500, "Ollama not available")
    
    # Set top_k
    pipeline.config.top_k = request.top_k
    
    # Query
    result = pipeline.query(request.query)
    
    # Format sources
    sources = [
        SourceDocument(
            title=doc.get("title", "Unknown"),
            content=doc.get("content", "")[:200] + "...",
            score=doc.get("score", 0.0),
            source=doc.get("source")
        )
        for doc in result["sources"]
    ]
    
    took_ms = (time.time() - start_time) * 1000
    
    return QueryResponse(
        query=result["question"],
        answer=result["answer"],
        sources=sources,
        model=result["model"],
        took_ms=took_ms
    )


@app.post("/search")
async def search(request: QueryRequest):
    """Search documents only (no generation)"""
    pipeline = get_rag_pipeline()
    
    documents = pipeline.retrieve(request.query)
    
    return {
        "query": request.query,
        "results": documents,
        "total": len(documents)
    }


if __name__ == "__main__":
    print("=" * 50)
    print("Week 07: RAG API Server")
    print("=" * 50)
    print("API Docs: http://localhost:9000/docs")
    print("=" * 50)
    
    uvicorn.run("api:app", host="0.0.0.0", port=9000, reload=True)
