"""
Test cases for Ollama Client
============================
ใช้สำหรับ auto-grading Week 07

คะแนน: 25 คะแนน
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Check if Ollama is available
OLLAMA_AVAILABLE = False
try:
    import requests
    response = requests.get("http://localhost:11434/api/tags", timeout=2)
    OLLAMA_AVAILABLE = response.status_code == 200
except:
    pass


class TestCodeStructure:
    """Test code structure (ไม่ต้องการ Ollama)"""
    
    def test_class_exists(self):
        """ทดสอบว่า OllamaClient class มีอยู่"""
        from ollama_client import OllamaClient
        assert OllamaClient is not None
    
    def test_methods_exist(self):
        """ทดสอบว่า methods ถูก define"""
        from ollama_client import OllamaClient
        
        assert hasattr(OllamaClient, 'generate')
        assert hasattr(OllamaClient, 'chat')
        assert hasattr(OllamaClient, 'is_available')
    
    def test_methods_not_pass(self):
        """ทดสอบว่า methods ไม่ใช่แค่ pass"""
        import inspect
        from ollama_client import OllamaClient
        
        methods = ['generate', 'chat', 'is_available']
        
        for method_name in methods:
            method = getattr(OllamaClient, method_name)
            source = inspect.getsource(method)
            
            code_lines = [
                l for l in source.split('\n')
                if l.strip()
                and not l.strip().startswith('#')
                and not l.strip().startswith('"""')
                and not l.strip().startswith("'''")
                and l.strip() != 'pass'
            ]
            
            assert len(code_lines) > 3, f"{method_name} appears not implemented"


@pytest.mark.skipif(not OLLAMA_AVAILABLE, reason="Ollama not running")
class TestOllamaClient:
    """Test with actual Ollama"""
    
    def test_is_available_returns_bool(self):
        """ทดสอบว่า is_available return bool"""
        from ollama_client import OllamaClient
        
        client = OllamaClient()
        result = client.is_available()
        
        assert isinstance(result, bool)
    
    def test_is_available_returns_true(self):
        """ทดสอบว่า is_available return True เมื่อ Ollama ทำงาน"""
        from ollama_client import OllamaClient
        
        client = OllamaClient()
        assert client.is_available() == True
    
    def test_generate_returns_string(self):
        """ทดสอบว่า generate return string"""
        from ollama_client import OllamaClient
        
        client = OllamaClient()
        result = client.generate("Say 'hello' only", max_tokens=10)
        
        assert isinstance(result, str)
        assert len(result) > 0
    
    def test_chat_returns_string(self):
        """ทดสอบว่า chat return string"""
        from ollama_client import OllamaClient
        
        client = OllamaClient()
        messages = [
            {"role": "user", "content": "Say 'hi' only"}
        ]
        result = client.chat(messages)
        
        assert isinstance(result, str)
        assert len(result) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
