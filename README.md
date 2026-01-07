# Full Stack RAG with Local LLM

## *"Build Your Own AI, Not Just API Calls"*

---

## 📋 Course Information

| Item | Detail |
|------|--------|
| Course Code | CSI403 |
| Course Name | **Full Stack RAG with Local LLM** |
| Credits | 3 (2-3-5) |
| Semester | 2/2568 (Jan - Apr 2026) |

---

## 🎯 Course Overview

หลักสูตรเชิงปฏิบัติการที่จะพาคุณเรียนรู้การพัฒนาระบบ **Retrieval-Augmented Generation (RAG)** แบบ **Full Stack** โดยใช้ **Local LLM** ที่รันบนเครื่องของตัวเอง ไม่ต้องพึ่งพา API Token จากภายนอก

---

## 🌱 Why Local LLM?

| ❌ Traditional Course | ✅ This Course |
|----------------------|----------------|
| OpenAI API Key | Local Ollama LLM |
| Pay per Token ($$$) | Free & Unlimited |
| Cloud Dependency | Self-Hosted |
| Data sent to Cloud | Data Stays Local 🔒 |

---

## 🛠️ Tech Stack (100% Self-Hosted)

| Component | Technology | Type |
|-----------|------------|:----:|
| Frontend | Streamlit | 🏠 Local |
| Backend | FastAPI | 🏠 Local |
| Embedding | HuggingFace (BAAI/bge-m3) | 🏠 Local |
| Vector DB | OpenSearch | 🏠 Local |
| **LLM** | **Ollama (qwen2.5:7b)** | **🏠 Local** |
| DevOps | Docker Compose | 🏠 Local |
| CI/CD | Jenkins / GitHub Actions | 🏠 Self-hosted |
| Testing | pytest | 🏠 Local |

---

## 📁 Project Structure

```
Full-Stack-RAG-with-Local-LLM/
├── README.md
├── course-info/
│   ├── syllabus.md
│   └── assessment.md
├── presentations/
│   ├── lectures/week01-09/
│   └── labs/lab01-08/
└── src/                              ← SOURCE CODE
    ├── week02-git-python/
    │   ├── document.py               # Document class
    │   ├── rag_config.py             # Configuration
    │   ├── utils.py                  # Utilities
    │   └── main.py
    ├── week03-docker-opensearch/
    │   ├── docker-compose.yml        # OpenSearch setup
    │   ├── setup_opensearch.py
    │   └── test_connection.py
    ├── week04-fastapi/
    │   ├── api.py                    # FastAPI app
    │   ├── models.py                 # Pydantic models
    │   └── requirements.txt
    ├── week05-opensearch-integration/
    │   ├── opensearch_client.py      # OpenSearch wrapper
    │   └── hybrid_search.py          # Search demo
    ├── week06-embeddings/
    │   ├── embedding_model.py        # HuggingFace embeddings
    │   ├── document_processor.py     # Chunking
    │   └── embedding.py              # Indexing script
    ├── week07-rag-llm-streamlit/
    │   ├── ollama_client.py          # Ollama wrapper
    │   ├── rag_pipeline.py           # Complete RAG
    │   ├── api.py                    # API with RAG
    │   └── app.py                    # Streamlit UI
    ├── week08-docker-compose/
    │   ├── docker-compose.yml        # 6 services
    │   ├── Dockerfile.api
    │   ├── Dockerfile.frontend
    │   └── Dockerfile.embedding
    └── week09-cicd/
        ├── tests/                    # pytest tests
        ├── Jenkinsfile
        └── .github/workflows/ci.yml
```

---

## 📅 Course Structure (15 Weeks)

### PART 1: FOUNDATION (Week 1-3)
- Week 1: Introduction to RAG + Local LLM Concepts
- Week 2: Git + Python Fundamentals → `src/week02-git-python/`
- Week 3: Docker + OpenSearch → `src/week03-docker-opensearch/`

### PART 2: BACKEND DEVELOPMENT (Week 4-5)
- Week 4: FastAPI + REST API → `src/week04-fastapi/`
- Week 5: OpenSearch Integration → `src/week05-opensearch-integration/`

### PART 3: RAG CORE + LOCAL LLM (Week 6-7)
- Week 6: Embeddings + Indexing → `src/week06-embeddings/`
- Week 7: Ollama + RAG + Streamlit → `src/week07-rag-llm-streamlit/`

### PART 4: DEVOPS & DEPLOYMENT (Week 8-9)
- Week 8: Docker Compose → `src/week08-docker-compose/`
- Week 9: CI/CD + Testing → `src/week09-cicd/`

### PART 5: PROJECT (Week 10-15)
- Build Your Own Self-Hosted RAG System

---

## 🚀 Quick Start

### 1. Setup Environment
```bash
conda create -n rag_env python=3.10 -y
conda activate rag_env
```

### 2. Install Ollama
```bash
# Download from https://ollama.ai
ollama pull qwen2.5:7b
```

### 3. Start OpenSearch
```bash
cd src/week03-docker-opensearch
docker-compose up -d
```

### 4. Index Documents
```bash
cd src/week06-embeddings
pip install -r requirements.txt
python embedding.py
```

### 5. Run RAG System
```bash
cd src/week07-rag-llm-streamlit
pip install -r requirements.txt

# Terminal 1: API
python api.py

# Terminal 2: UI
streamlit run app.py
```

### 6. Access
- API: http://localhost:9000/docs
- UI: http://localhost:8501

---

## 📊 Assessment (100%)

| Category | Total |
|----------|:-----:|
| Attendance | 10% |
| Quiz (4x) | 20% |
| Lab (8x) | 30% |
| Project | 40% |

---

## 📖 Reference

- Ollama: https://ollama.ai
- HuggingFace: https://huggingface.co
- FastAPI: https://fastapi.tiangolo.com
- Streamlit: https://docs.streamlit.io
- OpenSearch: https://opensearch.org/docs

---

**© 2026 Full Stack RAG with Local LLM - Sripatum University**

*"Build Your Own AI, Not Just API Calls"*
