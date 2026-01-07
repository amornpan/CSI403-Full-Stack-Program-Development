"""
PDF to Video - Week 05: OpenSearch Integration
"""
import asyncio
import edge_tts
from pathlib import Path
from pdf2image import convert_from_path
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

PDF_FILE = "week05-opensearch.pdf"
OUTPUT_VIDEO = "week05-opensearch-lecture.mp4"
VOICE = "th-TH-NiwatNeural"
RATE = "-15%"
DPI = 200

SCRIPTS = [
    """สวัสดีครับ สัปดาห์ที่ 5 เรื่อง OpenSearch Integration...
    วันนี้เราจะเรียนรู้การเชื่อมต่อ Python กับ OpenSearch...
    และทำ Vector Search ครับ""",
    
    """หัวข้อวันนี้ครับ...
    OpenSearch Python Client...
    Index Creation การสร้าง Index...
    Vector Search การค้นหาด้วย Vector...
    และ Lab 4 ครับ""",
    
    """การเชื่อมต่อ OpenSearch จาก Python ครับ...
    ใช้ library opensearch-py...
    สร้าง client ด้วย host และ port...
    ทดสอบด้วย client.info()...
    ถ้าได้ JSON กลับมาแสดงว่าเชื่อมต่อสำเร็จครับ""",
    
    """การสร้าง Index ครับ...
    Index เปรียบเหมือนตารางใน Database...
    กำหนด mappings สำหรับ fields...
    content เป็น text สำหรับ BM25 search...
    content_vector เป็น knn_vector สำหรับ Vector search...
    dimension ต้องตรงกับ embedding model ครับ""",
    
    """KNN Vector คืออะไรครับ...
    KNN ย่อมาจาก K-Nearest Neighbors...
    ค้นหา vectors ที่ใกล้เคียงกันมากที่สุด...
    ใช้ cosine similarity วัดความคล้าย...
    เหมาะสำหรับ Semantic Search ครับ""",
    
    """การ Index Documents ครับ...
    สร้าง document ที่มี content และ content_vector...
    ใช้ client.index เพิ่มเข้า index...
    vector ต้องมีขนาดตรงกับที่กำหนดไว้...
    สำหรับ bge-m3 คือ 1024 dimensions ครับ""",
    
    """Hybrid Search ครับ...
    รวม Vector Search กับ BM25...
    Vector Search หาความหมาย น้ำหนัก 70 เปอร์เซ็นต์...
    BM25 หาคำที่ตรงกัน น้ำหนัก 30 เปอร์เซ็นต์...
    ผลลัพธ์ดีกว่าใช้อย่างใดอย่างหนึ่งครับ""",
    
    """Lab 4 ครับ คะแนน 3.75 เปอร์เซ็นต์...
    เชื่อมต่อ OpenSearch จาก Python...
    สร้าง Index...
    Index Documents...
    ทำ Hybrid Search...
    เดดไลน์ วันอาทิตย์ 23:59 ครับ""",
    
    """มีคำถามไหมครับ?...
    แล้วเจอกันในแล็บ 4 นะครับ!""",
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
    print(f"🎬 Week 05: OpenSearch Integration")
    if not Path(PDF_FILE).exists():
        print(f"❌ ไม่พบ {PDF_FILE}")
        return
    await generate_all_audio()
    num = convert_pdf_to_images()
    create_video(min(num, len(SCRIPTS)))

if __name__ == "__main__":
    asyncio.run(main())
