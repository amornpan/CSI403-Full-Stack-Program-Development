# Week 08: Docker Compose (6 Services)

## 📁 Files in this folder
- `docker-compose.yml` - Complete 6-service setup
- `Dockerfile.api` - API service Dockerfile
- `Dockerfile.frontend` - Frontend Dockerfile
- `Dockerfile.embedding` - Embedding service Dockerfile

## 🎯 Learning Objectives
- Docker Compose multi-service
- Networks and volumes
- Production deployment
- Service orchestration

## 🏗️ Architecture

```
┌─────────────┐
│  Frontend   │ :8501 (Streamlit)
└──────┬──────┘
       ↓
┌─────────────┐
│   Backend   │ :8006
└──────┬──────┘
       │
       ├───→ Search API (:8005) ───→ OpenSearch (:9200)
       │                                    ↑
       │                             Embedding Service
       │
       └───→ Ollama (:11434)
```

## ▶️ How to Run
```bash
# Build and start all services
docker-compose up -d --build

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

## 🔗 URLs
- Frontend: http://localhost:8501
- Backend API: http://localhost:8006/docs
- Search API: http://localhost:8005/docs
- OpenSearch: http://localhost:9200
- Ollama: http://localhost:11434
