# Full Stack RAG with Local LLM - Quizzes for Wayground.com
## CSI403 - Sripatum University

---

# Week 1: Introduction to RAG + Local LLM (10 Questions)

---

## Question 1
**RAG ย่อมาจากอะไร?**

- a) Real-time Artificial Generation
- b) Retrieval-Augmented Generation ✓
- c) Rapid API Gateway
- d) Remote Access Gateway

**Answer: b) Retrieval-Augmented Generation**

**Explanation:**
RAG ย่อมาจาก **Retrieval-Augmented Generation** ซึ่งเป็นเทคนิคที่รวมการค้นหาข้อมูล (Retrieval) เข้ากับการสร้างคำตอบ (Generation) โดย LLM

RAG ทำงาน 3 ขั้นตอนหลัก:
1. **Retrieval** - ค้นหาเอกสารที่เกี่ยวข้อง
2. **Augmented** - เพิ่ม Context ให้กับ Prompt
3. **Generation** - LLM สร้างคำตอบจาก Context

📚 **Reference:** Week 1 Lecture - "What is RAG?" slide

---

## Question 2
**ในหลักสูตรนี้ใช้ LLM ตัวใดที่รันแบบ Local?**

- a) OpenAI GPT-4
- b) Google Bard
- c) Ollama (qwen2.5:7b) ✓
- d) Claude API

**Answer: c) Ollama (qwen2.5:7b)**

**Explanation:**
หลักสูตรนี้ใช้ **Ollama** เป็น Local LLM Runtime และใช้โมเดล **qwen2.5:7b** ซึ่งมี 7 billion parameters

ข้อดีของ Ollama:
- รันได้บนเครื่องของตนเอง ไม่ต้องใช้ Cloud
- ไม่ต้องใช้ API Key
- ข้อมูลไม่ถูกส่งออกไปภายนอก
- ใช้งานฟรี ไม่จำกัด

```bash
# ติดตั้งโมเดล
ollama pull qwen2.5:7b

# รันโมเดล
ollama run qwen2.5:7b
```

📚 **Reference:** Week 1 Lecture - "Tech Stack" slide, Week 7 Lecture - "What is Ollama?" slide

---

## Question 3
**Vector Database ที่ใช้ในหลักสูตรนี้คืออะไร?**

- a) PostgreSQL
- b) MongoDB
- c) OpenSearch ✓
- d) MySQL

**Answer: c) OpenSearch**

**Explanation:**
หลักสูตรนี้ใช้ **OpenSearch** เป็น Vector Database เพราะ:
- เป็น Open Source
- รองรับ Self-Hosted (รันบนเครื่องตนเอง)
- รองรับ Hybrid Search (รวม Vector Search + Keyword Search)
- รองรับ knn_vector สำหรับเก็บ Embeddings

OpenSearch รันบน Port 9200 สำหรับ REST API และ Port 9600 สำหรับ Performance Analyzer

📚 **Reference:** Week 1 Lecture - "Tech Stack" slide, Week 3 Lecture - "What is Vector Database?" slide

---

## Question 4
**Embedding Model ที่ใช้ในหลักสูตรมีกี่ dimensions?**

- a) 512
- b) 768
- c) 1024 ✓
- d) 1536

**Answer: c) 1024**

**Explanation:**
หลักสูตรนี้ใช้โมเดล **BAAI/bge-m3** ซึ่งสร้าง Vector ขนาด **1024 dimensions**

เปรียบเทียบกับโมเดลอื่น:
| Model | Dimensions | Type |
|-------|-----------|------|
| OpenAI ada-002 | 1536 | Cloud |
| **BAAI/bge-m3** | **1024** | **Local** |

ข้อดีของ bge-m3:
- รันได้แบบ Local ไม่ต้องใช้ API Key
- รองรับหลายภาษา (Multilingual)

📚 **Reference:** Week 6 Lecture - "Embedding Models" slide

---

## Question 5
**ข้อใดไม่ใช่ข้อจำกัดของ LLM ทั่วไป?**

- a) Knowledge cutoff date
- b) ไม่สามารถเข้าถึงเอกสารส่วนตัวได้
- c) สามารถรันได้แบบ offline เสมอ ✓
- d) อาจเกิด Hallucination ได้

**Answer: c) สามารถรันได้แบบ offline เสมอ**

**Explanation:**
LLM ทั่วไป (เช่น ChatGPT, Claude) มีข้อจำกัดดังนี้:
- **Knowledge cutoff date** - มีวันที่ตัดความรู้ ไม่รู้ข้อมูลหลังจากนั้น
- **ไม่สามารถเข้าถึงเอกสารส่วนตัว** - ไม่มีความสามารถอ่านไฟล์ของคุณ
- **Hallucination** - อาจสร้างข้อมูลเท็จขึ้นมา

**ข้อ c) ไม่ถูกต้อง** เพราะ LLM ส่วนใหญ่เป็น Cloud API ต้องใช้ Internet เพียง Local LLM เท่านั้นที่สามารถรันได้แบบ offline

📚 **Reference:** Week 1 Lecture - "The Problem with LLMs" slide

---

## Question 6
**RAG มีขั้นตอนหลักกี่ขั้นตอน?**

- a) 2 ขั้นตอน
- b) 3 ขั้นตอน ✓
- c) 4 ขั้นตอน
- d) 5 ขั้นตอน

**Answer: b) 3 ขั้นตอน**

**Explanation:**
RAG มี **3 ขั้นตอนหลัก** ตามชื่อย่อ:

1. **R - Retrieval (ค้นหา)**
   - ค้นหาเอกสารที่เกี่ยวข้องจาก Vector Database
   
2. **A - Augmented (เสริม)**
   - นำเอกสารที่ค้นหาได้มาเป็น Context เสริมให้กับ Prompt
   
