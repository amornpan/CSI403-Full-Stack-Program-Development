"""
Week 08: Frontend App
=====================
Streamlit frontend สำหรับ RAG system
"""

import streamlit as st
import requests
import os

# Configuration
API_HOST = os.getenv("API_HOST", "localhost")
API_PORT = os.getenv("API_PORT", "9000")
API_URL = f"http://{API_HOST}:{API_PORT}"

# Page config
st.set_page_config(
    page_title="RAG Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 RAG Chatbot")
st.caption(f"Connected to API: {API_URL}")

# Sidebar
with st.sidebar:
    st.title("⚙️ Settings")
    top_k = st.slider("Top K Results", 1, 10, 3)
    
    st.divider()
    
    # Health check
    st.subheader("Status")
    try:
        response = requests.get(f"{API_URL}/health", timeout=5)
        if response.status_code == 200:
            data = response.json()
            st.success(f"✅ API: {data['status']}")
            st.info(f"📦 OpenSearch: {data['opensearch_status']}")
        else:
            st.error("❌ API Error")
    except Exception as e:
        st.error(f"❌ Cannot connect to API")
        st.caption(str(e))

# Chat interface
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "sources" in message:
            with st.expander("📚 Sources"):
                for source in message["sources"]:
                    st.write(f"- {source}")

# Input
if prompt := st.chat_input("Ask a question..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    f"{API_URL}/query",
                    json={"question": prompt, "top_k": top_k},
                    timeout=30
                )
                
                if response.status_code == 200:
                    data = response.json()
                    answer = data["answer"]
                    sources = data["sources"]
                    
                    st.markdown(answer)
                    with st.expander("📚 Sources"):
                        for source in sources:
                            st.write(f"- {source}")
                    
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": answer,
                        "sources": sources
                    })
                else:
                    st.error(f"API Error: {response.status_code}")
            except Exception as e:
                st.error(f"Error: {str(e)}")

# Footer
st.divider()
st.caption("Week 08 - Docker Compose | CSI403")
