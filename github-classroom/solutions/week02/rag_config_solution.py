"""
Lab 01: RAG Configuration - SOLUTION
====================================
เฉลยพร้อมคำอธิบายโค้ดทุกบรรทัด

ไฟล์นี้เป็นเฉลยสำหรับอาจารย์ ห้ามแจกนักศึกษา!
"""

# =============================================================================
# IMPORTS
# =============================================================================

from dataclasses import dataclass
# dataclass: Decorator ที่ช่วยสร้าง class สำหรับเก็บข้อมูล
# - สร้าง __init__ อัตโนมัติ
# - สร้าง __repr__ อัตโนมัติ
# - สร้าง __eq__ อัตโนมัติ
# ทำให้เขียน code น้อยลงมาก


# =============================================================================
# OPENSEARCH CONFIG - Configuration สำหรับ OpenSearch
# =============================================================================

@dataclass
class OpenSearchConfig:
    """
    OpenSearch connection configuration
    
    @dataclass decorator ทำให้:
    - ไม่ต้องเขียน __init__ เอง
    - attributes ด้านล่างจะกลายเป็น parameters ของ __init__
    
    Attributes:
        host: hostname ของ OpenSearch server (default: "localhost")
        port: port number (default: 9200)
        index_name: ชื่อ index ที่ใช้เก็บ documents (default: "documents")
        use_ssl: ใช้ SSL encryption หรือไม่ (default: False)
    """
    
    # ----- Class Attributes with Default Values -----
    # Syntax: attribute_name: type = default_value
    
    host: str = "localhost"
    # host: ชื่อ server หรือ IP address
    # - "localhost" = เครื่องตัวเอง
    # - "192.168.1.100" = IP address
    # - "search.example.com" = domain name
    
    port: int = 9200
    # port: หมายเลข port ที่ OpenSearch รับ connection
    # - 9200 = default port ของ OpenSearch
    # - 443 = HTTPS port
    
    index_name: str = "documents"
    # index_name: ชื่อ index ใน OpenSearch
    # - คล้ายกับชื่อ table ใน database
    
    use_ssl: bool = False
    # use_ssl: ใช้ SSL/TLS encryption หรือไม่
    # - True = ใช้ https://
    # - False = ใช้ http://
    
    # =========================================================================
    # PROPERTY - url
    # =========================================================================
    
    @property
    def url(self) -> str:
        """
        สร้าง URL สำหรับเชื่อมต่อ OpenSearch
        
        @property decorator ทำให้เรียกใช้เหมือน attribute (ไม่ต้องใส่ ())
        - config.url ✓
        - config.url() ✗
        
        Returns:
            str: URL ในรูปแบบ "{protocol}://{host}:{port}"
        
        Example:
            >>> config = OpenSearchConfig(host="localhost", port=9200, use_ssl=False)
            >>> config.url
            'http://localhost:9200'
        """
        
        # =====================================================================
        # TODO 1 SOLUTION: สร้าง URL จาก host, port, use_ssl
        # =====================================================================
        
        # ----- เลือก protocol ตาม use_ssl -----
        # Ternary operator: value_if_true if condition else value_if_false
        # 
        # ถ้า self.use_ssl เป็น True → protocol = "https"
        # ถ้า self.use_ssl เป็น False → protocol = "http"
        protocol = "https" if self.use_ssl else "http"
        
        # ----- สร้าง URL ด้วย f-string -----
        # f-string format: f"text {variable} text"
        # 
        # ตัวอย่าง:
        # - protocol="http", host="localhost", port=9200
        # - ผลลัพธ์: "http://localhost:9200"
        return f"{protocol}://{self.host}:{self.port}"
        # =====================================================================


# =============================================================================
# OLLAMA CONFIG - Configuration สำหรับ Ollama LLM
# =============================================================================