3. **G - Generation (สร้าง)**
   - LLM สร้างคำตอบโดยใช้ Context ที่ได้รับ

📚 **Reference:** Week 1 Lecture - "What is RAG?" slide

---

## Question 7
**ข้อใดคือข้อดีของ Local LLM เมื่อเทียบกับ Cloud API?**

- a) ต้องจ่ายค่า API
- b) ข้อมูลถูกส่งไปยัง Cloud
- c) ไม่มี Rate Limit และใช้งานฟรี ✓
- d) ต้องพึ่งพา Internet ตลอดเวลา

**Answer: c) ไม่มี Rate Limit และใช้งานฟรี**

**Explanation:**
ข้อดีของ Local LLM เปรียบเทียบกับ Cloud API:

| Cloud API | Local LLM |
|-----------|-----------|
| จ่ายค่า Token | **ฟรี ไม่จำกัด** |
| มี Rate Limit | **ไม่มี Rate Limit** |
| ข้อมูลส่งไป Cloud | **ข้อมูลอยู่ในเครื่อง** |
| ต้องใช้ Internet | **ทำงานได้ Offline** |

📚 **Reference:** Week 1 Lecture - "Benefits of Local LLM" slide

---

## Question 8
**Frontend ที่ใช้ในหลักสูตรนี้คืออะไร?**

- a) React
- b) Vue.js
- c) Streamlit ✓
- d) Angular

**Answer: c) Streamlit**

**Explanation:**
หลักสูตรนี้ใช้ **Streamlit** เป็น Frontend เพราะ:
- เขียน UI ได้ง่ายด้วย Python
- ไม่ต้องรู้ HTML/CSS/JavaScript
- เหมาะสำหรับสร้าง Data Apps และ AI Applications

```python
import streamlit as st

st.title("RAG Q&A")

if prompt := st.chat_input("Ask..."):
    st.chat_message("user").write(prompt)
    response = call_api(prompt)
    st.chat_message("assistant").write(response)
```

📚 **Reference:** Week 1 Lecture - "Tech Stack" slide, Week 7 Lecture - "Streamlit UI" slide

---

## Question 9
**ค่า Token ของ OpenAI GPT-4 ต่อ 1 ล้าน Token ประมาณเท่าไร?**

- a) $2.00
- b) $10.00
- c) $30.00 ✓
- d) $50.00

**Answer: c) $30.00**

**Explanation:**
ค่าใช้จ่ายต่อ 1 ล้าน Token:

| Service | Cost | Type |
|---------|------|------|
| OpenAI GPT-4 | **$30.00** | Cloud API |
| OpenAI GPT-3.5 | $2.00 | Cloud API |
| Ollama (Local) | **$0.00** | Self-Hosted |

นี่คือเหตุผลหลักที่หลักสูตรนี้เลือกใช้ Local LLM - **ฟรีตลอดไป!**

📚 **Reference:** Week 1 Lecture - "Cost Comparison" slide

---

## Question 10
**ซอฟต์แวร์ใดที่ต้องติดตั้งก่อนเริ่มเรียน Week 2?**

- a) Adobe Photoshop
- b) Microsoft Word
- c) Docker Desktop ✓
- d) Notepad++

**Answer: c) Docker Desktop**

**Explanation:**
ซอฟต์แวร์ที่ต้องติดตั้งก่อน Week 2:

1. **Miniconda** - Python 3.10+
2. **Git** - Version Control
3. **VS Code** - Code Editor
4. **Docker Desktop** - Container Platform
5. **Ollama** - Local LLM Runtime

Docker Desktop จำเป็นสำหรับรัน OpenSearch และบริการอื่นๆ ในรูปแบบ Container

📚 **Reference:** Week 1 Lecture - "Software to Install" slide

---

# Week 2: Git + Python Fundamentals (10 Questions)

---

## Question 1
**คำสั่ง Git ใดใช้สำหรับ Clone repository จาก GitHub?**

- a) git pull
- b) git clone ✓
- c) git fetch
- d) git download

**Answer: b) git clone**

**Explanation:**
`git clone` ใช้สำหรับคัดลอก repository ทั้งหมดจาก Remote (GitHub) มายังเครื่อง Local

```bash
git clone https://github.com/amornpan/Generic-RAG.git
cd Generic-RAG
```

เปรียบเทียบคำสั่งอื่น:
- `git pull` - ดึงการเปลี่ยนแปลงล่าสุดมา merge กับ local
- `git fetch` - ดึงข้อมูลมาแต่ไม่ merge
- `git download` - ไม่มีคำสั่งนี้ใน Git

📚 **Reference:** Week 2 Lecture - "Git Basic Commands" slide, Lab 1 - Task 2

---

## Question 2
**คำสั่งใดใช้ตรวจสอบสถานะของ Git repository?**

- a) git check
- b) git info
- c) git status ✓
- d) git view

**Answer: c) git status**

**Explanation:**
`git status` แสดงสถานะปัจจุบันของ repository:
- ไฟล์ที่มีการเปลี่ยนแปลง
- ไฟล์ที่อยู่ใน Staging Area
- Branch ปัจจุบัน

```bash
git status
```

ตัวอย่าง output:
```
On branch main
Changes not staged for commit:
  modified:   api.py
```

📚 **Reference:** Week 2 Lecture - "Git Basic Commands" slide

---

## Question 3
**ในการสร้าง Conda environment ใช้ Python version ใด?**

- a) Python 3.8
- b) Python 3.9
- c) Python 3.10 ✓
- d) Python 3.12

**Answer: c) Python 3.10**

**Explanation:**
หลักสูตรนี้ใช้ **Python 3.10** ในการสร้าง Conda Environment:

```bash
# สร้าง environment
conda create -n rag_env python=3.10 -y

# Activate environment
conda activate rag_env

# Install dependencies
pip install -r requirements.txt
```

