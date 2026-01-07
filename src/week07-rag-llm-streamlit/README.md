# Week 07: Local LLM + RAG Pipeline + Streamlit

## 📁 Files in this folder
- `ollama_client.py` - Ollama LLM wrapper
- `rag_pipeline.py` - Complete RAG pipeline
- `api.py` - FastAPI with RAG
- `app.py` - Streamlit UI
- `md_corpus/` - Sample documents

## 🎯 Learning Objectives
- Ollama for local LLM
- Complete RAG pipeline
- Prompt engineering
- Streamlit chat UI

## ▶️ How to Run

### 1. Start Ollama
```bash
ollama pull qwen2.5:7b
ollama serve
```

### 2. Start OpenSearch
```bash
cd ../week03-docker-opensearch
docker-compose up -d
```

### 3. Index documents (from Week 06)
```bash
cd ../week06-embeddings
python embedding.py
```

### 4. Run API
```bash
python api.py
```

### 5. Run Streamlit
```bash
streamlit run app.py
```

## 🔗 URLs
- API: http://localhost:9000/docs
- Streamlit: http://localhost:8501
- Ollama: http://localhost:11434
