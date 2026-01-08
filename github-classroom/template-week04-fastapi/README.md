# Week 04: FastAPI (Lab 03)

## 📋 ข้อมูลทั่วไป

| หัวข้อ | รายละเอียด |
|--------|------------|
| **วิชา** | CSI403 - Full Stack RAG with Local LLM |
| **Week** | Week 04 |
| **Lab** | Lab 03 |
| **หัวข้อ** | FastAPI + REST API |
| **คะแนน** | 3.75% |
| **Deadline** | ดูใน GitHub Classroom |

---

## 🎯 วัตถุประสงค์

เมื่อทำ Lab นี้เสร็จ นักศึกษาจะสามารถ:

1. สร้าง REST API ด้วย FastAPI ได้
2. ใช้ Pydantic สำหรับ data validation ได้
3. สร้าง CRUD endpoints ได้
4. ใช้งาน Swagger UI ได้

---

## 📝 งานที่ต้องทำ

### Task 1: สร้าง Pydantic Models (30 คะแนน)

เปิดไฟล์ `src/models.py` และทำตาม TODO:

1. **TODO 1**: สร้าง `DocumentCreate` model
2. **TODO 2**: สร้าง `DocumentResponse` model  
3. **TODO 3**: สร้าง `SearchRequest` model
4. **TODO 4**: สร้าง `SearchResponse` model

### Task 2: สร้าง API Endpoints (50 คะแนน)

เปิดไฟล์ `src/api.py` และทำตาม TODO:

1. **TODO 1**: Implement `GET /health` endpoint
2. **TODO 2**: Implement `GET /documents` endpoint
3. **TODO 3**: Implement `POST /documents` endpoint
4. **TODO 4**: Implement `GET /documents/{doc_id}` endpoint
5. **TODO 5**: Implement `DELETE /documents/{doc_id}` endpoint

### Task 3: Screenshot Swagger UI (10 คะแนน)

1. รัน API server
2. เปิด http://localhost:9000/docs
3. ถ่าย screenshot

### Task 4: เขียน README ส่วน "สิ่งที่เรียนรู้" (10 คะแนน)

---

## 🚀 วิธีทำ Lab

### ขั้นตอนที่ 1: Clone Repository

```bash
git clone <URL ของ repo คุณ>
cd week04-fastapi-<username>
```

### ขั้นตอนที่ 2: สร้าง Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt
```

### ขั้นตอนที่ 3: ทำ Task ตามที่กำหนด

แก้ไขไฟล์ `src/models.py` และ `src/api.py`

### ขั้นตอนที่ 4: รัน API Server

```bash
python src/api.py
```

### ขั้นตอนที่ 5: ทดสอบ API

```bash
# Health check
curl http://localhost:9000/health

# List documents
curl http://localhost:9000/documents

# Create document
curl -X POST http://localhost:9000/documents \
  -H "Content-Type: application/json" \
  -d '{"title": "Test", "content": "Hello World"}'
```

### ขั้นตอนที่ 6: เปิด Swagger UI

เปิด browser ไปที่: http://localhost:9000/docs

### ขั้นตอนที่ 7: รัน Tests

```bash
pytest tests/ -v
```

---

## ✅ เกณฑ์การให้คะแนน (Rubric)

| เกณฑ์ | คะแนน | รายละเอียด |
|-------|-------|------------|
| **Task 1: models.py** | 30 | Pydantic models ถูกต้อง |
| **Task 2: api.py** | 50 | Endpoints ทำงานถูกต้อง |
| **Task 3: Screenshots** | 10 | Swagger UI screenshot |
| **Task 4: README** | 10 | เขียนสิ่งที่เรียนรู้ |
| **รวม** | **100** | |

---

## 📚 สิ่งที่เรียนรู้

> **[นักศึกษาเขียนส่วนนี้]**
> 
> เขียนอธิบายสิ่งที่ได้เรียนรู้จากการทำ Lab นี้ เช่น:
> - FastAPI concepts
> - Pydantic validation
> - REST API design
> - HTTP methods และ status codes
> 
> (ลบข้อความนี้แล้วเขียนของตัวเอง)

---

## 📖 แหล่งเรียนรู้เพิ่มเติม

- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [Pydantic Documentation](https://docs.pydantic.dev)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

---

## ❓ ต้องการความช่วยเหลือ?

- ถามใน LINE กลุ่มวิชา
- เปิด Issue ใน Repository นี้
- พบอาจารย์ในชั่วโมง Office Hours

---

**© 2026 CSI403 - Full Stack RAG with Local LLM**
