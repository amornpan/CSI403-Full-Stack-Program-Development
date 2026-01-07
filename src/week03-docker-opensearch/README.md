# Week 03: Docker + OpenSearch

## 📁 Files in this folder
- `docker-compose.yml` - OpenSearch Docker setup
- `setup_opensearch.py` - Python script to setup OpenSearch
- `test_connection.py` - Test OpenSearch connection

## 🎯 Learning Objectives
- Docker basics
- Run OpenSearch container
- Setup Hybrid Search Pipeline
- Connect from Python

## ▶️ How to Run

### 1. Start OpenSearch
```bash
docker-compose up -d
```

### 2. Verify
```bash
curl http://localhost:9200
```

### 3. Run Python setup
```bash
conda activate rag_env
pip install opensearch-py
python setup_opensearch.py
```
