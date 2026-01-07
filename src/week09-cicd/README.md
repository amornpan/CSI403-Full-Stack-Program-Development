# Week 09: CI/CD Pipeline + Testing

## 📁 Files in this folder
- `tests/` - pytest test files
- `Jenkinsfile` - Jenkins pipeline
- `.github/workflows/ci.yml` - GitHub Actions
- `pytest.ini` - pytest configuration

## 🎯 Learning Objectives
- pytest testing
- Jenkins CI/CD
- GitHub Actions
- Code coverage

## ▶️ How to Run Tests
```bash
# Install pytest
pip install pytest pytest-cov pytest-asyncio httpx

# Run tests
pytest tests/ -v

# With coverage
pytest tests/ --cov=. --cov-report=html
```

## 🔄 CI/CD Pipeline

### Jenkins
```bash
# Start Jenkins
docker run -p 8080:8080 jenkins/jenkins:lts
```

### GitHub Actions
Push to GitHub and the workflow will run automatically.