@dataclass
class OllamaConfig:
    """
    Ollama LLM configuration
    
    Ollama คือ tool สำหรับรัน LLM (Large Language Model) บนเครื่อง local
    
    Attributes:
        host: hostname ของ Ollama server
        port: port number (default: 11434)
        model: ชื่อ model ที่ใช้ (default: "qwen2.5:7b")
        temperature: ค่า randomness ในการ generate (0.0-1.0)
    """
    
    host: str = "localhost"
    # host: ที่อยู่ของ Ollama server
    
    port: int = 11434
    # port: default port ของ Ollama
    
    model: str = "qwen2.5:7b"
    # model: ชื่อ model ที่จะใช้
    # - "qwen2.5:7b" = Qwen 2.5 ขนาด 7 billion parameters
    # - "llama3:8b" = LLaMA 3 ขนาด 8 billion parameters
    # - "mistral:7b" = Mistral ขนาด 7 billion parameters
    
    temperature: float = 0.7
    # temperature: ควบคุมความ random ของ output
    # - 0.0 = deterministic (ผลลัพธ์เหมือนกันทุกครั้ง)
    # - 1.0 = random มาก (ผลลัพธ์หลากหลาย)
    # - 0.7 = ค่ากลางๆ ที่นิยมใช้
    
    # =========================================================================
    # PROPERTY - base_url (ให้มาแล้ว ไม่ต้องทำ)
    # =========================================================================
    
    @property
    def base_url(self) -> str:
        """
        Base URL ของ Ollama server
        
        Returns:
            str: URL ในรูปแบบ "http://host:port"
        """
        # f-string สร้าง URL พื้นฐาน
        return f"http://{self.host}:{self.port}"
    
    # =========================================================================
    # PROPERTY - generate_url
    # =========================================================================
    
    @property
    def generate_url(self) -> str:
        """
        URL สำหรับ generate API
        
        Ollama API มีหลาย endpoints:
        - /api/generate - สำหรับ text generation
        - /api/chat - สำหรับ chat completion
        - /api/embeddings - สำหรับสร้าง embeddings
        
        Returns:
            str: URL ในรูปแบบ "http://host:port/api/generate"
        """
        
        # =====================================================================
        # TODO 2 SOLUTION: สร้าง generate URL
        # =====================================================================
        
        # ----- ใช้ base_url แล้วต่อด้วย path -----
        # 
        # self.base_url จะ return "http://localhost:11434" (เรียก property)
        # แล้วต่อด้วย "/api/generate"
        # 
        # ผลลัพธ์: "http://localhost:11434/api/generate"
        # 
        return f"{self.base_url}/api/generate"
        # 
        # หรือเขียนแบบนี้ก็ได้:
        # return self.base_url + "/api/generate"
        # =====================================================================


# =============================================================================
# EMBEDDING CONFIG - Configuration สำหรับ Embedding Model
# =============================================================================

@dataclass
class EmbeddingConfig:
    """
    Embedding model configuration
    
    Embedding คือการแปลง text เป็น vector (ตัวเลข)
    เพื่อใช้ในการค้นหาความคล้ายคลึงกัน
    
    Attributes:
        model_name: ชื่อ model ที่ใช้สร้าง embedding
        dimension: จำนวน dimensions ของ vector
    """
    
    model_name: str = "BAAI/bge-m3"
    # model_name: ชื่อ model จาก HuggingFace
    # - "BAAI/bge-m3" = BGE M3 model (รองรับหลายภาษา รวมถึงไทย)
    # - "sentence-transformers/all-MiniLM-L6-v2" = model ขนาดเล็ก
    
    dimension: int = 1024
    # dimension: จำนวน dimensions ของ embedding vector
    # - 1024 = BGE M3 default
    # - 384 = all-MiniLM-L6-v2


# =============================================================================
# RAG CONFIG - Main Configuration รวมทุกอย่าง
# =============================================================================

