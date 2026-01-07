# Presentations

## 📁 Folder Structure

```
presentations/
├── lectures/
│   ├── week01/week01-intro-rag.tex
│   ├── week02/week02-git-python.tex
│   ├── week03/week03-docker-opensearch.tex
│   ├── week04/week04-fastapi.tex
│   ├── week05/week05-opensearch.tex
│   ├── week06/week06-embeddings.tex
│   ├── week07/week07-rag-llm-streamlit.tex
│   ├── week08/week08-docker-compose.tex
│   └── week09/week09-cicd.tex
├── labs/
│   ├── lab01/ - lab08/ (README.md each)
├── common/
│   └── images/
├── build-all.bat
└── README.md
```

---

## 📊 Presentation Overview

| Week | File | Topic | Repository |
|:----:|------|-------|:----------:|
| 1 | week01-intro-rag.tex | Introduction to RAG + Local LLM | - |
| 2 | week02-git-python.tex | Git + Python Fundamentals | Generic-RAG |
| 3 | week03-docker-opensearch.tex | Docker + OpenSearch | Generic-RAG |
| 4 | week04-fastapi.tex | FastAPI + REST API | Generic-RAG |
| 5 | week05-opensearch.tex | OpenSearch Integration | Generic-RAG |
| 6 | week06-embeddings.tex | Embeddings + Document Indexing | Generic-RAG |
| 7 | week07-rag-llm-streamlit.tex | Local LLM + RAG + Streamlit | Generic-RAG |
| 8 | week08-docker-compose.tex | Docker Compose (6 Services) | Advanced-RAG-Docker |
| 9 | week09-cicd.tex | CI/CD Pipeline + Testing | Advanced-RAG-Docker |

---

## 🛠️ Building Presentations

### Prerequisites
- MiKTeX (Windows) or TeX Live
- VS Code with LaTeX Workshop extension

### Build All
```batch
cd presentations
build-all.bat
```

### Build Single
```batch
cd presentations/lectures/week01
pdflatex week01-intro-rag.tex
```

---

**© 2026 Full Stack RAG with Local LLM**
