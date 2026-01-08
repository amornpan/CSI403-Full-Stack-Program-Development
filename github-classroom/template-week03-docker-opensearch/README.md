# Week 03: Docker + OpenSearch (Lab 02)

## 📋 ข้อมูลทั่วไป

| หัวข้อ | รายละเอียด |
|--------|------------|
| **วิชา** | CSI403 - Full Stack RAG with Local LLM |
| **Week** | Week 03 |
| **Lab** | Lab 02 |
| **หัวข้อ** | Docker + OpenSearch |
| **คะแนน** | 3.75% |
| **Deadline** | ดูใน GitHub Classroom |

---

## 🎯 วัตถุประสงค์

เมื่อทำ Lab นี้เสร็จ นักศึกษาจะสามารถ:

1. ติดตั้งและใช้งาน Docker Desktop ได้
2. เขียน docker-compose.yml ได้
3. รัน OpenSearch ด้วย Docker ได้
4. ตั้งค่า Hybrid Search Pipeline ได้

---

## 📝 งานที่ต้องทำ

### Task 1: เขียน docker-compose.yml (40 คะแนน)

เปิดไฟล์ `docker-compose.yml` และทำตาม TODO:

1. **TODO 1**: กำหนด environment variables สำหรับ OpenSearch
2. **TODO 2**: กำหนด ports mapping
3. **TODO 3**: กำหนด healthcheck
4. **TODO 4**: เพิ่ม OpenSearch Dashboards service

### Task 2: เขียน setup_opensearch.py (30 คะแนน)

เปิดไฟล์ `src/setup_opensearch.py` และทำตาม TODO:

1. **TODO 1**: Implement function `check_connection()`
2. **TODO 2**: Implement function `setup_hybrid_search_pipeline()`
3. **TODO 3**: Implement function `create_index()`

### Task 3: ทดสอบและ Screenshot (20 คะแนน)

1. รัน `docker-compose up -d`
2. รัน `python src/setup_opensearch.py`
3. ถ่าย screenshot ผลลัพธ์

### Task 4: เขียน README ส่วน "สิ่งที่เรียนรู้" (10 คะแนน)

---

## 🚀 วิธีทำ Lab

### ขั้นตอนที่ 1: ติดตั้ง Docker Desktop

1. ดาวน์โหลดจาก https://docker.com
2. ติดตั้งและเปิดใช้งาน
3. ตรวจสอบ: `docker --version`

### ขั้นตอนที่ 2: Clone Repository

```bash
git clone <URL ของ repo คุณ>
cd week03-docker-opensearch-<username>
```

### ขั้นตอนที่ 3: แก้ไข docker-compose.yml

ทำตาม TODO ที่ระบุไว้ในไฟล์

### ขั้นตอนที่ 4: รัน OpenSearch

```bash
docker-compose up -d
```

### ขั้นตอนที่ 5: ตรวจสอบว่า OpenSearch ทำงาน

```bash
# ตรวจสอบ containers
docker-compose ps

# ตรวจสอบ OpenSearch
curl http://localhost:9200
```

### ขั้นตอนที่ 6: รัน Setup Script

```bash
pip install -r requirements.txt
python src/setup_opensearch.py
```

### ขั้นตอนที่ 7: รัน Tests

```bash
pytest tests/ -v
```

### ขั้นตอนที่ 8: ถ่าย Screenshots

บันทึก screenshots ไว้ใน `screenshots/`:
- `docker-ps.png` - ผลลัพธ์ `docker-compose ps`
- `opensearch-health.png` - ผลลัพธ์ `curl localhost:9200`
- `setup-complete.png` - ผลลัพธ์ setup script

---

## ✅ เกณฑ์การให้คะแนน (Rubric)

| เกณฑ์ | คะแนน | รายละเอียด |
|-------|-------|------------|
| **Task 1: docker-compose.yml** | 40 | ผ่าน tests + containers รันได้ |
| **Task 2: setup_opensearch.py** | 30 | ผ่าน tests ทั้งหมด |
| **Task 3: Screenshots** | 20 | มี screenshots ครบ 3 รูป |
| **Task 4: README** | 10 | เขียนสิ่งที่เรียนรู้ครบถ้วน |
| **รวม** | **100** | |

---

## 📚 สิ่งที่เรียนรู้

> **[นักศึกษาเขียนส่วนนี้]**
> 
> เขียนอธิบายสิ่งที่ได้เรียนรู้จากการทำ Lab นี้ เช่น:
> - Docker commands ที่ได้ใช้
> - docker-compose.yml structure
> - OpenSearch concepts
> - ปัญหาที่เจอและวิธีแก้ไข
> 
> (ลบข้อความนี้แล้วเขียนของตัวเอง)

---

## 📖 แหล่งเรียนรู้เพิ่มเติม

- [Docker Documentation](https://docs.docker.com)
- [Docker Compose](https://docs.docker.com/compose/)
- [OpenSearch Documentation](https://opensearch.org/docs/latest/)

---

## ⚠️ Troubleshooting

### Docker ไม่ทำงาน
```bash
# ตรวจสอบว่า Docker Desktop เปิดอยู่
docker info
```

### Port 9200 ถูกใช้งาน
```bash
# ตรวจสอบ port
netstat -an | findstr 9200

# หยุด container เก่า
docker-compose down
```

### OpenSearch ไม่ start
```bash
# ดู logs
docker-compose logs opensearch
```

---

## ❓ ต้องการความช่วยเหลือ?

- ถามใน LINE กลุ่มวิชา
- เปิด Issue ใน Repository นี้
- พบอาจารย์ในชั่วโมง Office Hours

---

**© 2026 CSI403 - Full Stack RAG with Local LLM**
