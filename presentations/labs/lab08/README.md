# Lab 8: CI/CD + Testing (3.75%)

## Objectives
- Write pytest tests
- Create CI/CD pipeline
- Setup GitHub Actions

---

## Tasks

### Task 1: Write test_api.py
```python
import pytest
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_search():
    response = client.post("/search", 
        json={"query": "test", "top_k": 5})
    assert response.status_code == 200
```

### Task 2: Run Tests
```bash
pytest tests/ -v
pytest tests/ --cov=. --cov-report=html
```

### Task 3: Create Jenkinsfile
```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps { sh 'docker-compose build' }
        }
        stage('Test') {
            steps { sh 'pytest tests/' }
        }
        stage('Deploy') {
            steps { sh 'docker-compose up -d' }
        }
    }
}
```

### Task 4: Create GitHub Actions
Create `.github/workflows/ci.yml`:
```yaml
name: CI/CD
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: docker-compose build
      - run: docker-compose up -d
      - run: sleep 60
      - run: curl -f http://localhost:8006/health
```

---

## Repository
https://github.com/amornpan/Advanced-RAG-Docker

## Deliverables
- [ ] Tests written
- [ ] Tests passing
- [ ] Jenkinsfile created
- [ ] GitHub Actions workflow
- [ ] Documentation

## Deadline
Sunday 23:59
