# Lab 01: Python Basics for RAG System

## 📋 ข้อมูล Lab

| หัวข้อ | รายละเอียด |
|--------|------------|
| **วิชา** | CSI403 - Full Stack RAG with Local LLM |
| **Lab** | Lab 01 |
| **หัวข้อ** | Python Basics for RAG |
| **คะแนน** | 100 คะแนน |
| **รูปแบบ** | Jupyter Notebook (.ipynb) |

---

## 🎯 วัตถุประสงค์

เมื่อทำ Lab นี้เสร็จ นักศึกษาจะ:

1. ✅ เข้าใจ Data Types พื้นฐาน (string, list, dictionary)
2. ✅ เข้าใจ Function และ Class เบื้องต้น
3. ✅ สามารถสร้าง Document class สำหรับระบบ RAG
4. ✅ สามารถทำ Text Processing พื้นฐาน

---

## 🚀 วิธีทำ Lab

### ขั้นตอนที่ 1: Clone Repository

```bash
git clone <URL ของ repo>
cd lab01-python-basics-<username>
```

### ขั้นตอนที่ 2: เปิด Jupyter Notebook

```bash
# ติดตั้ง Jupyter (ถ้ายังไม่มี)
pip install jupyter

# เปิด Notebook
jupyter notebook Lab01_Python_Basics_for_RAG.ipynb
```

หรือใช้ **VS Code** กับ extension "Jupyter"

### ขั้นตอนที่ 3: ทำแบบฝึกหัด

- อ่านคำอธิบายในแต่ละ cell
- รันตัวอย่าง code
- ทำแบบฝึกหัด (หา `# TODO:` และ `___`)
- รัน cell เพื่อทดสอบ

### ขั้นตอนที่ 4: Submit

```bash
git add .
git commit -m "Complete Lab 01"
git push
```

---

## 📊 โครงสร้าง Lab

```
Part 1: Python Basics Review (20 คะแนน)
├── 1.1 String
├── 1.2 List
└── 1.3 Dictionary

Part 2: Function (20 คะแนน)
├── 2.1 get_summary()
└── 2.2 chunk_text()

Part 3: Class (30 คะแนน)
└── 3.1 Document class

Part 4: Document Processing (30 คะแนน)
├── 4.1 process_documents()
└── 4.2 search_documents()
```

---

## 📚 เนื้อหาที่เรียน

### RAG System Architecture

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   📄 เอกสาร   │───▶│  🔍 ค้นหา   │───▶│  🤖 AI ตอบ  │
│  (Documents) │    │  (Retrieve)  │    │  (Generate) │
└─────────────┘    └─────────────┘    └─────────────┘
```

### Document Class

```python
class Document:
    def __init__(self, title, content, source=None):
        self.title = title
        self.content = content
        self.source = source
        self.word_count = len(content.split())
    
    def get_summary(self, max_length=100):
        # Return truncated content
        ...
    
    def to_dict(self):
        # Return dictionary representation
        ...
```

---

## ❓ FAQ

### Q: ไม่เคยเขียน Python มาก่อน ทำได้ไหม?
A: Lab นี้ออกแบบมาสำหรับผู้เริ่มต้น มีตัวอย่างและคำอธิบายทุกขั้นตอน

### Q: จะรู้ได้ยังไงว่าทำถูก?
A: รัน cell ทดสอบ ถ้าไม่มี error และแสดงผลถูกต้อง แสดงว่าทำถูก

### Q: ใช้ AI ช่วยได้ไหม?
A: ได้ แต่ต้องเข้าใจโค้ดที่เขียน เพราะจะมีคำถามในชั้นเรียน

---

## 📖 แหล่งเรียนรู้เพิ่มเติม

- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Jupyter Notebook Guide](https://jupyter.org/documentation)
- [W3Schools Python](https://www.w3schools.com/python/)

---

**© 2026 CSI403 - Full Stack RAG with Local LLM**
