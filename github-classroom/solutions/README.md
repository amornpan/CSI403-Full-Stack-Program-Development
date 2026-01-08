# 📚 Solutions - เฉลย Lab ทั้งหมด

> ⚠️ **สำหรับอาจารย์เท่านั้น - ห้ามแจกนักศึกษา!**

---

## 📁 โครงสร้างโฟลเดอร์

```
solutions/
├── README.md           ← ไฟล์นี้
├── week02/
│   ├── document_solution.py      ← เฉลย Document class
│   └── rag_config_solution.py    ← เฉลย RAG Config
├── week03/                       ← (เพิ่มภายหลัง)
├── week04/                       ← (เพิ่มภายหลัง)
└── ...
```

---

## 📝 Week 02 Solutions

### document_solution.py

| TODO | คำตอบ | คะแนน |
|------|-------|-------|
| TODO 1 | `self.word_count = len(content.split())` | 15 |
| TODO 2 | `if len(...) <= max_length: return ... else: return ...[:max_length] + "..."` | 15 |
| TODO 3 | `return self.word_count` | 10 |
| TODO 4 | `return {"title": ..., "content": ..., "source": ..., "word_count": ...}` | 10 |

### rag_config_solution.py

| TODO | คำตอบ | คะแนน |
|------|-------|-------|
| TODO 1 | `protocol = "https" if self.use_ssl else "http"` + `return f"{protocol}://{self.host}:{self.port}"` | 15 |
| TODO 2 | `return f"{self.base_url}/api/generate"` | 10 |

---

## 🔑 Key Concepts ที่นักศึกษาควรเรียนรู้

### Week 02

1. **OOP Basics**
   - Class และ Object
   - `__init__` constructor
   - Instance variables (`self.xxx`)
   - Methods

2. **Python Built-ins**
   - `str.split()` - แยก string เป็น list
   - `len()` - นับจำนวน elements
   - String slicing `[:]`

3. **Type Hints**
   - `Optional[str]` - อาจเป็น None
   - `Dict[str, Any]` - dictionary
   - `-> str` - return type

4. **Dataclass**
   - `@dataclass` decorator
   - Default values
   - `@property` decorator
   - `__post_init__`

5. **F-strings**
   - `f"Hello {name}"`
   - String formatting

---

## 🧪 วิธีทดสอบเฉลย

```bash
cd solutions/week02

# ทดสอบ document
python document_solution.py

# ทดสอบ config
python rag_config_solution.py
```

---

## 📋 Checklist สำหรับตรวจงาน

### Week 02

- [ ] `word_count` คำนวณถูกต้อง
- [ ] `get_summary()` ตัด string ถูกต้อง
- [ ] `get_summary()` เพิ่ม "..." เมื่อ content ยาว
- [ ] `get_word_count()` return ค่าถูกต้อง
- [ ] `to_dict()` return dictionary ครบทุก keys
- [ ] `url` property สร้าง URL ถูกต้อง
- [ ] `url` เลือก http/https ตาม use_ssl
- [ ] `generate_url` ต่อ path ถูกต้อง
- [ ] มี commits >= 3 ครั้ง

---

## 📌 หมายเหตุ

- เฉลยมี comments อธิบายทุกบรรทัด
- สามารถใช้เป็น reference สำหรับสอน
- นักศึกษาอาจเขียนต่างจากเฉลยได้ ถ้าผล output ถูกต้อง
