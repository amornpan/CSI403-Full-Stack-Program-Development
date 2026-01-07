# Lab 1: Git + Python Fundamentals (3.75%)

## Objectives
- Fork and clone Generic-RAG repository
- Practice Git workflow
- Review Python fundamentals

---

## Tasks

### Task 1: Fork Repository
1. Go to https://github.com/amornpan/Generic-RAG
2. Click "Fork" button
3. You now have your own copy

### Task 2: Clone to Local
```bash
git clone https://github.com/YOUR_USERNAME/Generic-RAG.git
cd Generic-RAG
```

### Task 3: Setup Environment
```bash
conda create -n rag_env python=3.10 -y
conda activate rag_env
pip install -r requirements.txt
```

### Task 4: Create Feature Branch
```bash
git checkout -b feature/lab01-python
```

### Task 5: Write Python OOP Example
Create `lab01_example.py`:
```python
class Document:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content
    
    def get_summary(self) -> str:
        return self.content[:100] + "..."

# Test
doc = Document("Test", "This is a test document...")
print(doc.get_summary())
```

### Task 6: Commit and Push
```bash
git add .
git commit -m "Lab 1: Add Python OOP example"
git push origin feature/lab01-python
```

### Task 7: Create Pull Request
1. Go to GitHub
2. Click "Compare & pull request"
3. Create PR

---

## Deliverables
- [ ] Forked repository
- [ ] Feature branch created
- [ ] Python file committed
- [ ] Pull Request created
- [ ] Screenshot of PR

## Deadline
Sunday 23:59
