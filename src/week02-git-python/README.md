# Week 02: Git + Python Fundamentals (3.75%)

## 📋 ข้อมูลสัปดาห์นี้

| หัวข้อ | รายละเอียด |
|--------|------------|
| **วิชา** | CSI403 - Full Stack RAG with Local LLM |
| **สัปดาห์** | Week 02 |
| **หัวข้อ** | Git + Python Basics for RAG |
| **คะแนน** | 3.75% ของคะแนนรวม |

---

## 🎯 Objectives

เมื่อเรียนจบสัปดาห์นี้ นักศึกษาจะ:

- ✅ Fork และ clone Generic-RAG repository ได้
- ✅ เข้าใจ Git workflow (branch, commit, push, PR)
- ✅ เข้าใจ Python OOP (Classes, Inheritance)
- ✅ ใช้ Type hints และ Dataclasses ได้
- ✅ เขียน Document class สำหรับระบบ RAG ได้

---

## 📁 Files in this folder

```
week02-git-python/
├── document.py         # Document & MarkdownDocument classes
├── main.py             # Entry point demo
├── rag_config.py       # Configuration using Dataclasses
├── utils.py            # Utility functions
├── requirements.txt    # Dependencies
└── README.md           # ไฟล์นี้
```

| ไฟล์ | รายละเอียด |
|------|------------|
| `document.py` | Document class พร้อม methods สำหรับ RAG |
| `rag_config.py` | Dataclasses สำหรับ configuration |
| `utils.py` | Utility functions (chunking, cleaning) |
| `main.py` | ตัวอย่างการใช้งานทุก component |

---

## 🚀 Tasks

### Task 1: Fork Repository

1. ไปที่ https://github.com/amornpan/Generic-RAG
2. คลิกปุ่ม **"Fork"** (มุมขวาบน)
3. เลือก account ของตัวเอง
4. รอให้ Fork เสร็จ - จะได้ repo ใหม่ในชื่อของคุณ

```
✅ ตอนนี้คุณมี: https://github.com/YOUR_USERNAME/Generic-RAG
```

---

### Task 2: Clone to Local

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/Generic-RAG.git

# เข้าไปยัง folder
cd Generic-RAG

# ตรวจสอบ remote
git remote -v
```

**Expected output:**
```
origin  https://github.com/YOUR_USERNAME/Generic-RAG.git (fetch)
origin  https://github.com/YOUR_USERNAME/Generic-RAG.git (push)
```

---

### Task 3: Setup Environment

```bash
# สร้าง Conda environment
conda create -n rag_env python=3.10 -y

# Activate environment
conda activate rag_env

# ติดตั้ง dependencies
pip install -r requirements.txt
```

**ตรวจสอบ:**
```bash
python --version
# Python 3.10.x

pip list | grep torch
# torch 2.6.x
```

---

### Task 4: Create Feature Branch

```bash
# สร้าง branch ใหม่
git checkout -b feature/lab01-python

# ตรวจสอบ branch
git branch
```

**Expected output:**
```
  main
* feature/lab01-python
```

---

### Task 5: Study Python OOP Examples

#### 5.1 Document Class (`document.py`)

```python
from typing import Optional
from datetime import datetime

class Document:
    """Represents a document in the RAG system"""
    
    def __init__(self, title: str, content: str, source: Optional[str] = None):
        self.title = title
        self.content = content
        self.source = source
        self.created_at = datetime.now()
        self.word_count = len(content.split())
    
    def get_summary(self, max_length: int = 100) -> str:
        """Return first max_length characters of content"""
        if len(self.content) <= max_length:
            return self.content
        return self.content[:max_length] + "..."
    
    def get_chunks(self, chunk_size: int = 500) -> list[str]:
        """Split content into chunks"""
        words = self.content.split()
        chunks = []
        for i in range(0, len(words), chunk_size):
            chunk = " ".join(words[i:i + chunk_size])
            chunks.append(chunk)
        return chunks
```

**ทดสอบ:**
```bash
python document.py
```

---

#### 5.2 Configuration with Dataclasses (`rag_config.py`)

```python
from dataclasses import dataclass, field

@dataclass
class OpenSearchConfig:
    host: str = "localhost"
    port: int = 9200
    index_name: str = "documents"
    
    @property
    def url(self) -> str:
        return f"http://{self.host}:{self.port}"

@dataclass
class RAGConfig:
    opensearch: OpenSearchConfig = field(default_factory=OpenSearchConfig)
    chunk_size: int = 1024
    top_k: int = 5
```

**ทดสอบ:**
```bash
python rag_config.py
```

---

#### 5.3 Utility Functions (`utils.py`)

```python
def chunk_text(text: str, chunk_size: int = 1024, overlap: int = 200):
    """Split text into overlapping chunks"""
    if len(text) <= chunk_size:
        yield text
        return
    
    start = 0
    while start < len(text):
        end = start + chunk_size
        yield text[start:end]
        start = end - overlap
```

**ทดสอบ:**
```bash
python utils.py
```

---

### Task 6: Run Main Demo

```bash
python main.py
```

**Expected output:**
```
==================================================
Week 02: Python Fundamentals for RAG
==================================================

1. Configuration:
   OpenSearch: http://localhost:9200
   Ollama: http://localhost:11434
   Model: qwen2.5:7b

2. Documents:
   - Document(title='RAG Introduction', words=8)
   - Document(title='Embeddings', words=8)
   - Document(title='Vector Database', words=7)

3. Chunking:
   Original: 1200 chars
   Chunks: 14

