"""
PDF to Video - Lab 03: FastAPI
"""
import asyncio
import edge_tts
from pathlib import Path
from pdf2image import convert_from_path
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

PDF_FILE = "lab03.pdf"
OUTPUT_VIDEO = "lab03-fastapi.mp4"
VOICE = "th-TH-NiwatNeural"
RATE = "-15%"
DPI = 200

SCRIPTS = [
    """สวัสดีครับ... ยินดีต้อนรับเข้าสู่ แล็บที่ 3 เรื่อง ฟาสต์เอพีไอ...
    แล็บนี้มีคะแนน 3.75 เปอร์เซ็นต์ครับ...
    เราจะเรียนรู้การสร้าง REST API ด้วย ฟาสต์เอพีไอ""",
    
    """วัตถุประสงค์ของแล็บนี้ครับ...
    ข้อแรก... ศึกษาไฟล์ api.py จาก Generic-RAG...
    ข้อสอง... รัน ฟาสต์เอพีไอ เซิร์ฟเวอร์...
    ข้อสาม... ทดสอบ เอพีไอ เอนด์พอยท์ ต่างๆ...
    รีโพซิทอรี่คือ github.com/amornpan/Generic-RAG ครับ""",
    
    """ทาสค์แรก... ศึกษาโครงสร้าง api.py ครับ...
    ดูการสร้าง ฟาสต์เอพีไอ แอป...
    ดู Pydantic โมเดล สำหรับ validation...
    และดู เอนด์พอยท์ ต่างๆ... /health, /search, /query ครับ""",
    
    """ทาสค์ที่ 2... รัน เซิร์ฟเวอร์ครับ...
    เข้าไปในโฟลเดอร์ Generic-RAG...
    แอคทิเวท rag_env...
    แล้วพิมพ์ python api.py...
    เซิร์ฟเวอร์จะรันที่ http://localhost:9000 ครับ""",
    
    """ทาสค์ที่ 3... ทดสอบ เอนด์พอยท์ครับ...
    ใช้ curl ทดสอบ /health ก่อน...
    แล้วทดสอบ /search ด้วย POST request...
    ส่ง JSON body ที่มี query และ top_k ครับ""",
    
    """ทาสค์ที่ 4... เปิด Swagger Docs ครับ...
    เข้า http://localhost:9000/docs ในเบราว์เซอร์...
    จะเห็น Interactive API documentation...
    สามารถทดสอบ เอนด์พอยท์ ได้ตรงนี้เลย...
    และดู รีเควสต์ รีสปอนส์ สคีมา ได้ครับ""",
    
    """ทาสค์ที่ 5... เพิ่ม เอนด์พอยท์ใหม่ครับ...
    สร้าง /documents เอนด์พอยท์ สำหรับลิสต์เอกสารทั้งหมด...
    ใช้ @app.get decorator...
    Query โอเพ่นเสิร์ช ด้วย match_all...
    แล้ว return ผลลัพธ์กลับไปครับ""",
    
    """สิ่งที่ต้องส่งครับ...
    เซิร์ฟเวอร์รันได้... เอนด์พอยท์ทดสอบผ่าน...
    เพิ่ม เอนด์พอยท์ใหม่แล้ว... พร้อมถ่ายหน้าจอ...
    เดดไลน์ วันอาทิตย์ 23:59 ครับ!""",
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
    print(f"🎬 Lab 03: FastAPI")
    if not Path(PDF_FILE).exists():
        print(f"❌ ไม่พบ {PDF_FILE}")
        return
    await generate_all_audio()
    num = convert_pdf_to_images()
    create_video(min(num, len(SCRIPTS)))

if __name__ == "__main__":
    asyncio.run(main())
