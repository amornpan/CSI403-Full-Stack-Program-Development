# Lab 7: Docker Compose (3.75%)

## Objectives
- Clone Advanced-RAG-Docker
- Run 6 services with Docker Compose
- Verify all services

---

## Tasks

### Task 1: Clone Repository
```bash
git clone https://github.com/amornpan/Advanced-RAG-Docker.git
cd Advanced-RAG-Docker
```

### Task 2: Study docker-compose.yml
Review the 6 services:
- opensearch_container (9200)
- embedding_container
- search_api_container (8005)
- backend_container (8006)
- frontend_container (8501)
- ollama_container (11434)

### Task 3: Start Services
```bash
docker-compose up -d
```

### Task 4: Check Status
```bash
docker-compose ps
```

### Task 5: View Logs
```bash
docker-compose logs -f
```

### Task 6: Test Application
Open http://localhost:8501

### Task 7: Stop Services
```bash
docker-compose down
```

---

## Repository
https://github.com/amornpan/Advanced-RAG-Docker

## Deliverables
- [ ] All 6 services running
- [ ] Application accessible
- [ ] Screenshots of docker ps
- [ ] Document observations

## Deadline
Sunday 23:59
