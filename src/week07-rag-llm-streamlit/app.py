"""
Week 07: Streamlit Chat UI
User interface for RAG system
"""

import streamlit as st
import requests
from datetime import datetime

# Configuration
API_URL = "http://localhost:9000"

# Page config
st.set_page_config(
    page_title="RAG Q&A System",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 RAG-Powered Q&A System")
st.markdown("*Full Stack RAG with Local LLM - Week 07*")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    
    top_k = st.slider("Number of sources", 1, 10, 5)
    
    st.divider()
    
    # Health check
    st.header("🔗 System Status")
    try:
        response = requests.get(f"{API_URL}/health", timeout=5)
        if response.status_code == 200:
            health = response.json()
            for component, status in health["components"].items():
                icon = "✅" if status else "❌"
                st.write(f"{icon} {component}")
        else:
            st.error("API not responding")
    except:
        st.error("Cannot connect to API")
        st.info("Make sure API is running:\n`python api.py`")
    
    st.divider()
    
    st.header("ℹ️ About")
    st.markdown("""
    This system uses:
    - **Ollama** for local LLM
    - **OpenSearch** for vector search
    - **bge-m3** for embeddings
    
    No API keys required! 🎉
    """)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "sources" in message:
            with st.expander("📚 Sources"):
                for src in message["sources"]:
                    st.markdown(f"**{src['title']}**")
                    st.markdown(f"*Score: {src['score']:.4f}*")
                    st.text(src['content'])
                    st.divider()

# Chat input
if prompt := st.chat_input("ถามคำถามได้เลย..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get response
    with st.chat_message("assistant"):
        with st.spinner("กำลังคิด..."):
            try:
                response = requests.post(
                    f"{API_URL}/query",
                    json={"query": prompt, "top_k": top_k},
                    timeout=120
                )
                
                if response.status_code == 200:
                    result = response.json()
                    
                    # Display answer
                    st.markdown(result["answer"])
                    
                    # Display sources
                    with st.expander(f"📚 Sources ({len(result['sources'])})"):
                        for src in result["sources"]:
                            st.markdown(f"**{src['title']}**")
                            st.markdown(f"*Score: {src['score']:.4f}*")
                            st.text(src['content'])
                            st.divider()
                    
                    # Metadata
                    st.caption(f"Model: {result['model']} | Time: {result['took_ms']:.0f}ms")
                    
                    # Save to history
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": result["answer"],
                        "sources": result["sources"]
                    })
                else:
                    st.error(f"Error: {response.status_code}")
                    
            except requests.exceptions.ConnectionError:
                st.error("❌ Cannot connect to API")
                st.info("Make sure API is running: `python api.py`")
            except Exception as e:
                st.error(f"Error: {e}")

# Footer
st.divider()
st.caption("© 2026 Full Stack RAG with Local LLM | Week 07")
