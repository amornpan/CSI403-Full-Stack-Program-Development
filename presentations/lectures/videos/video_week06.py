"""
PDF to Video - Week 06: Embeddings
"""
import asyncio
import edge_tts
from pathlib import Path
from pdf2image import convert_from_path
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

PDF_FILE = "week06-embeddings.pdf"
OUTPUT_VIDEO = "week06-embeddings-lecture.mp4"
VOICE = "th-TH-NiwatNeural"
RATE = "-15%"
DPI = 200

SCRIPTS = [
    """สวัสดีครับ สัปดาห์ที่ 6 เรื่อง Embeddings...
    วันนี้เราจะเรียนรู้การสร้าง Vector Embeddings...
    ซึ่งเป็นหัวใจสำคัญของระบบ RAG ครับ""",
    
    """หัวข้อวันนี้ครับ...
    Embeddings คืออะไร...
    Chunking การแบ่งเอกสาร...
    bge-m3 Model...
    และ Lab 5 ครับ""",
    
    """Embeddings คืออะไรครับ...
    คือการแปลงข้อความเป็น Vector ตัวเลข...
    ข้อความที่มีความหมายคล้ายกัน จะมี Vector ใกล้กัน...
    ใช้สำหรับค้นหาความหมาย ไม่ใช่แค่คำที่ตรงกันครับ""",
    
    """Chunking คืออะไรครับ...
    การแบ่งเอกสารยาวๆ เป็นส่วนเล็กๆ...
    เพราะ Embedding model มีขีดจำกัด token...
    Chunk ที่ดีควรมีความหมายครบในตัวเอง...
    มี overlap กันเล็กน้อยเพื่อรักษา context ครับ""",
    
    """bge-m3 Model ครับ...
    เป็น Embedding model จาก BAAI...
    รองรับหลายภาษา รวมถึงภาษาไทย...
    สร้าง Vector 1024 dimensions...
    ทำงานได้ที่เครื่อง ไม่ต้องใช้ API ครับ""",
    
    """Indexing Pipeline ครับ...
    โหลดเอกสารจากโฟลเดอร์...
    Chunk เอกสารเป็นส่วนย่อย...
    สร้าง Embeddings ด้วย bge-m3...
    Index ลง OpenSearch...
    ทำครั้งเดียว ใช้ได้ตลอดครับ""",
    
    """Lab 5 ครับ คะแนน 3.75 เปอร์เซ็นต์...
    รัน embedding.py...
    ตรวจสอบจำนวนเอกสารใน Index...
    เพิ่มเอกสารใหม่...
    ทดสอบ Search...
    เดดไลน์ วันอาทิตย์ 23:59 ครับ""",
    
    """มีคำถามไหมครับ?...
    แล้วเจอกันในแล็บ 5 นะครับ!""",
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
    print(f"🎬 Week 06: Embeddings")
    if not Path(PDF_FILE).exists():
        print(f"❌ ไม่พบ {PDF_FILE}")
        return
    await generate_all_audio()
    num = convert_pdf_to_images()
    create_video(min(num, len(SCRIPTS)))

if __name__ == "__main__":
    asyncio.run(main())