📚 **Reference:** Week 2 Lecture - "Conda Environment" slide, Lab 1 - Task 3

---

## Question 4
**Type hint สำหรับตัวแปรที่เก็บค่าทศนิยมคือข้อใด?**

- a) int
- b) str
- c) float ✓
- d) decimal

**Answer: c) float**

**Explanation:**
Python Type Hints สำหรับประเภทข้อมูลพื้นฐาน:

```python
name: str = "RAG System"      # ข้อความ
count: int = 42               # จำนวนเต็ม
score: float = 0.95           # ทศนิยม
is_active: bool = True        # Boolean
```

📚 **Reference:** Week 2 Lecture - "Python Data Types" slide

---

## Question 5
**คำสั่งใดใช้ Push code ไปยัง Remote repository?**

- a) git send origin main
- b) git push origin main ✓
- c) git upload origin main
- d) git commit origin main

**Answer: b) git push origin main**

**Explanation:**
`git push origin main` ใช้ส่ง commits จาก Local ไปยัง Remote repository

```bash
# Stage all changes
git add .

# Commit with message
git commit -m "Add new feature"

# Push to remote
git push origin main
```

- `origin` = ชื่อ Remote repository (default)
- `main` = ชื่อ Branch

📚 **Reference:** Week 2 Lecture - "Git Basic Commands" slide, Lab 1 - Task 6

---

## Question 6
**Method __init__ ใน Python Class ใช้ทำอะไร?**

- a) ลบ Object
- b) กำหนดค่าเริ่มต้นของ Object ✓
- c) แสดงผล Object
- d) คัดลอก Object

**Answer: b) กำหนดค่าเริ่มต้นของ Object**

**Explanation:**
`__init__` เป็น Constructor Method ใน Python ใช้กำหนดค่าเริ่มต้นเมื่อสร้าง Object

```python
class Document:
    def __init__(self, title: str, content: str):
        self.title = title      # กำหนดค่าเริ่มต้น
        self.content = content  # กำหนดค่าเริ่มต้น
    
    def get_summary(self) -> str:
        return self.content[:100] + "..."

# สร้าง Object - __init__ จะถูกเรียก
doc = Document("Test", "This is a test document...")
```

📚 **Reference:** Week 2 Lecture - "Python Classes" slide, Lab 1 - Task 5

---

## Question 7
**คำสั่งใดใช้ Activate Conda environment ชื่อ rag_env?**

- a) conda start rag_env
- b) conda activate rag_env ✓
- c) conda run rag_env
- d) conda enable rag_env

**Answer: b) conda activate rag_env**

**Explanation:**
`conda activate` ใช้เปิดใช้งาน Conda Environment:

```bash
# สร้าง environment
conda create -n rag_env python=3.10 -y

# Activate (เปิดใช้งาน)
conda activate rag_env

# Deactivate (ปิดใช้งาน)
conda deactivate
```

📚 **Reference:** Week 2 Lecture - "Conda Environment" slide, Lab 1 - Task 3

---

## Question 8
**ข้อใดคือวิธีการประกาศ Dictionary ใน Python?**

- a) items = [1, 2, 3]
- b) items = (1, 2, 3)
- c) config = {"model": "bge-m3"} ✓
- d) config = <"model", "bge-m3">

**Answer: c) config = {"model": "bge-m3"}**

**Explanation:**
Python Collections แต่ละประเภท:

```python
# List - ใช้ []
items: list = [1, 2, 3]

# Tuple - ใช้ ()
coords: tuple = (1, 2, 3)

# Dictionary - ใช้ {}
config: dict = {"model": "bge-m3"}
```

Dictionary เก็บข้อมูลแบบ key-value pairs

📚 **Reference:** Week 2 Lecture - "Python Data Types" slide

---

## Question 9
**คำสั่ง git add . ทำหน้าที่อะไร?**

- a) ลบไฟล์ทั้งหมด
- b) เพิ่มไฟล์ทั้งหมดเข้า Staging area ✓
- c) สร้างไฟล์ใหม่
- d) แสดงไฟล์ทั้งหมด

**Answer: b) เพิ่มไฟล์ทั้งหมดเข้า Staging area**

**Explanation:**
`git add .` เพิ่มไฟล์ที่มีการเปลี่ยนแปลงทั้งหมดเข้า Staging Area เพื่อเตรียม Commit

```bash
# Stage ไฟล์เดียว
git add filename.py

# Stage ไฟล์ทั้งหมด
git add .

# Commit
git commit -m "Add new feature"
```

📚 **Reference:** Week 2 Lecture - "Git Basic Commands" slide, Lab 1 - Task 6

---

## Question 10
**การสร้าง Feature branch ใน Git ใช้คำสั่งใด?**

- a) git branch feature/lab01
- b) git checkout -b feature/lab01 ✓
- c) git create branch feature/lab01
- d) git new feature/lab01

**Answer: b) git checkout -b feature/lab01**

**Explanation:**
`git checkout -b` สร้าง Branch ใหม่และสลับไปใช้งานในคำสั่งเดียว

```bash
# สร้างและสลับไป branch ใหม่
git checkout -b feature/lab01-python
```

เทียบกับ:
```bash
# git branch สร้าง branch แต่ไม่สลับไป
git branch feature/lab01
git checkout feature/lab01  # ต้องสลับเอง
```

**Git Flow Best Practice:** สร้าง Feature Branch สำหรับงานใหม่ แทนที่จะ commit ตรงไปที่ main

📚 **Reference:** Week 2 Lecture, Lab 1 - Task 4

---

# Week 3: Docker + OpenSearch (10 Questions)

---

## Question 1
**Docker Image คืออะไร?**

- a) Container ที่กำลังทำงาน
- b) Blueprint หรือ Template สำหรับสร้าง Container ✓
- c) ไฟล์ Log ของ Container
- d) Network สำหรับ Container

