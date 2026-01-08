# Week 05: OpenSearch Integration (Lab 04)

## 📋 ข้อมูลทั่วไป

| หัวข้อ | รายละเอียด |
|--------|------------|
| **วิชา** | CSI403 - Full Stack RAG with Local LLM |
| **Week** | Week 05 |
| **Lab** | Lab 04 |
| **หัวข้อ** | OpenSearch Integration + Hybrid Search |
| **คะแนน** | 3.75% |
| **Deadline** | ดูใน GitHub Classroom |

---

## 🎯 วัตถุประสงค์

เมื่อทำ Lab นี้เสร็จ นักศึกษาจะสามารถ:

1. เชื่อมต่อ Python กับ OpenSearch ได้
2. สร้างและจัดการ Index ได้
3. ทำ CRUD operations กับ OpenSearch ได้
4. Implement Hybrid Search (BM25 + Vector) ได้

---

## 📝 งานที่ต้องทำ

### Task 1: OpenSearch Client (40 คะแนน)

เปิดไฟล์ `src/opensearch_client.py` และทำตาม TODO:

1. **TODO 1**: Implement `index_document()` - เพิ่ม document ลง index
2. **TODO 2**: Implement `get_document()` - ดึง document จาก id
3. **TODO 3**: Implement `delete_document()` - ลบ document
4. **TODO 4**: Implement `search_bm25()` - ค้นหาแบบ BM25

### Task 2: Hybrid Search (40 คะแนน)

เปิดไฟล์ `src/hybrid_search.py` และทำตาม TODO:

1. **TODO 1**: Implement `vector_search()` - ค้นหาด้วย vector
2. **TODO 2**: Implement `hybrid_search()` - รวม BM25 + Vector
3. **TODO 3**: Implement `rerank_results()` - จัดอันดับผลลัพธ์ใหม่

### Task 3: ทดสอบและ Screenshot (10 คะแนน)

1. รัน OpenSearch ด้วย Docker
2. รัน tests และถ่าย screenshot

### Task 4: เขียน README ส่วน "สิ่งที่เรียนรู้" (10 คะแนน)

---

## 🚀 วิธีทำ Lab

### ขั้นตอนที่ 1: รัน OpenSearch

```bash
# ใช้ docker-compose จาก Week 03 หรือ
docker run -d -p 9200:9200 -p 9600:9600 \
  -e "discovery.type=single-node" \
  -e "DISABLE_SECURITY_PLUGIN=true" \
  opensearchproject/opensearch:2.11.1
```

### ขั้นตอนที่ 2: Clone และ Setup

```bash
git clone <URL ของ repo คุณ>
cd week05-opensearch-integration-<username>

python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### ขั้นตอนที่ 3: ทำ Tasks

แก้ไขไฟล์ `src/opensearch_client.py` และ `src/hybrid_search.py`

### ขั้นตอนที่ 4: รัน Tests

```bash
pytest tests/ -v
```

### ขั้นตอนที่ 5: ทดสอบด้วยตัวเอง

```bash
python src/opensearch_client.py
python src/hybrid_search.py
```

---

## ✅ เกณฑ์การให้คะแนน (Rubric)

| เกณฑ์ | คะแนน | รายละเอียด |
|-------|-------|------------|
| **Task 1: opensearch_client.py** | 40 | CRUD operations ทำงานถูกต้อง |
| **Task 2: hybrid_search.py** | 40 | Hybrid search ทำงานถูกต้อง |
| **Task 3: Screenshots** | 10 | test results screenshot |
| **Task 4: README** | 10 | เขียนสิ่งที่เรียนรู้ |
| **รวม** | **100** | |

---

## 📚 สิ่งที่เรียนรู้

> **[นักศึกษาเขียนส่วนนี้]**
> 
> เขียนอธิบายสิ่งที่ได้เรียนรู้จากการทำ Lab นี้ เช่น:
> - OpenSearch query DSL
> - BM25 vs Vector search
> - Hybrid search concept
> - ปัญหาที่เจอและวิธีแก้ไข
> 
> (ลบข้อความนี้แล้วเขียนของตัวเอง)

---

## 📖 แหล่งเรียนรู้เพิ่มเติม

- [OpenSearch Python Client](https://opensearch.org/docs/latest/clients/python/)
- [OpenSearch Query DSL](https://opensearch.org/docs/latest/query-dsl/)
- [Hybrid Search](https://opensearch.org/docs/latest/search-plugins/hybrid-search/)

---

## ❓ ต้องการความช่วยเหลือ?

- ถามใน LINE กลุ่มวิชา
- เปิด Issue ใน Repository นี้
- พบอาจารย์ในชั่วโมง Office Hours

---

**© 2026 CSI403 - Full Stack RAG with Local LLM**