4. Context Formatting:
   Context length: 145 chars

==================================================
✅ Python fundamentals completed!
==================================================
```

---

### Task 7: Create Your Own Document Class

สร้างไฟล์ `lab01_example.py`:

```python
"""
Lab 01: สร้าง Document class ของตัวเอง
"""

from typing import List, Dict, Optional
from datetime import datetime


class Document:
    """Document class สำหรับระบบ RAG"""
    
    def __init__(self, title: str, content: str, source: Optional[str] = None):
        self.title = title
        self.content = content
        self.source = source
        self.created_at = datetime.now()
        self.word_count = len(content.split())
    
    def get_summary(self, max_length: int = 100) -> str:
        """สร้างสรุปเนื้อหา"""
        if len(self.content) <= max_length:
            return self.content
        return self.content[:max_length] + "..."
    
    def get_word_count(self) -> int:
        """คืนค่าจำนวนคำ"""
        return self.word_count
    
    def to_dict(self) -> Dict:
        """แปลงเป็น Dictionary"""
        return {
            "title": self.title,
            "content": self.content,
            "source": self.source,
            "word_count": self.word_count
        }
    
    def __repr__(self) -> str:
        return f"Document(title='{self.title}', words={self.word_count})"


def process_documents(documents: List[Document]) -> Dict:
    """ประมวลผลรายการเอกสาร"""
    total_documents = len(documents)
    total_words = sum(doc.word_count for doc in documents)
    average_words = total_words / total_documents if total_documents > 0 else 0
    titles = [doc.title for doc in documents]
    
    return {
        "total_documents": total_documents,
        "total_words": total_words,
        "average_words": average_words,
        "titles": titles
    }


def search_documents(documents: List[Document], query: str) -> List[Document]:
    """ค้นหาเอกสารที่มี query (case-insensitive)"""
    query_lower = query.lower()
    return [doc for doc in documents if query_lower in doc.content.lower()]


# ทดสอบ
if __name__ == "__main__":
    print("=" * 50)
    print("Lab 01: Document Class Demo")
    print("=" * 50)
    
    # สร้างเอกสาร
    docs = [
        Document("RAG Introduction", "RAG combines retrieval and generation."),
        Document("OpenSearch Guide", "OpenSearch is a search engine for RAG."),
        Document("Python OOP", "Object-oriented programming in Python.")
    ]
    
    # แสดงเอกสาร
    print("\n📄 Documents:")
    for doc in docs:
        print(f"   {doc}")
    
    # ค้นหา
    print("\n🔍 Search 'RAG':")
    results = search_documents(docs, "RAG")
    for doc in results:
        print(f"   - {doc.title}")
    
    # สรุป
    print("\n📊 Statistics:")
    stats = process_documents(docs)
    print(f"   Total: {stats['total_documents']} docs")
    print(f"   Words: {stats['total_words']} words")
    print(f"   Average: {stats['average_words']:.1f} words/doc")
```

---

### Task 8: Commit and Push

```bash
# ดู status
git status

# เพิ่มไฟล์
git add lab01_example.py

# Commit
git commit -m "Lab 1: Add Python OOP example - Document class"

# Push to remote
git push origin feature/lab01-python
```

---

### Task 9: Create Pull Request

1. ไปที่ GitHub repository ของคุณ
2. คลิก **"Compare & pull request"** (แถบสีเหลือง)
3. เขียน description:
   ```
   ## Lab 01: Python OOP Example
   
   - สร้าง Document class พร้อม methods
   - เพิ่ม process_documents function
   - เพิ่ม search_documents function
   ```
4. คลิก **"Create pull request"**
5. **Screenshot** หน้า PR

---

## 📊 Learning Objectives Checklist

| หัวข้อ | เนื้อหา | ไฟล์ |
|--------|---------|------|
| Python OOP | Classes, `__init__`, methods | `document.py` |
| Inheritance | `MarkdownDocument(Document)` | `document.py` |
| Type Hints | `def func(x: str) -> int` | ทุกไฟล์ |
| Dataclasses | `@dataclass` decorator | `rag_config.py` |
| Properties | `@property` decorator | `rag_config.py` |
| Generators | `yield` keyword | `utils.py` |
| File I/O | `open()`, `read()` | `utils.py` |

---

## 📤 Deliverables

- [ ] Forked repository
- [ ] Conda environment ทำงานได้
- [ ] รัน `python main.py` สำเร็จ
- [ ] Feature branch created
- [ ] `lab01_example.py` committed
- [ ] Pull Request created
- [ ] Screenshot ของ PR

---

## ▶️ Quick Start

```bash
# 1. Activate environment
conda activate rag_env

# 2. Run demo
python main.py

# 3. Run individual files
python document.py
python rag_config.py
python utils.py
```

---

## ❓ FAQ

**Q: conda activate ไม่ได้?**
```bash
conda init
# แล้วเปิด terminal ใหม่
```

**Q: pip install error?**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Q: git push ถูก reject?**
```bash
git pull origin feature/lab01-python
git push origin feature/lab01-python
```

---

## 🔗 Resources

- [Python Official Docs](https://docs.python.org/3/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Dataclasses Guide](https://docs.python.org/3/library/dataclasses.html)
- [Type Hints](https://docs.python.org/3/library/typing.html)

---

## 🎯 Next Week

**Week 03**: Docker + OpenSearch - ติดตั้งและใช้งาน Vector Database

---

## 📅 Deadline

**Sunday 23:59**