**Answer: b) Blueprint หรือ Template สำหรับสร้าง Container**

**Explanation:**
ความแตกต่างระหว่าง Docker Image และ Container:

| Docker Image | Docker Container |
|-------------|-----------------|
| Blueprint/Template | Running Instance |
| ไฟล์ที่ไม่เปลี่ยนแปลง | กำลังทำงาน |
| สร้างได้หลาย Container | สร้างจาก Image |

```bash
# ดู Images ทั้งหมด
docker images

# ดู Containers ที่กำลังทำงาน
docker ps
```

📚 **Reference:** Week 3 Lecture - "What is Docker?" slide

---

## Question 2
**OpenSearch ใช้ Port ใดสำหรับ REST API?**

- a) 8080
- b) 3306
- c) 9200 ✓
- d) 5432

**Answer: c) 9200**

**Explanation:**
OpenSearch ใช้ 2 Ports หลัก:

| Port | Purpose |
|------|---------|
| **9200** | **REST API** |
| 9600 | Performance Analyzer |

```bash
# ทดสอบ REST API
curl http://localhost:9200
```

📚 **Reference:** Week 3 Lecture - "Run OpenSearch" slide, Lab 2 - Task 2

---

## Question 3
**คำสั่งใดใช้แสดง Container ที่กำลังทำงานทั้งหมด?**

- a) docker list
- b) docker ps ✓
- c) docker show
- d) docker containers

**Answer: b) docker ps**

**Explanation:**
```bash
# แสดง Container ที่กำลังทำงาน
docker ps

# แสดง Container ทั้งหมด (รวมที่หยุดแล้ว)
docker ps -a
```

📚 **Reference:** Week 3 Lecture - "Docker Commands" slide

---

## Question 4
**Flag -d ในคำสั่ง docker run หมายถึงอะไร?**

- a) Delete mode
- b) Debug mode
- c) Detached mode ✓
- d) Download mode

**Answer: c) Detached mode**

**Explanation:**
`-d` หรือ `--detach` หมายถึงรัน Container ใน Background

```bash
# รันแบบ Detached (Background)
docker run -d --name opensearch-node \
  -p 9200:9200 \
  opensearchproject/opensearch:2.11.1
```

ถ้าไม่ใส่ -d จะรันแบบ Foreground และ terminal จะถูก block

📚 **Reference:** Week 3 Lecture - "Docker Commands" slide

---

## Question 5
**ในการตั้งค่า OpenSearch แบบ Single node ต้องกำหนด Environment variable ใด?**

- a) discovery.type=cluster
- b) discovery.type=single-node ✓
- c) node.type=single
- d) cluster.mode=single

**Answer: b) discovery.type=single-node**

**Explanation:**
สำหรับการรัน OpenSearch แบบ Single Node:

```bash
docker run -d --name opensearch-node \
  -p 9200:9200 -p 9600:9600 \
  -e "discovery.type=single-node" \
  -e "DISABLE_SECURITY_PLUGIN=true" \
  opensearchproject/opensearch:2.11.1
```

- `discovery.type=single-node` - บอกว่าเป็น Node เดียว ไม่ต้องค้นหา Node อื่น

📚 **Reference:** Week 3 Lecture - "Run OpenSearch" slide, Lab 2 - Task 2

---

## Question 6
**Version ของ OpenSearch ที่ใช้ในหลักสูตรคือเวอร์ชันใด?**

- a) 1.0.0
- b) 2.0.0
- c) 2.11.1 ✓
- d) 3.0.0

**Answer: c) 2.11.1**

**Explanation:**
หลักสูตรนี้ใช้ **OpenSearch 2.11.1**:

```bash
docker run -d \
  opensearchproject/opensearch:2.11.1
```

📚 **Reference:** Week 3 Lecture - "Run OpenSearch" slide, Lab 2 - Task 2

---

## Question 7
**คำสั่งใดใช้หยุดการทำงานของ Container ชื่อ my-app?**

- a) docker kill my-app
- b) docker stop my-app ✓
- c) docker pause my-app
- d) docker end my-app

**Answer: b) docker stop my-app**

**Explanation:**
```bash
# หยุด Container (graceful shutdown)
docker stop my-app

# ลบ Container
docker rm my-app
```

เปรียบเทียบ:
- `docker stop` - Graceful shutdown (ส่ง SIGTERM)
- `docker kill` - Force stop (ส่ง SIGKILL)
- `docker pause` - หยุดชั่วคราว (ยังอยู่ใน memory)

📚 **Reference:** Week 3 Lecture - "Docker Commands" slide

---

## Question 8
**Hybrid Search Pipeline ใช้ Normalization technique แบบใด?**

- a) z-score
- b) min_max ✓
- c) decimal
- d) percentage

**Answer: b) min_max**

**Explanation:**
Hybrid Search Pipeline ใช้ **min_max normalization**:

```bash
curl -X PUT "localhost:9200/_search/pipeline/hybrid-search-pipeline" \
  -H "Content-Type: application/json" \
  -d '{
    "phase_results_processors": [{
      "normalization-processor": {
        "normalization": {"technique": "min_max"},
        "combination": {
          "technique": "arithmetic_mean",
          "parameters": {"weights": [0.3, 0.7]}
        }
      }
    }]
  }'
```

min_max ทำให้ค่าอยู่ในช่วง 0-1 เพื่อรวม Vector Score กับ BM25 Score

📚 **Reference:** Week 3 Lecture, Lab 2 - Task 4

---

## Question 9
**Port 9600 ของ OpenSearch ใช้สำหรับอะไร?**

- a) REST API
- b) Performance Analyzer ✓
- c) Database backup
- d) Admin console

**Answer: b) Performance Analyzer**

**Explanation:**
OpenSearch Ports:

