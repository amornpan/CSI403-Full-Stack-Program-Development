# Week 06: Embeddings + Document Indexing

## 📁 Files in this folder
- `embedding_model.py` - HuggingFace embedding wrapper
- `document_processor.py` - Document chunking and processing
- `embedding.py` - Main indexing script
- `requirements.txt` - Dependencies

## 🎯 Learning Objectives
- HuggingFace embeddings (bge-m3)
- Document chunking
- Indexing pipeline
- Local embedding (no API key!)

## ▶️ How to Run
```bash
conda activate rag_env
pip install -r requirements.txt

# Index documents
python embedding.py
```

## 💡 Note
First run will download the bge-m3 model (~2GB).
After that, it runs completely offline!
