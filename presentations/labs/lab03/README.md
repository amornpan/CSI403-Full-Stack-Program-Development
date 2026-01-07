# Lab 3: FastAPI (3.75%)

## Objectives
- Study api.py from Generic-RAG
- Run FastAPI server
- Test API endpoints

---

## Tasks

### Task 1: Study api.py
Review the structure:
- FastAPI app
- Pydantic models
- Endpoints: /health, /search, /query

### Task 2: Run Server
```bash
cd Generic-RAG
conda activate rag_env
python api.py
```

### Task 3: Test Endpoints
```bash
# Health check
curl http://localhost:9000/health

# Search
curl -X POST http://localhost:9000/search \
  -H "Content-Type: application/json" \
  -d '{"query": "test", "top_k": 5}'
```

### Task 4: Access Swagger Docs
Open: http://localhost:9000/docs

### Task 5: Add New Endpoint
Add `/documents` endpoint to list all documents.

---

## Repository
https://github.com/amornpan/Generic-RAG

## Deliverables
- [ ] Server running
- [ ] Endpoints tested
- [ ] New endpoint added
- [ ] Screenshots

## Deadline
Sunday 23:59