| Port | Purpose |
|------|---------|
| 9200 | REST API |
| **9600** | **Performance Analyzer** |

📚 **Reference:** Week 3 Lecture - "Run OpenSearch" slide, Lab 2 - Task 2

---

## Question 10
**Weight ของ Vector Search ใน Hybrid Search คือเท่าไร?**

- a) 0.3
- b) 0.5
- c) 0.7 ✓
- d) 0.9

**Answer: c) 0.7**

**Explanation:**
Hybrid Search รวม Vector Search กับ BM25 (Keyword Search):

| Search Type | Weight |
|------------|--------|
| BM25 (Keyword) | 0.3 |
| **Vector (KNN)** | **0.7** |

Vector Search ได้น้ำหนักมากกว่าเพราะเข้าใจ Semantic meaning ได้ดีกว่า

📚 **Reference:** Week 3 Lecture, Lab 2 - Task 4, Lab 4 - Task 4

---

# Week 4: FastAPI + REST API (10 Questions)

---

## Question 1
**HTTP Method ใดใช้สำหรับสร้างข้อมูลใหม่?**

- a) GET
- b) POST ✓
- c) PUT
- d) DELETE

**Answer: b) POST**

**Explanation:**
HTTP Methods (CRUD Operations):

| Method | Action | Example |
|--------|--------|---------|
| GET | Read | Get documents |
| **POST** | **Create** | **Create document** |
| PUT | Update | Update document |
| DELETE | Delete | Delete document |

📚 **Reference:** Week 4 Lecture - "HTTP Methods" slide

---

## Question 2
**HTTP Method ใดใช้สำหรับอ่านข้อมูล?**

- a) GET ✓
- b) POST
- c) PUT
- d) PATCH

**Answer: a) GET**

**Explanation:**
**GET** ใช้สำหรับอ่านข้อมูล (Read operation):

```bash
# Health check
curl http://localhost:9000/health

# Get documents
curl http://localhost:9000/documents
```

📚 **Reference:** Week 4 Lecture - "HTTP Methods" slide

---

## Question 3
**FastAPI ใช้ Library ใดสำหรับ Data validation?**

- a) Marshmallow
- b) Cerberus
- c) Pydantic ✓
- d) Voluptuous

**Answer: c) Pydantic**

**Explanation:**
FastAPI ใช้ **Pydantic** สำหรับ Data Validation:

```python
from pydantic import BaseModel

class SearchRequest(BaseModel):
    query: str
    top_k: int = 5

@app.post("/search")
def search(request: SearchRequest):
    # Pydantic validates automatically
    return {"results": []}
```

ข้อดีของ Pydantic:
- Automatic validation
- Type coercion
- Clear error messages

📚 **Reference:** Week 4 Lecture - "Why FastAPI?" slide, "FastAPI Example" slide

---

## Question 4
**Swagger UI ของ FastAPI เข้าถึงได้จาก Path ใด?**

- a) /api
- b) /swagger
- c) /docs ✓
- d) /documentation

**Answer: c) /docs**

**Explanation:**
FastAPI สร้าง Documentation อัตโนมัติ:

- **Swagger UI:** `http://localhost:9000/docs`
- **ReDoc:** `http://localhost:9000/redoc`

สามารถทดสอบ API ได้โดยตรงจาก Swagger UI

📚 **Reference:** Week 4 Lecture - "Why FastAPI?" slide, Lab 3 - Task 4

---

## Question 5
**ข้อใดไม่ใช่ข้อดีของ FastAPI?**

- a) High performance
- b) Auto documentation
- c) ต้องเขียน Code มากกว่า Flask ✓
- d) Native async support

**Answer: c) ต้องเขียน Code มากกว่า Flask**

**Explanation:**
ข้อดีของ FastAPI:
- **Fast** - High performance
- **Easy** - ไม่ต้องเขียน code มาก
- **Auto Docs** - Swagger UI อัตโนมัติ
- **Type Hints** - Pydantic validation
- **Async** - Native support

ข้อ c) **ไม่ใช่ข้อดี** และ**ไม่จริง** - FastAPI เขียน code น้อยกว่า Flask เพราะมี auto validation และ auto docs

📚 **Reference:** Week 4 Lecture - "Why FastAPI?" slide

---

## Question 6
**Server ของ Generic-RAG รันบน Port ใด?**

- a) 8000
- b) 8080
- c) 9000 ✓
- d) 5000

**Answer: c) 9000**

**Explanation:**
Generic-RAG API รันบน **Port 9000**:

```bash
python api.py
# Server runs on http://localhost:9000
```

Endpoints:
- `http://localhost:9000/health`
- `http://localhost:9000/search`
- `http://localhost:9000/docs`

📚 **Reference:** Week 4 Lecture, Lab 3 - Task 2

---

## Question 7
**ในการกำหนด default value ของ top_k เป็น 5 เขียนอย่างไร?**

- a) top_k: int
- b) top_k: int = 5 ✓
- c) top_k = int(5)
- d) top_k: default(5)

**Answer: b) top_k: int = 5**

**Explanation:**
Python Type Hints พร้อม Default Value:

```python
class SearchRequest(BaseModel):
    query: str           # Required field
    top_k: int = 5       # Optional with default = 5
```

- `query: str` - ต้องระบุ
- `top_k: int = 5` - ถ้าไม่ระบุจะใช้ค่า 5

📚 **Reference:** Week 4 Lecture - "FastAPI Example" slide

---

## Question 8
**HTTP Method ใดใช้สำหรับลบข้อมูล?**

- a) GET
- b) POST
- c) REMOVE
- d) DELETE ✓

**Answer: d) DELETE**

**Explanation:**
**DELETE** ใช้สำหรับลบข้อมูล:

| Method | Action |
|--------|--------|
| GET | Read |
| POST | Create |
| PUT | Update (all) |
| PATCH | Update (partial) |
| **DELETE** | **Delete** |

