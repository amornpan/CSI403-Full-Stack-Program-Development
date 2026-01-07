"""
PDF to Video - Week 03: Docker + OpenSearch
"""
import asyncio
import edge_tts
from pathlib import Path
from pdf2image import convert_from_path
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

PDF_FILE = "week03-docker-opensearch.pdf"
OUTPUT_VIDEO = "week03-docker-opensearch-lecture.mp4"
VOICE = "th-TH-NiwatNeural"
RATE = "-15%"
DPI = 200

SCRIPTS = [
    """สวัสดีครับ สัปดาห์ที่ 3 เรื่อง Docker และ OpenSearch...
    วันนี้เราจะเรียนรู้ Containerization...
    และ Vector Database ที่ใช้ในระบบ RAG ครับ""",
    
    """หัวข้อวันนี้ครับ...
    Docker Fundamentals พื้นฐาน ด็อกเกอร์...
    OpenSearch Introduction รู้จักกับ โอเพ่นเสิร์ช...
    และ Lab 2 ครับ""",
    
    """ทำไมต้องใช้ Docker ครับ...
    Works on my machine syndrome...
    บ่อยครั้งที่โค้ดรันได้ที่เครื่องเรา แต่ไม่ได้ที่เครื่องอื่น...
    Docker แก้ปัญหานี้โดยบรรจุทุกอย่างไว้ใน Container...
    ย้ายไปที่ไหนก็ทำงานเหมือนกันครับ""",
    
    """คำสั่ง Docker พื้นฐานครับ...
    docker pull ดาวน์โหลด image...
    docker run รัน container...
    docker ps ดู container ที่กำลังรัน...
    docker stop หยุด container...
    docker rm ลบ container ครับ""",
    
    """OpenSearch คืออะไรครับ...
    เป็น Search Engine ที่รองรับ Vector Search...
    พัฒนาต่อจาก Elasticsearch...
    เหมาะสำหรับทำ Semantic Search ในระบบ RAG...
    เก็บทั้ง Text และ Vector ได้ในที่เดียวครับ""",
    
    """Hybrid Search คืออะไรครับ...
    รวม Vector Search กับ BM25 เข้าด้วยกัน...
    Vector Search ดูความหมาย Semantic...
    BM25 ดูคำที่ตรงกัน Keyword...
    รวมกันได้ผลลัพธ์ที่ดีกว่าครับ""",
    
    """การรัน OpenSearch ด้วย Docker ครับ...
    ใช้คำสั่ง docker run...
    เปิดพอร์ต 9200 สำหรับ REST API...
    ตั้งค่า discovery.type เป็น single-node...
    รอสักครู่ก็พร้อมใช้งานครับ""",
    
    """Lab 2 ครับ คะแนน 3.75 เปอร์เซ็นต์...
    ติดตั้ง Docker Desktop...
    รัน OpenSearch container...
    ตั้งค่า Hybrid Search Pipeline...
    ทดสอบการเชื่อมต่อ...
    เดดไลน์ วันอาทิตย์ 23:59 ครับ""",
    
    """มีคำถามไหมครับ?...
    แล้วเจอกันในแล็บ 2 นะครับ!""",
]

async def generate_audio(text, output_file):
    communicate = edge_tts.Communicate(text, VOICE, rate=RATE)
    await communicate.save(output_file)

async def generate_all_audio():
    Path("audio").mkdir(exist_ok=True)
    print("🎤 สร้างเสียง...")
    for i, script in enumerate(SCRIPTS, 1):
        await generate_audio(script, f"audio/slide_{i:02d}.mp3")
        print(f"  ✅ Slide {i}/{len(SCRIPTS)}")

def convert_pdf_to_images():
    Path("images").mkdir(exist_ok=True)
    print("🖼️ แปลง PDF...")
    images = convert_from_path(PDF_FILE, dpi=DPI)
    for i, img in enumerate(images, 1):
        img.save(f"images/slide_{i:02d}.png", "PNG")
    return len(images)

def create_video(num_slides):
    print("🎬 สร้างวีดีโอ...")
    clips = []
    for i in range(1, num_slides + 1):
        img, aud = f"images/slide_{i:02d}.png", f"audio/slide_{i:02d}.mp3"
        if Path(aud).exists():
            audio = AudioFileClip(aud)
            clip = ImageClip(img).set_duration(audio.duration).set_audio(audio)
        else:
            clip = ImageClip(img).set_duration(5)
        clips.append(clip)
    final = concatenate_videoclips(clips, method="compose")
    final.write_videofile(OUTPUT_VIDEO, fps=24, codec="libx264", audio_codec="aac", verbose=False, logger=None)
    final.close()
    print(f"✅ {OUTPUT_VIDEO}")

async def main():
    print(f"🎬 Week 03: Docker + OpenSearch")
    if not Path(PDF_FILE).exists():
        print(f"❌ ไม่พบ {PDF_FILE}")
        return
    await generate_all_audio()
    num = convert_pdf_to_images()
    create_video(min(num, len(SCRIPTS)))

if __name__ == "__main__":
    asyncio.run(main())