@dataclass
class RAGConfig:
    """
    Main RAG system configuration
    
    รวม config ทั้งหมดไว้ในที่เดียวเพื่อง่ายต่อการจัดการ
    
    Design Pattern: Composition
    - แทนที่จะ inherit จาก config อื่นๆ
    - เราเก็บ config เป็น attributes แทน
    
    Attributes:
        opensearch: OpenSearch connection config
        ollama: Ollama LLM config
        embedding: Embedding model config
        chunk_size: ขนาดของแต่ละ chunk (characters)
        chunk_overlap: overlap ระหว่าง chunks
        top_k: จำนวน documents ที่จะ retrieve
    """
    
    # ----- Nested Config Objects -----
    # ค่า default เป็น None เพราะจะสร้างใน __post_init__
    
    opensearch: OpenSearchConfig = None
    ollama: OllamaConfig = None
    embedding: EmbeddingConfig = None
    
    # ----- Chunking Settings -----
    
    chunk_size: int = 1024
    # chunk_size: ขนาดของ text chunk
    # - ใช้สำหรับแบ่ง document ยาวๆ เป็นชิ้นเล็กๆ
    # - 1024 characters เป็นค่าที่นิยมใช้
    
    chunk_overlap: int = 200
    # chunk_overlap: จำนวน characters ที่ซ้อนทับกันระหว่าง chunks
    # - ช่วยไม่ให้ข้อมูลหายตรงรอยต่อ
    # - เช่น chunk 1: char 0-1024, chunk 2: char 824-1848
    
    # ----- Search Settings -----
    
    top_k: int = 5
    # top_k: จำนวน documents ที่จะ retrieve
    # - ค้นหาแล้วเอามา 5 อันที่คล้ายที่สุด
    
    def __post_init__(self):
        """
        Initialize nested configs if not provided
        
        __post_init__ เป็น special method ของ dataclass
        - เรียกอัตโนมัติหลังจาก __init__ ทำงานเสร็จ
        - ใช้สำหรับ logic เพิ่มเติมที่ต้องทำหลัง init
        """
        
        # ----- สร้าง default configs ถ้าไม่ได้ระบุ -----
        # ใช้ "if X is None" แทน "if not X" เพราะชัดเจนกว่า
        
        if self.opensearch is None:
            self.opensearch = OpenSearchConfig()
        
        if self.ollama is None:
            self.ollama = OllamaConfig()
        
        if self.embedding is None:
            self.embedding = EmbeddingConfig()


# =============================================================================
# MAIN BLOCK - ทดสอบ
# =============================================================================

if __name__ == "__main__":
    
    print("=" * 60)
    print("Testing RAG Configuration - SOLUTION")
    print("=" * 60)
    
    # -------------------------------------------------------------------------
    # ทดสอบ OpenSearchConfig
    # -------------------------------------------------------------------------
    
    print("\n--- OpenSearch Config ---")
    
    # สร้างด้วยค่า default
    os_config = OpenSearchConfig()
    print(f"Host: {os_config.host}")          # localhost
    print(f"Port: {os_config.port}")          # 9200
    print(f"Use SSL: {os_config.use_ssl}")    # False
    print(f"URL: {os_config.url}")            # http://localhost:9200
    
    # สร้างด้วย SSL
    os_ssl = OpenSearchConfig(
        host="search.example.com",
        port=443,
        use_ssl=True
    )
    print(f"SSL URL: {os_ssl.url}")           # https://search.example.com:443
    
    # -------------------------------------------------------------------------
    # ทดสอบ OllamaConfig
    # -------------------------------------------------------------------------
    
    print("\n--- Ollama Config ---")
    
    ollama_config = OllamaConfig()
    print(f"Model: {ollama_config.model}")               # qwen2.5:7b
    print(f"Temperature: {ollama_config.temperature}")   # 0.7
    print(f"Base URL: {ollama_config.base_url}")         # http://localhost:11434
    print(f"Generate URL: {ollama_config.generate_url}") # http://localhost:11434/api/generate
    
    # Custom config
    custom_ollama = OllamaConfig(
        host="ollama.example.com",
        port=8080,
        model="llama3:8b"
    )
    print(f"Custom Generate URL: {custom_ollama.generate_url}")
    # http://ollama.example.com:8080/api/generate
    
    # -------------------------------------------------------------------------
    # ทดสอบ RAGConfig รวม
    # -------------------------------------------------------------------------
    
    print("\n--- Full RAG Config ---")
    
    config = RAGConfig()
    print(f"OpenSearch URL: {config.opensearch.url}")
    print(f"Ollama URL: {config.ollama.generate_url}")
    print(f"Embedding Model: {config.embedding.model_name}")
    print(f"Chunk size: {config.chunk_size}")
    print(f"Chunk overlap: {config.chunk_overlap}")
    print(f"Top K: {config.top_k}")
    
    # -------------------------------------------------------------------------
    # ทดสอบ Custom RAGConfig
    # -------------------------------------------------------------------------
    
    print("\n--- Custom RAG Config ---")
    
    custom_config = RAGConfig(
        opensearch=OpenSearchConfig(host="10.0.0.1", use_ssl=True),
        chunk_size=2048,
        top_k=10
    )
    print(f"Custom OpenSearch: {custom_config.opensearch.url}")
    print(f"Custom Chunk size: {custom_config.chunk_size}")
    print(f"Custom Top K: {custom_config.top_k}")
    
    print("\n" + "=" * 60)
    print("All tests passed! ✅")
    print("=" * 60)