📚 **Reference:** Week 4 Lecture - "HTTP Methods" slide

---

## Question 9
**Endpoint /health ใช้ทำอะไร?**

- a) ลบข้อมูล
- b) ตรวจสอบสถานะของ Server ✓
- c) ค้นหาข้อมูล
- d) อัปเดตข้อมูล

**Answer: b) ตรวจสอบสถานะของ Server**

**Explanation:**
`/health` เป็น Health Check Endpoint ใช้ตรวจสอบว่า Server ทำงานปกติ:

```python
@app.get("/health")
def health():
    return {"status": "healthy"}
```

```bash
curl http://localhost:9000/health
# {"status": "healthy"}
```

📚 **Reference:** Week 4 Lecture - "FastAPI Example" slide, Lab 3 - Task 3

---

## Question 10
**HTTP Method ใดใช้สำหรับอัปเดตข้อมูลทั้งหมด?**

- a) GET
- b) POST
- c) PUT ✓
- d) PATCH

**Answer: c) PUT**

**Explanation:**
ความแตกต่างระหว่าง PUT และ PATCH:

| Method | Usage |
|--------|-------|
| **PUT** | **Update ข้อมูลทั้งหมด (Full update)** |
| PATCH | Update เฉพาะบางส่วน (Partial update) |

📚 **Reference:** Week 4 Lecture - "HTTP Methods" slide

---

# Week 5: OpenSearch Integration (10 Questions)

---

## Question 1
**Vector Search ทำงานโดยใช้หลักการใด?**

- a) Exact matching
- b) Term frequency
- c) Semantic similarity ✓
- d) Alphabetical order

**Answer: c) Semantic similarity**

**Explanation:**
**Vector Search** ทำงานโดยใช้ **Semantic Similarity**:

- แปลงข้อความเป็น Vector (Embedding)
- ค้นหา Vector ที่คล้ายกันในฐานข้อมูล
- เข้าใจ "ความหมาย" ไม่ใช่แค่คำที่ตรงกัน

เช่น ค้นหา "รถยนต์" สามารถหา "automobile" หรือ "car" ได้

📚 **Reference:** Week 5 Lecture - "Vector vs Keyword Search" slide

---

## Question 2
**BM25 เป็นอัลกอริทึมสำหรับการค้นหาแบบใด?**

- a) Vector search
- b) Keyword search ✓
- c) Image search
- d) Voice search

**Answer: b) Keyword search**

**Explanation:**
**BM25** (Best Match 25) เป็นอัลกอริทึมสำหรับ **Keyword Search**:

- ใช้ Term Frequency (TF)
- ใช้ Inverse Document Frequency (IDF)
- จับคู่คำที่ตรงกัน (Lexical matching)

📚 **Reference:** Week 5 Lecture - "Vector vs Keyword Search" slide, Lab 4 - Task 4

---

## Question 3
**Hybrid Search คืออะไร?**

- a) การค้นหาด้วย Vector เท่านั้น
- b) การค้นหาด้วย Keyword เท่านั้น
- c) การรวม Vector Search และ Keyword Search ✓
- d) การค้นหาแบบ Real-time

**Answer: c) การรวม Vector Search และ Keyword Search**

**Explanation:**
**Hybrid Search** = Vector Search + Keyword Search (BM25)

| Component | Weight | Strength |
|-----------|--------|----------|
| BM25 | 0.3 | Exact matching, Fast |
| Vector | 0.7 | Semantic understanding |

ได้ประโยชน์จากทั้งสองวิธี!

📚 **Reference:** Week 5 Lecture - "Vector vs Keyword Search" slide

---

## Question 4
**ใน Index settings ต้องเปิด Feature ใดเพื่อใช้งาน Vector search?**

- a) fts: true
- b) knn: true ✓
- c) vector: true
- d) search: true

**Answer: b) knn: true**

**Explanation:**
ต้องเปิด **knn: true** ใน Index Settings:

```python
index_body = {
    "settings": {
        "index": {
            "knn": True  # เปิดใช้งาน Vector Search
        }
    },
    "mappings": {...}
}
```

KNN = K-Nearest Neighbors (อัลกอริทึมค้นหา Vector ที่ใกล้เคียง)

📚 **Reference:** Week 5 Lecture - "Create Index" slide, Lab 4 - Task 2

---

## Question 5
**Python library สำหรับเชื่อมต่อ OpenSearch คืออะไร?**

- a) opensearch-client
- b) opensearchpy ✓
- c) opensearch-connector
- d) pyopensearch

**Answer: b) opensearchpy**

**Explanation:**
ใช้ **opensearchpy** library:

```python
from opensearchpy import OpenSearch

client = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],
    use_ssl=False
)

print(client.info())
```

📚 **Reference:** Week 5 Lecture - "Connect to OpenSearch" slide, Lab 4 - Task 1

---

## Question 6
**Field type สำหรับเก็บ Vector ใน OpenSearch คืออะไร?**

- a) vector_field
- b) dense_vector
- c) knn_vector ✓
- d) embedding_field

**Answer: c) knn_vector**

**Explanation:**
ใช้ **knn_vector** type สำหรับเก็บ Embeddings:

```python
"mappings": {
    "properties": {
        "content": {"type": "text"},
        "content_vector": {
            "type": "knn_vector",
            "dimension": 1024  # ตาม embedding model
        }
    }
}
```

📚 **Reference:** Week 5 Lecture - "Create Index" slide, Lab 4 - Task 2

---

## Question 7
**ข้อดีของ Keyword Search (BM25) คืออะไร?**

- a) เข้าใจความหมาย
- b) ค้นหาแบบ Exact matching และรวดเร็ว ✓
- c) ค้นหาตาม Context
- d) ไม่ต้องใช้ Index

