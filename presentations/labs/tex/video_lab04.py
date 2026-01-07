"""
PDF to Video - Lab 04: OpenSearch Integration
"""
import asyncio
import edge_tts
from pathlib import Path
from pdf2image import convert_from_path
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

PDF_FILE = "lab04.pdf"
OUTPUT_VIDEO = "lab04-opensearch-integration.mp4"
VOICE = "th-TH-NiwatNeural"
RATE = "-15%"
DPI = 200

SCRIPTS = [
    """สวัสดีครับ... แล็บที่ 4 เรื่อง โอเพ่นเสิร์ช อินทิเกรชัน...
    คะแนน 3.75 เปอร์เซ็นต์ครับ...
    เราจะเชื่อมต่อ ไพธอน กับ โอเพ่นเสิร์ช และทำ ไฮบริด เสิร์ช""",
    
    """วัตถุประสงค์ครับ...
    เชื่อมต่อ โอเพ่นเสิร์ช จาก ไพธอน...
    สร้าง อินเด็กซ์ สำหรับเก็บเอกสาร...
    อินเด็กซ์ เอกสารลงไป...
    และทำ ไฮบริด เสิร์ช ครับ""",
    
    """ทาสค์แรก... เชื่อมต่อ โอเพ่นเสิร์ชครับ...
    อิมพอร์ต OpenSearch จาก opensearchpy...
    สร้าง ไคลเอนต์ ด้วย host localhost พอร์ต 9200...
    use_ssl เป็น False เพราะเราปิด security ไว้...
    ทดสอบด้วย client.info() ครับ""",
    
    """ทาสค์ที่ 2... สร้าง อินเด็กซ์ครับ...
    กำหนด settings ให้ knn เป็น True...
    ใน mappings มี properties สองตัว...
    content เป็น text สำหรับ BM25...
    content_vector เป็น knn_vector ขนาด 1024 มิติ...
    แล้วเรียก client.indices.create ครับ""",
    
    """ทาสค์ที่ 3... อินเด็กซ์ เอกสารครับ...
    สร้าง doc ที่มี content และ content_vector...
    content_vector ต้องมี 1024 มิติ ตรงกับ bge-m3 โมเดล...
    ใช้ client.index เพื่อใส่เอกสารลงไป...
    ระวัง... มิติของ เวกเตอร์ ต้องตรงกับที่กำหนดไว้ครับ""",
    
    """ทาสค์ที่ 4... ทำ ไฮบริด เสิร์ชครับ...
    รวม เวกเตอร์ เสิร์ช กับ BM25 เข้าด้วยกัน...
    เวกเตอร์ เสิร์ช ดูความหมาย... น้ำหนัก 70 เปอร์เซ็นต์...
    BM25 ดูคำที่ตรงกัน... น้ำหนัก 30 เปอร์เซ็นต์...
    ผลลัพธ์จะดีกว่าใช้อย่างใดอย่างหนึ่งครับ""",
    
    """สิ่งที่ต้องส่งครับ...
    เชื่อมต่อ โอเพ่นเสิร์ช ได้...
    สร้าง อินเด็กซ์ แล้ว...
    อินเด็กซ์ เอกสารแล้ว...
    เสิร์ช ทำงานได้...
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
    print(f"🎬 Lab 04: OpenSearch Integration")
    if not Path(PDF_FILE).exists():
        print(f"❌ ไม่พบ {PDF_FILE}")
        return
    await generate_all_audio()
    num = convert_pdf_to_images()
    create_video(min(num, len(SCRIPTS)))

if __name__ == "__main__":
    asyncio.run(main())
