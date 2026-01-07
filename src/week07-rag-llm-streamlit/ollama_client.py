"""
Week 07: Ollama Client
Wrapper for local LLM using Ollama
"""

import requests
from typing import Optional, Generator
from dataclasses import dataclass


@dataclass
class OllamaConfig:
    host: str = "localhost"
    port: int = 11434
    model: str = "qwen2.5:7b"
    temperature: float = 0.7
    
    @property
    def base_url(self) -> str:
        return f"http://{self.host}:{self.port}"
    
    @property
    def generate_url(self) -> str:
        return f"{self.base_url}/api/generate"
    
    @property
    def chat_url(self) -> str:
        return f"{self.base_url}/api/chat"


class OllamaClient:
    """Client for Ollama local LLM"""
    
    def __init__(self, config: Optional[OllamaConfig] = None):
        self.config = config or OllamaConfig()
    
    def is_available(self) -> bool:
        """Check if Ollama is running"""
        try:
            response = requests.get(f"{self.config.base_url}/api/tags", timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def list_models(self) -> list:
        """List available models"""
        try:
            response = requests.get(f"{self.config.base_url}/api/tags")
            if response.status_code == 200:
                return [m["name"] for m in response.json().get("models", [])]
        except:
            pass
        return []
    
    def generate(self, prompt: str, stream: bool = False) -> str:
        """Generate text from prompt"""
        payload = {
            "model": self.config.model,
            "prompt": prompt,
            "stream": stream,
            "options": {
                "temperature": self.config.temperature
            }
        }
        
        response = requests.post(
            self.config.generate_url,
            json=payload,
            timeout=120
        )
        
        if response.status_code == 200:
            return response.json()["response"]
        else:
            raise Exception(f"Ollama error: {response.status_code}")
    
    def generate_stream(self, prompt: str) -> Generator[str, None, None]:
        """Generate text with streaming"""
        payload = {
            "model": self.config.model,
            "prompt": prompt,
            "stream": True,
            "options": {
                "temperature": self.config.temperature
            }
        }
        
        response = requests.post(
            self.config.generate_url,
            json=payload,
            stream=True,
            timeout=120
        )
        
        for line in response.iter_lines():
            if line:
                import json
                data = json.loads(line)
                if "response" in data:
                    yield data["response"]
    
    def chat(self, messages: list, stream: bool = False) -> str:
        """Chat completion"""
        payload = {
            "model": self.config.model,
            "messages": messages,
            "stream": stream,
            "options": {
                "temperature": self.config.temperature
            }
        }
        
        response = requests.post(
            self.config.chat_url,
            json=payload,
            timeout=120
        )
        
        if response.status_code == 200:
            return response.json()["message"]["content"]
        else:
            raise Exception(f"Ollama error: {response.status_code}")


# Singleton
_ollama_client: Optional[OllamaClient] = None


def get_ollama_client() -> OllamaClient:
    global _ollama_client
    if _ollama_client is None:
        _ollama_client = OllamaClient()
    return _ollama_client


if __name__ == "__main__":
    print("=" * 50)
    print("Testing Ollama Client")
    print("=" * 50)
    
    client = get_ollama_client()
    
    if client.is_available():
        print("✅ Ollama is running")
        print(f"   Models: {client.list_models()}")
        
        # Test generation
        print("\n--- Test Generation ---")
        prompt = "What is RAG in AI? Answer in 2 sentences."
        print(f"Prompt: {prompt}")
        
        response = client.generate(prompt)
        print(f"Response: {response}")
    else:
        print("❌ Ollama is not running")
        print("   Run: ollama serve")
