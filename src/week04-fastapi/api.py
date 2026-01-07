"""
Week 04: FastAPI Application
Basic RAG API structure
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import time
import uvicorn

from models import (
    SearchRequest, SearchResponse, SearchResult,
    QueryRequest, QueryResponse,
    HealthResponse, ErrorResponse,
    DocumentInput
)

# Create FastAPI app
app = FastAPI(
    title="RAG API",
    description="Full Stack RAG with Local LLM - Week 04",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample data (will be replaced with OpenSearch in Week 05)
SAMPLE_DOCUMENTS = [
    {
        "title": "Introduction to RAG",
        "content": "RAG (Retrieval-Augmented Generation) combines retrieval and generation for accurate answers.",
        "source": "docs/intro.md"
    },
    {
        "title": "Embeddings",
        "content": "Embeddings convert text to numerical vectors that capture semantic meaning.",
        "source": "docs/embeddings.md"
    },
    {
        "title": "Vector Database",
        "content": "OpenSearch is a vector database that stores embeddings for similarity search.",
        "source": "docs/vectordb.md"
    },
    {
        "title": "Local LLM",
        "content": "Ollama allows running LLMs locally without API keys. We use qwen2.5:7b model.",
        "source": "docs/llm.md"
    }
]


# === Endpoints ===

@app.get("/", tags=["Root"])
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to RAG API",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        timestamp=datetime.now(),
        version="1.0.0"
    )


@app.post("/search", response_model=SearchResponse, tags=["Search"])
async def search(request: SearchRequest):
    """
    Search documents
    
    Returns documents matching the query (simple keyword search for now)
    """
    start_time = time.time()
    
    # Simple keyword search (will be replaced with vector search)
    query_lower = request.query.lower()
    results = []
    
    for doc in SAMPLE_DOCUMENTS:
        content_lower = doc["content"].lower()
        title_lower = doc["title"].lower()
        
        if query_lower in content_lower or query_lower in title_lower:
            score = 1.0 if query_lower in title_lower else 0.8
            results.append(SearchResult(
                title=doc["title"],
                content=doc["content"],
                score=score,
                source=doc.get("source")
            ))
    
    # Sort by score and limit
    results.sort(key=lambda x: x.score, reverse=True)
    results = results[:request.top_k]
    
    took_ms = (time.time() - start_time) * 1000
    
    return SearchResponse(
        query=request.query,
        results=results,
        total=len(results),
        took_ms=took_ms
    )


@app.post("/query", response_model=QueryResponse, tags=["RAG"])
async def query(request: QueryRequest):
    """
    RAG Query endpoint
    
    Search for relevant documents and generate answer using LLM
    (LLM integration will be added in Week 07)
    """
    # First, search for relevant documents
    search_req = SearchRequest(query=request.query, top_k=request.top_k)
    search_response = await search(search_req)
    
    # Build context from search results
    context = "\n\n".join([
        f"[{r.title}]: {r.content}" 
        for r in search_response.results
    ])
    
    # Generate answer (placeholder - will use Ollama in Week 07)
    if search_response.results:
        answer = f"Based on the search results, here's what I found about '{request.query}':\n\n"
        for r in search_response.results:
            answer += f"- {r.title}: {r.content}\n"
    else:
        answer = f"I couldn't find relevant information about '{request.query}'."
    
    return QueryResponse(
        query=request.query,
        answer=answer,
        sources=search_response.results,
        model="placeholder (Week 07: Ollama)"
    )


@app.get("/documents", tags=["Documents"])
async def list_documents():
    """List all documents"""
    return {
        "documents": SAMPLE_DOCUMENTS,
        "total": len(SAMPLE_DOCUMENTS)
    }


@app.post("/documents", tags=["Documents"])
async def add_document(doc: DocumentInput):
    """Add a new document"""
    new_doc = {
        "title": doc.title,
        "content": doc.content,
        "source": doc.source
    }
    SAMPLE_DOCUMENTS.append(new_doc)
    return {
        "message": "Document added",
        "document": new_doc
    }


# Run server
if __name__ == "__main__":
    print("=" * 50)
    print("Week 04: FastAPI Server")
    print("=" * 50)
    print("API Docs: http://localhost:9000/docs")
    print("=" * 50)
    
    uvicorn.run(
        "api:app",
        host="0.0.0.0",
        port=9000,
        reload=True
    )