**Answer: b) ค้นหาแบบ Exact matching และรวดเร็ว**

**Explanation:**
ข้อดีของ **BM25 (Keyword Search)**:
- ✅ Exact matching
- ✅ รวดเร็ว
- ✅ ไม่ต้องใช้ Embedding model

ข้อเสีย:
- ❌ ไม่เข้าใจ Semantic meaning
- ❌ พลาดคำที่มีความหมายเหมือนกันแต่เขียนต่างกัน

📚 **Reference:** Week 5 Lecture - "Vector vs Keyword Search" slide

---

## Question 8
**ข้อใดคือข้อเสียของ Keyword Search?**

- a) ช้าเกินไป
- b) ใช้ Memory มาก
- c) พลาดความหมายเชิง Semantic ✓
- d) ต้องใช้ GPU

**Answer: c) พลาดความหมายเชิง Semantic**

**Explanation:**
**ข้อเสียของ Keyword Search:**
- พลาด Semantic meaning
- เช่น ค้นหา "รถยนต์" จะไม่เจอ "automobile" หรือ "vehicle"

นี่คือเหตุผลที่ต้องใช้ **Hybrid Search** รวมกับ Vector Search

📚 **Reference:** Week 5 Lecture - "Vector vs Keyword Search" slide

---

## Question 9
**Weight ของ BM25 ใน Hybrid Search Pipeline คือเท่าไร?**

- a) 0.3 ✓
- b) 0.5
- c) 0.7
- d) 0.9

**Answer: a) 0.3**

**Explanation:**
Hybrid Search Weights:

| Search Type | Weight |
|------------|--------|
| **BM25 (Keyword)** | **0.3** |
| Vector (KNN) | 0.7 |

BM25 ได้น้ำหนักน้อยกว่าเพราะ Vector Search เข้าใจความหมายได้ดีกว่า

📚 **Reference:** Lab 2 - Task 4, Lab 4 - Task 4

---

## Question 10
**คำสั่งใดใช้สร้าง Index ใน OpenSearch?**

- a) client.create(index="docs", body=index_body)
- b) client.indices.create(index="docs", body=index_body) ✓
- c) client.index.new(name="docs", settings=index_body)
- d) client.new_index(index="docs", body=index_body)

**Answer: b) client.indices.create(index="docs", body=index_body)**

**Explanation:**
```python
from opensearchpy import OpenSearch

client = OpenSearch(...)

index_body = {
    "settings": {"index": {"knn": True}},
    "mappings": {...}
}

# สร้าง Index
client.indices.create(index="documents", body=index_body)
```

📚 **Reference:** Week 5 Lecture - "Create Index" slide, Lab 4 - Task 2

---

# Week 6: Embeddings + Document Indexing (10 Questions)

---

## Question 1
**Embedding คืออะไร?**

- a) การบีบอัดไฟล์
- b) การแปลงข้อความเป็น Vector ✓
- c) การเข้ารหัสข้อมูล
- d) การสำรองข้อมูล

**Answer: b) การแปลงข้อความเป็น Vector**

**Explanation:**
**Embedding** = การแปลงข้อความเป็น Vector ตัวเลข

```python
# ข้อความ
text = "Hello"

# Embedding
vector = [0.12, -0.34, 0.56, ...]  # 1024 dimensions
```

ข้อความที่มีความหมายคล้ายกันจะมี Vector ที่คล้ายกัน

📚 **Reference:** Week 6 Lecture - "What are Embeddings?" slide

---

## Question 2
**Model bge-m3 สร้าง Vector ขนาดกี่มิติ?**

- a) 512
- b) 768
- c) 1024 ✓
- d) 2048

**Answer: c) 1024**

**Explanation:**
**BAAI/bge-m3** สร้าง Vector ขนาด **1024 dimensions**:

```python
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-m3",
    trust_remote_code=True
)

vector = embed_model.get_text_embedding("Hello")
print(len(vector))  # 1024
```

📚 **Reference:** Week 6 Lecture - "Embedding Models" slide, "HuggingFace Embedding" slide

---

## Question 3
**ข้อใดถูกต้องเกี่ยวกับ Embedding?**

- a) ข้อความที่คล้ายกันจะมี Vector ที่แตกต่างกัน
- b) ข้อความที่คล้ายกันจะมี Vector ที่คล้ายกัน ✓
- c) ทุกข้อความมี Vector เหมือนกัน
- d) Vector ไม่มีความสัมพันธ์กับความหมาย

**Answer: b) ข้อความที่คล้ายกันจะมี Vector ที่คล้ายกัน**

**Explanation:**
หลักการของ Embedding:
- **Similar texts → Similar vectors**
- ใช้ Cosine Similarity หรือ Euclidean Distance วัดความคล้าย

เช่น:
- "รถยนต์" และ "automobile" จะมี Vector ใกล้เคียงกัน
- "รถยนต์" และ "อาหาร" จะมี Vector ห่างกัน

📚 **Reference:** Week 6 Lecture - "What are Embeddings?" slide

---

## Question 4
**Library ใดใช้สำหรับสร้าง Embedding แบบ Local?**

- a) OpenAI
- b) Google AI
- c) HuggingFaceEmbedding ✓
- d) Azure Cognitive

**Answer: c) HuggingFaceEmbedding**

**Explanation:**
ใช้ **HuggingFaceEmbedding** จาก LlamaIndex:

```python
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-m3",
    trust_remote_code=True
)

# Create embedding - No API Key!
vector = embed_model.get_text_embedding("Hello")
```

รันได้ Local ไม่ต้องใช้ API Key!

📚 **Reference:** Week 6 Lecture - "HuggingFace Embedding" slide

---

## Question 5
**Document Chunking คืออะไร?**

- a) การลบเอกสาร
- b) การรวมเอกสาร
- c) การแบ่งเอกสารเป็นส่วนย่อย ✓
- d) การเข้ารหัสเอกสาร

