# 🎬 Video Generator for Full-Stack RAG Course

สร้างวีดีโอบรรยายจาก PDF Presentation พร้อมเสียง AI ภาษาไทยอัตโนมัติ

## 📋 สารบัญ

- [ภาพรวม](#-ภาพรวม)
- [ความต้องการระบบ](#-ความต้องการระบบ)
- [การติดตั้ง](#-การติดตั้ง)
- [โครงสร้างโปรเจค](#-โครงสร้างโปรเจค)
- [การสร้างวีดีโอ Lectures](#-การสร้างวีดีโอ-lectures)
- [การสร้างวีดีโอ Labs](#-การสร้างวีดีโอ-labs)
- [การปรับแต่ง](#-การปรับแต่ง)
- [การแก้ไขปัญหา](#-การแก้ไขปัญหา)

---

## 🎯 ภาพรวม

ระบบนี้แปลง PDF Slides เป็นวีดีโอพร้อมเสียง AI ภาษาไทยอัตโนมัติ ประกอบด้วย:

| ประเภท | จำนวน | คำอธิบาย |
|--------|-------|----------|
| **Lecture Videos** | 9 สัปดาห์ | วีดีโอบรรยายเนื้อหาทฤษฎี |
| **Lab Videos** | 8 แล็บ | วีดีโออธิบายขั้นตอนปฏิบัติ |

### ✨ Features

- 🎤 **AI Voice ภาษาไทย** - ใช้ Edge TTS (Microsoft) เสียงเหมือนคนจริง
- 📄 **PDF to Video** - แปลง PDF เป็นวีดีโอพร้อมเสียงบรรยาย
- ⚡ **Batch Processing** - สร้างหลายวีดีโอพร้อมกันได้
- 🆓 **ฟรี!** - ไม่มีค่าใช้จ่าย ไม่ต้องสมัคร API

---

## 💻 ความต้องการระบบ

### ซอฟต์แวร์ที่ต้องมี

| Software | Version | Download |
|----------|---------|----------|
| Windows | 10/11 | - |
| Anaconda/Miniconda | Latest | [Download](https://docs.conda.io/en/latest/miniconda.html) |
| MiKTeX (LaTeX) | Latest | [Download](https://miktex.org/download) |
| Internet | - | สำหรับ Edge TTS |

### ฮาร์ดแวร์แนะนำ

- **RAM**: 8 GB ขึ้นไป
- **Storage**: 10 GB ว่าง (สำหรับวีดีโอ output)
- **CPU**: 4 cores ขึ้นไป

---

## 🚀 การติดตั้ง

### ขั้นตอนที่ 1: Clone Repository

```bash
git clone https://github.com/amornpan/Full-Stack-RAG-with-Local-LLM.git
cd Full-Stack-RAG-with-Local-LLM
```

### ขั้นตอนที่ 2: สร้าง Conda Environment

```bash
# สร้าง environment ใหม่
conda create -n video-generator python=3.11 -y

# เปิดใช้งาน
conda activate video-generator

# ติดตั้ง dependencies
conda install -c conda-forge poppler ffmpeg moviepy pdf2image pillow -y
pip install edge-tts pydub
```

หรือใช้ไฟล์ environment.yml:

```bash
# สร้างไฟล์ environment.yml
cat > environment.yml << EOF
name: video-generator
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.11
  - pip
  - numpy
  - pillow
  - poppler
  - pdf2image
  - ffmpeg
  - moviepy
  - pip:
    - edge-tts>=6.1.0
    - pydub>=0.25.0
EOF

# สร้าง environment
conda env create -f environment.yml
```

### ขั้นตอนที่ 3: ติดตั้ง LaTeX Packages (ถ้ายังไม่มี)

```bash
cd presentations/labs/tex
install-packages.bat
```

---

## 📁 โครงสร้างโปรเจค

```
Full-Stack-RAG-with-Local-LLM/
├── presentations/
│   ├── lectures/                    # Lecture slides
│   │   ├── week01/
│   │   │   └── week01-intro-rag.pdf
│   │   ├── week02/
│   │   │   └── week02-git-python.pdf
│   │   ├── ... (week03-week09)
│   │   │
│   │   └── videos/                  # 📹 Lecture video scripts
│   │       ├── build-video.bat      # Menu สร้างวีดีโอ
│   │       ├── video_week01.py
│   │       ├── video_week02.py
│   │       └── ... (video_week03-09.py)
│   │
│   └── labs/                        # Lab slides
│       ├── tex/                     # LaTeX source files
│       │   ├── lab01.tex - lab08.tex
│       │   ├── build-all.bat        # Build all PDFs
│       │   ├── build-video.bat      # Menu สร้างวีดีโอ
│       │   ├── video_lab01.py
│       │   └── ... (video_lab02-08.py)
│       │
│       └── pdf/                     # Generated PDFs
│           └── lab01.pdf - lab08.pdf
```

---

## 📺 การสร้างวีดีโอ Lectures

### ขั้นตอนที่ 1: ตรวจสอบ PDF

ตรวจสอบว่ามีไฟล์ PDF ในแต่ละโฟลเดอร์ week:

```
lectures/week01/week01-intro-rag.pdf
lectures/week02/week02-git-python.pdf
lectures/week03/week03-docker-opensearch.pdf
lectures/week04/week04-fastapi.pdf
lectures/week05/week05-opensearch.pdf
lectures/week06/week06-embeddings.pdf
lectures/week07/week07-rag-llm-streamlit.pdf
lectures/week08/week08-docker-compose.pdf
lectures/week09/week09-cicd.pdf
```

ถ้ายังไม่มี ให้ build จาก .tex ก่อน:

```bash
cd presentations/lectures/week01
pdflatex week01-intro-rag.tex
```

### ขั้นตอนที่ 2: สร้างวีดีโอ

```bash
# เปิด Anaconda Prompt
conda activate video-generator

# ไปที่โฟลเดอร์ videos
cd C:\Users\Asus\test\Full-Stack-RAG-with-Local-LLM\presentations\lectures\videos

# รัน menu
build-video.bat
```

### ขั้นตอนที่ 3: เลือก Option

```
============================================
  Lecture Video Generator
============================================

Select option:
  [1] Build Week 01 video (Intro to RAG)
  [2] Build Week 02 video (Git + Python)
  [3] Build Week 03 video (Docker + OpenSearch)
  [4] Build Week 04 video (FastAPI)
  [5] Build Week 05 video (OpenSearch Integration)
  [6] Build Week 06 video (Embeddings)
  [7] Build Week 07 video (RAG + LLM + Streamlit)
  [8] Build Week 08 video (Docker Compose)
  [9] Build Week 09 video (CI/CD)
  [A] Build ALL lecture videos
  [0] Exit

Enter choice (0-9, A): _
```

### Output Files

```
lectures/videos/
├── week01-intro-rag-lecture.mp4
├── week02-git-python-lecture.mp4
├── week03-docker-opensearch-lecture.mp4
├── week04-fastapi-lecture.mp4
├── week05-opensearch-lecture.mp4
├── week06-embeddings-lecture.mp4
├── week07-rag-llm-streamlit-lecture.mp4
├── week08-docker-compose-lecture.mp4
└── week09-cicd-lecture.mp4
```

---

## 🔬 การสร้างวีดีโอ Labs

### ขั้นตอนที่ 1: Build PDF จาก LaTeX

```bash
# เปิด Command Prompt (ไม่ต้อง conda)
cd C:\Users\Asus\test\Full-Stack-RAG-with-Local-LLM\presentations\labs\tex

# Build all PDFs
build-all.bat
```

จะได้ไฟล์ PDF ในโฟลเดอร์ `pdf/`:
- lab01.pdf - lab08.pdf

### ขั้นตอนที่ 2: สร้างวีดีโอ

```bash
# เปิด Anaconda Prompt
conda activate video-generator

# ไปที่โฟลเดอร์ tex
cd C:\Users\Asus\test\Full-Stack-RAG-with-Local-LLM\presentations\labs\tex

# รัน menu
build-video.bat
```

### ขั้นตอนที่ 3: เลือก Option

```
============================================
  Lab Video Generator
============================================

Select option:
  [1] Build Lab 01 video
  [2] Build Lab 02 video
  ...
  [8] Build Lab 08 video
  [9] Build ALL lab videos
  [0] Exit

Enter choice (0-9): _
```

### Output Files

```
labs/tex/videos/
├── lab01-git-python.mp4
├── lab02-docker-opensearch.mp4
├── lab03-fastapi.mp4
├── lab04-opensearch-integration.mp4
├── lab05-embeddings.mp4
├── lab06-rag-llm-streamlit.mp4
├── lab07-docker-compose.mp4
└── lab08-cicd-testing.mp4
```

---

## ⚙️ การปรับแต่ง

### เปลี่ยนเสียง AI

แก้ไขในไฟล์ `video_*.py`:

```python
# เสียงผู้ชายไทย (default)
VOICE = "th-TH-NiwatNeural"

# เสียงผู้หญิงไทย
VOICE = "th-TH-PremwadeeNeural"

# เสียงผู้ชายอังกฤษ (US)
VOICE = "en-US-GuyNeural"

# เสียงผู้หญิงอังกฤษ (US)
VOICE = "en-US-JennyNeural"
```

### ปรับความเร็วเสียง

```python
RATE = "+0%"    # ปกติ
RATE = "-15%"   # ช้าลง 15% (แนะนำ)
RATE = "-20%"   # ช้าลง 20%
RATE = "+10%"   # เร็วขึ้น 10%
```

### ปรับคุณภาพรูปภาพ

```python
DPI = 150   # คุณภาพต่ำ (ไฟล์เล็ก)
DPI = 200   # คุณภาพกลาง (แนะนำ)
DPI = 300   # คุณภาพสูง (ไฟล์ใหญ่)
```

### แก้ไข Script บรรยาย

แก้ไขใน `SCRIPTS` list:

```python
SCRIPTS = [
    # Slide 1
    """ข้อความที่จะพูดใน slide แรก...
    ใช้ ... เพื่อเพิ่ม pause...""",
    
    # Slide 2
    """ข้อความที่จะพูดใน slide ที่สอง...""",
    
    # ... ต่อไปเรื่อยๆ
]
```

### เทคนิคการเขียน Script

#### 1. เพิ่ม Pause ด้วย `...`

```python
# ❌ ไม่ดี - พูดรัว
"""สวัสดีครับนักศึกษาทุกคนยินดีต้อนรับเข้าสู่การเรียน"""

# ✅ ดี - มี pause
"""สวัสดีครับนักศึกษาทุกคน... ยินดีต้อนรับเข้าสู่การเรียน..."""
```

#### 2. แปลงคำศัพท์อังกฤษเป็นทับศัพท์ไทย

| English | ทับศัพท์ไทย |
|---------|------------|
| Full Stack | ฟูลสแตค |
| Frontend | ฟรอนท์เอนด์ |
| Backend | แบ็คเอนด์ |
| DevOps | เดฟออปส์ |
| CI/CD | ซีไอ ซีดี |
| Docker | ด็อกเกอร์ |
| API | เอพีไอ |
| GitHub | กิตฮับ |
| Database | ดาต้าเบส |
| Deploy | ดีพลอย |

---

## 🔧 การแก้ไขปัญหา

### ปัญหา: conda activate ไม่ได้

```bash
# ใช้ Anaconda Prompt แทน Command Prompt
# หรือ initialize conda ก่อน
conda init cmd.exe
```

### ปัญหา: poppler not found

```bash
conda install -c conda-forge poppler -y
```

### ปัญหา: Network error จาก Edge TTS

- ตรวจสอบ Internet connection
- ลองรันใหม่อีกครั้ง

### ปัญหา: moviepy error

```bash
pip install --upgrade moviepy
pip install imageio==2.31.1
```

### ปัญหา: ไฟล์วีดีโอไม่มีเสียง

- ตรวจสอบว่าไฟล์ใน `audio/` ถูกสร้างครบหรือไม่
- จำนวน script ต้องตรงกับจำนวน slide ใน PDF

### ปัญหา: LaTeX compile error

```bash
# ติดตั้ง packages ที่ขาด
cd presentations/labs/tex
install-packages.bat
```

---

## 📊 ข้อมูลวีดีโอ Output

| Property | Value |
|----------|-------|
| Format | MP4 (H.264 + AAC) |
| Resolution | ตาม PDF (~1920x1080) |
| FPS | 24 |
| ความยาว | 5-15 นาทีต่อวีดีโอ |

---

## 🎤 รายชื่อเสียง AI ที่รองรับ

### ภาษาไทย
| Voice ID | เพศ | คุณภาพ |
|----------|-----|--------|
| `th-TH-NiwatNeural` | ชาย | ⭐⭐⭐⭐⭐ |
| `th-TH-PremwadeeNeural` | หญิง | ⭐⭐⭐⭐⭐ |

### ภาษาอังกฤษ (US)
| Voice ID | เพศ | คุณภาพ |
|----------|-----|--------|
| `en-US-GuyNeural` | ชาย | ⭐⭐⭐⭐⭐ |
| `en-US-JennyNeural` | หญิง | ⭐⭐⭐⭐⭐ |

### ดูรายชื่อเสียงทั้งหมด

```bash
edge-tts --list-voices
```

---

## 📞 ติดต่อ

- **Email**: amornpan@gmail.com
- **GitHub**: https://github.com/amornpan

---

## 📜 License

MIT License - ใช้งานได้อย่างอิสระ

---

## 🙏 Credits

- [Edge TTS](https://github.com/rany2/edge-tts) - Microsoft Edge Text-to-Speech
- [MoviePy](https://zulko.github.io/moviepy/) - Video editing library
- [pdf2image](https://github.com/Belval/pdf2image) - PDF to image converter
- [MiKTeX](https://miktex.org/) - LaTeX distribution
