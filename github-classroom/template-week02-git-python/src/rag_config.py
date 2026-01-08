"""
Lab 01: RAG Configuration
=========================
เรียนรู้การใช้ dataclass สำหรับ configuration

นักศึกษาต้องทำตาม TODO ที่กำหนด
"""

from dataclasses import dataclass


@dataclass
class OpenSearchConfig:
    """
    OpenSearch connection configuration
    
    Attributes:
        host: hostname ของ OpenSearch server
        port: port number
        index_name: ชื่อ index ที่ใช้
        use_ssl: ใช้ SSL หรือไม่
    
    Example:
        >>> config = OpenSearchConfig()
        >>> config.url
        'http://localhost:9200'
    """
    host: str = "localhost"
    port: int = 9200
    index_name: str = "documents"
    use_ssl: bool = False
    
    @property
    def url(self) -> str:
        """
        สร้าง URL สำหรับเชื่อมต่อ OpenSearch
        
        Returns:
            str: URL ในรูปแบบ "http://host:port" หรือ "https://host:port"
        
        Example:
            >>> config = OpenSearchConfig(host="localhost", port=9200, use_ssl=False)
            >>> config.url
            'http://localhost:9200'
            
            >>> config2 = OpenSearchConfig(host="search.example.com", port=443, use_ssl=True)
            >>> config2.url
            'https://search.example.com:443'
        """
        # TODO 1: Implement property นี้
        # - ถ้า use_ssl เป็น True → ใช้ "https://"
        # - ถ้า use_ssl เป็น False → ใช้ "http://"
        # - รูปแบบ: "{protocol}://{host}:{port}"
        # เขียนโค้ดด้านล่างนี้:
        pass  # ลบบรรทัดนี้แล้วเขียนโค้ด


@dataclass
class OllamaConfig:
    """
    Ollama LLM configuration
    
    Attributes:
        host: hostname ของ Ollama server
        port: port number
        model: ชื่อ model ที่ใช้
        temperature: ค่า temperature สำหรับ generation
    
    Example:
        >>> config = OllamaConfig()
        >>> config.generate_url
        'http://localhost:11434/api/generate'
    """
    host: str = "localhost"
    port: int = 11434
    model: str = "qwen2.5:7b"
    temperature: float = 0.7
    
    @property
    def base_url(self) -> str:
        """Base URL ของ Ollama server"""
        return f"http://{self.host}:{self.port}"
    
    @property
    def generate_url(self) -> str:
        """
        URL สำหรับ generate API
        
        Returns:
            str: URL ในรูปแบบ "http://host:port/api/generate"
        
        Example:
            >>> config = OllamaConfig(host="localhost", port=11434)
            >>> config.generate_url
            'http://localhost:11434/api/generate'
        """
        # TODO 2: Implement property นี้
        # - ใช้ self.base_url แล้วต่อด้วย "/api/generate"
        # เขียนโค้ดด้านล่างนี้:
        pass  # ลบบรรทัดนี้แล้วเขียนโค้ด


@dataclass
class EmbeddingConfig:
    """Embedding model configuration"""
    model_name: str = "BAAI/bge-m3"
    dimension: int = 1024


@dataclass
class RAGConfig:
    """
    Main RAG system configuration
    
    รวม config ทั้งหมดไว้ในที่เดียว
    """
    opensearch: OpenSearchConfig = None
    ollama: OllamaConfig = None
    embedding: EmbeddingConfig = None
    
    # Chunking settings
    chunk_size: int = 1024
    chunk_overlap: int = 200
    
    # Search settings
    top_k: int = 5
    
    def __post_init__(self):
        """Initialize nested configs if not provided"""
        if self.opensearch is None:
            self.opensearch = OpenSearchConfig()
        if self.ollama is None:
            self.ollama = OllamaConfig()
        if self.embedding is None:
            self.embedding = EmbeddingConfig()


# ==========================================
# ส่วนนี้สำหรับทดสอบด้วยตัวเอง
# รัน: python src/rag_config.py
# ==========================================
if __name__ == "__main__":
    print("=" * 50)
    print("Testing RAG Configuration")
    print("=" * 50)
    
    # ทดสอบ OpenSearchConfig
    print("\n--- OpenSearch Config ---")
    os_config = OpenSearchConfig()
    print(f"Host: {os_config.host}")
    print(f"Port: {os_config.port}")
    print(f"URL: {os_config.url}")
    
    # ทดสอบ SSL
    os_ssl = OpenSearchConfig(host="search.example.com", port=443, use_ssl=True)
    print(f"SSL URL: {os_ssl.url}")
    
    # ทดสอบ OllamaConfig
    print("\n--- Ollama Config ---")
    ollama_config = OllamaConfig()
    print(f"Model: {ollama_config.model}")
    print(f"Base URL: {ollama_config.base_url}")
    print(f"Generate URL: {ollama_config.generate_url}")
    
    # ทดสอบ RAGConfig รวม
    print("\n--- Full RAG Config ---")
    config = RAGConfig()
    print(f"OpenSearch: {config.opensearch.url}")
    print(f"Ollama: {config.ollama.generate_url}")
    print(f"Embedding: {config.embedding.model_name}")
    print(f"Chunk size: {config.chunk_size}")
    print(f"Top K: {config.top_k}")
