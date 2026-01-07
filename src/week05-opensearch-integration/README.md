# Week 05: OpenSearch Integration

## 📁 Files in this folder
- `opensearch_client.py` - OpenSearch client wrapper
- `hybrid_search.py` - Hybrid search implementation
- `api.py` - Updated API with OpenSearch

## 🎯 Learning Objectives
- OpenSearch Python client
- Vector search
- Hybrid search (Vector + BM25)
- Index management

## ▶️ How to Run
```bash
# Make sure OpenSearch is running
docker-compose -f ../week03-docker-opensearch/docker-compose.yml up -d

# Run
conda activate rag_env
python hybrid_search.py
```
