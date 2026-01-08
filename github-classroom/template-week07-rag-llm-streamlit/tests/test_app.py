"""
Test cases for Streamlit App
============================
ใช้สำหรับ auto-grading Week 07

คะแนน: 30 คะแนน

Note: Streamlit tests เป็นการตรวจสอบโค้ดมากกว่า runtime
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


class TestAppStructure:
    """Test app.py structure"""
    
    def test_app_file_exists(self):
        """ทดสอบว่า app.py มีอยู่"""
        app_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'app.py')
        assert os.path.exists(app_path), "app.py not found"
    
    def test_app_imports_streamlit(self):
        """ทดสอบว่า app import streamlit"""
        app_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'app.py')
        
        with open(app_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        assert "import streamlit" in content or "from streamlit" in content
    
    def test_app_imports_rag(self):
        """ทดสอบว่า app import RAGPipeline"""
        app_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'app.py')
        
        with open(app_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        assert "RAGPipeline" in content


class TestTODO1ChatInterface:
    """Test TODO 1: Chat Interface (10 คะแนน)"""
    
    def test_has_chat_message(self):
        """ทดสอบว่ามี st.chat_message"""
        app_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'app.py')
        
        with open(app_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        assert "chat_message" in content, "Should use st.chat_message"
    
    def test_has_chat_input(self):
        """ทดสอบว่ามี st.chat_input"""
        app_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'app.py')
        
        with open(app_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        assert "chat_input" in content, "Should use st.chat_input"
    
    def test_uses_session_state(self):
        """ทดสอบว่าใช้ session_state"""
        app_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'app.py')
        
        with open(app_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        assert "session_state" in content, "Should use st.session_state"


class TestTODO2Sources:
    """Test TODO 2: Sources Display (10 คะแนน)"""
    
    def test_has_sources_display(self):
        """ทดสอบว่ามีการแสดง sources"""
        app_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'app.py')
        
        with open(app_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # ควรมี expander หรือ caption สำหรับ sources
        has_sources = "sources" in content.lower()
        has_expander = "expander" in content
        has_caption = "caption" in content
        
        assert has_sources, "Should handle sources"


class TestTODO3Sidebar:
    """Test TODO 3: Sidebar Settings (10 คะแนน)"""
    
    def test_has_sidebar(self):
        """ทดสอบว่ามี sidebar"""
        app_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'app.py')
        
        with open(app_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        assert "sidebar" in content, "Should use st.sidebar"
    
    def test_has_temperature_slider(self):
        """ทดสอบว่ามี temperature setting"""
        app_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'app.py')
        
        with open(app_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        assert "temperature" in content.lower(), "Should have temperature setting"
    
    def test_has_slider(self):
        """ทดสอบว่าใช้ slider"""
        app_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'app.py')
        
        with open(app_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        assert "slider" in content, "Should use st.slider"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