**Answer: c) การแบ่งเอกสารเป็นส่วนย่อย**

**Explanation:**
**Chunking** = แบ่งเอกสารยาวเป็นชิ้นเล็กๆ (Chunks)

เหตุผล:
- Embedding model มี limit จำนวน tokens
- Chunks เล็กให้ผลลัพธ์ที่แม่นยำกว่า

📚 **Reference:** Week 6 Lecture - "Chunking" slide

---

## Question 6
**SentenceSplitter ใช้พารามิเตอร์ใดกำหนดขนาดของ Chunk?**

- a) size
- b) chunk_size ✓
- c) max_length
- d) split_size

**Answer: b) chunk_size**

**Explanation:**
```python
from llama_index.core.node_parser import SentenceSplitter

splitter = SentenceSplitter(
    chunk_size=1024,     # ขนาด chunk (characters)
    chunk_overlap=200    # ส่วนที่ซ้อนทับกัน
)

chunks = splitter.split_text(document_text)
```

📚 **Reference:** Week 6 Lecture - "Chunking" slide

---

## Question 7
**chunk_overlap ใช้ทำอะไร?**

- a) กำหนดขนาด Chunk
- b) กำหนดจำนวน Chunk
- c) กำหนดส่วนที่ซ้อนทับกันระหว่าง Chunk ✓
- d) กำหนด Encoding

**Answer: c) กำหนดส่วนที่ซ้อนทับกันระหว่าง Chunk**

**Explanation:**
**chunk_overlap** กำหนดส่วนที่ซ้อนทับระหว่าง Chunks:

```python
SentenceSplitter(
    chunk_size=1024,
    chunk_overlap=200  # 200 characters overlap
)
```

ช่วยให้ไม่สูญเสีย context ตรงรอยต่อของ chunks

📚 **Reference:** Week 6 Lecture - "Chunking" slide

---

## Question 8
**OpenAI ada-002 มี Embedding dimension เท่าไร?**

- a) 1024
- b) 1536 ✓
- c) 2048
- d) 4096

**Answer: b) 1536**

**Explanation:**
เปรียบเทียบ Embedding Models:

| Model | Dimensions | Type |
|-------|-----------|------|
| OpenAI ada-002 | **1536** | Cloud |
| BAAI/bge-m3 | 1024 | Local |

📚 **Reference:** Week 6 Lecture - "Embedding Models" slide

---

## Question 9
**ข้อดีของ bge-m3 เมื่อเทียบกับ OpenAI ada-002 คืออะไร?**

- a) มี Dimension มากกว่า
- b) รันบน Cloud เท่านั้น
- c) ไม่ต้องใช้ API Key ✓
- d) รองรับภาษาอังกฤษเท่านั้น

**Answer: c) ไม่ต้องใช้ API Key**

**Explanation:**
ข้อดีของ **bge-m3**:
- ✅ รันได้ Local - **ไม่ต้องใช้ API Key**
- ✅ ฟรี ไม่มีค่าใช้จ่าย
- ✅ รองรับหลายภาษา (Multilingual)
- ✅ ข้อมูลไม่ถูกส่งไป Cloud

📚 **Reference:** Week 6 Lecture - "Embedding Models" slide

---

## Question 10
**ไฟล์เอกสารที่ใช้ใน Generic-RAG เก็บอยู่ในโฟลเดอร์ใด?**

- a) documents/
- b) data/
- c) md_corpus/ ✓
- d) files/

**Answer: c) md_corpus/**

**Explanation:**
เอกสาร Markdown (.md) เก็บในโฟลเดอร์ **md_corpus/**:

```bash
Generic-RAG/
├── md_corpus/       # เอกสารทั้งหมด
│   ├── doc1.md
│   ├── doc2.md
│   └── ...
├── embedding.py
└── api.py
```

📚 **Reference:** Lab 5 - Task 1, Task 4-5

---

# Week 7: Local LLM + RAG Pipeline + Streamlit (10 Questions)

---

## Question 1
**Ollama คืออะไร?**

- a) Cloud LLM Service
- b) Local LLM Runtime ✓
- c) Vector Database
- d) Web Framework

**Answer: b) Local LLM Runtime**

**Explanation:**
**Ollama** คือ **Local LLM Runtime**:
- รัน LLM บนเครื่องของตนเอง
- ไม่ต้องใช้ API Key
- ฟรี ใช้งานไม่จำกัด
- ข้อมูลอยู่ในเครื่อง

```bash
# ดาวน์โหลดโมเดล
ollama pull qwen2.5:7b

# รันโมเดล
ollama run qwen2.5:7b
```

📚 **Reference:** Week 7 Lecture - "What is Ollama?" slide, Lab 6 - Task 1-2

---

*(หมายเหตุ: ข้อมูล Question 1 ของ Week 7 ถูกตัดไปในเอกสารต้นฉบับ แต่ได้เพิ่ม Explanation จากข้อมูลที่มี)*

---

## Summary

### Total Questions: 70+ Questions (Weeks 1-7)

### Topics Covered:
- **Week 1:** Introduction to RAG, Local LLM, Tech Stack
- **Week 2:** Git Commands, Python Fundamentals, Conda
- **Week 3:** Docker, OpenSearch, Hybrid Search Pipeline
- **Week 4:** FastAPI, REST API, HTTP Methods, Pydantic
- **Week 5:** Vector Search, Keyword Search, OpenSearch Integration
- **Week 6:** Embeddings, Document Chunking, bge-m3
- **Week 7:** Ollama, RAG Pipeline, Streamlit

### Key References:
- Lecture slides from `/presentations/lectures/`
- Lab materials from `/presentations/labs/tex/`

---

*Generated for https://wayground.com*
*CSI403 - Full Stack RAG with Local LLM*
*Sripatum University*
