"""
PDF to Video - Week 04: FastAPI
"""
import asyncio
import edge_tts
from pathlib import Path
from pdf2image import convert_from_path
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

PDF_FILE = "week04-fastapi.pdf"
OUTPUT_VIDEO = "week04-fastapi-lecture.mp4"
VOICE = "th-TH-NiwatNeural"
RATE = "-15%"
DPI = 200

SCRIPTS = [
    """สวัสดีครับ สัปดาห์ที่ 4 เรื่อง FastAPI...
    วันนี้เราจะเรียนรู้การสร้าง REST API...
    ด้วย FastAPI framework ที่ทันสมัยและรวดเร็วครับ""",
    
    """หัวข้อวันนี้ครับ...
    REST API คืออะไร...
    FastAPI Introduction รู้จัก FastAPI...
    Pydantic สำหรับ Data Validation...
    และ Lab 3 ครับ""",
    
    """REST API คืออะไรครับ...
    เป็นรูปแบบการสื่อสารระหว่าง Client กับ Server...
    ใช้ HTTP Methods เช่น GET POST PUT DELETE...
    ส่งข้อมูลในรูปแบบ JSON...
    Stateless ไม่เก็บ state ระหว่าง request ครับ""",
    
    """ทำไมต้อง FastAPI ครับ...
    เร็วมาก เทียบเท่า NodeJS และ Go...
    สร้าง API Documentation อัตโนมัติ...
    Validate ข้อมูลอัตโนมัติด้วย Pydantic...
    รองรับ Async/Await...
    เขียนง่าย อ่านง่ายครับ""",
    
    """โครงสร้าง FastAPI App ครับ...
    import FastAPI แล้วสร้าง app instance...
    ใช้ decorator @app.get หรือ @app.post...
    กำหนด path เช่น /health หรือ /search...
    function จะถูกเรียกเมื่อมี request มาที่ path นั้นครับ""",
    
    """Pydantic คืออะไรครับ...
    Library สำหรับ Data Validation...
    สร้าง Schema กำหนดโครงสร้างข้อมูล...
    ตรวจสอบ Type อัตโนมัติ...
    แปลง JSON เป็น Python Object ได้ง่ายครับ""",
    
    """Swagger Documentation ครับ...
    FastAPI สร้าง API Docs อัตโนมัติ...
    เข้าถึงได้ที่ /docs...
    ทดสอบ API ได้ในหน้าเว็บเลย...
    ดู Request Response Schema ได้ครับ""",
    
    """Lab 3 ครับ คะแนน 3.75 เปอร์เซ็นต์...
    ศึกษา api.py จาก Generic-RAG...
    รัน FastAPI Server...
    ทดสอบ Endpoints...
    เพิ่ม Endpoint ใหม่...
    เดดไลน์ วันอาทิตย์ 23:59 ครับ""",
    
    """มีคำถามไหมครับ?...
    แล้วเจอกันในแล็บ 3 นะครับ!""",
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
    print(f"🎬 Week 04: FastAPI")
    if not Path(PDF_FILE).exists():
        print(f"❌ ไม่พบ {PDF_FILE}")
        return
    await generate_all_audio()
    num = convert_pdf_to_images()
    create_video(min(num, len(SCRIPTS)))

if __name__ == "__main__":
    asyncio.run(main())
