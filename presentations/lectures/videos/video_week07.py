"""
PDF to Video - Week 07: RAG + LLM + Streamlit
"""
import asyncio
import edge_tts
from pathlib import Path
from pdf2image import convert_from_path
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

PDF_FILE = "week07-rag-llm-streamlit.pdf"
OUTPUT_VIDEO = "week07-rag-llm-streamlit-lecture.mp4"
VOICE = "th-TH-NiwatNeural"
RATE = "-15%"
DPI = 200

SCRIPTS = [
    """สวัสดีครับ สัปดาห์ที่ 7 เรื่อง RAG + LLM + Streamlit...
    วันนี้เราจะประกอบทุกอย่างเข้าด้วยกัน...
    สร้างระบบ RAG ที่สมบูรณ์ครับ""",
    
    """หัวข้อวันนี้ครับ...
    Ollama Local LLM...
    RAG Pipeline ครบวงจร...
    Streamlit UI...
    และ Lab 6 ครับ""",
    
    """Ollama คืออะไรครับ...
    เป็นเครื่องมือรัน LLM บนเครื่องตัวเอง...
    ฟรี ไม่ต้องใช้ API Key...
    รองรับหลาย Models เช่น qwen llama mistral...
    ใช้งานง่ายด้วย Command Line ครับ""",
    
    """qwen2.5:7b Model ครับ...
    7 พันล้าน Parameters...
    ใช้ RAM ประมาณ 8 GB...
    คุณภาพดี ตอบภาษาไทยได้...
    เหมาะสำหรับเรียนรู้และพัฒนาครับ""",
    
    """RAG Pipeline ครบวงจรครับ...
    User ถามคำถาม...
    Search หาเอกสารที่เกี่ยวข้องจาก OpenSearch...
    Retrieve ดึง context ที่เกี่ยวข้อง...
    Generate LLM สร้างคำตอบจาก context...
    Response ส่งคำตอบกลับไปให้ User ครับ""",
    
    """Streamlit คืออะไรครับ...
    Framework สำหรับสร้าง Web UI ด้วย Python...
    เขียนง่าย ไม่ต้องรู้ HTML CSS JS...
    เหมาะสำหรับ Data Apps และ AI Apps...
    Deploy ง่าย รันด้วยคำสั่งเดียวครับ""",
    
    """Prompt Engineering ครับ...
    การออกแบบ Prompt ให้ LLM ตอบได้ดี...
    ระบุ Context ให้ชัดเจน...
    กำหนดรูปแบบคำตอบที่ต้องการ...
    บอกข้อจำกัดเช่น ตอบจาก context เท่านั้นครับ""",
    
    """Lab 6 ครับ คะแนน 3.75 เปอร์เซ็นต์...
    ติดตั้ง Ollama และดาวน์โหลด Model...
    รัน API ที่เชื่อมกับ LLM...
    รัน Streamlit UI...
    ทดสอบระบบ RAG ครบวงจร...
    เดดไลน์ วันอาทิตย์ 23:59 ครับ""",
    
    """มีคำถามไหมครับ?...
    แล็บนี้สนุกมาก ได้เห็น AI ตอบคำถามจากเอกสารเรา!...
    แล้วเจอกันในแล็บ 6 นะครับ!""",
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
    print(f"🎬 Week 07: RAG + LLM + Streamlit")
    if not Path(PDF_FILE).exists():
        print(f"❌ ไม่พบ {PDF_FILE}")
        return
    await generate_all_audio()
    num = convert_pdf_to_images()
    create_video(min(num, len(SCRIPTS)))

if __name__ == "__main__":
    asyncio.run(main())
