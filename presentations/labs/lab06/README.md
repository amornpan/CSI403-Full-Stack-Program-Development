# Lab 6: RAG + Local LLM + Streamlit (3.75%)

## Objectives
- Setup Ollama
- Complete RAG pipeline
- Run Streamlit UI

---

## Tasks

### Task 1: Install Ollama
1. Download from https://ollama.ai
2. Install and run

### Task 2: Pull Model
```bash
ollama pull qwen2.5:7b
```

### Task 3: Test LLM
```bash
ollama run qwen2.5:7b
# Type: "What is RAG?"
```

### Task 4: Run API with LLM
```bash
cd Generic-RAG
python api.py
```

### Task 5: Run Streamlit
```bash
streamlit run app.py
```

### Task 6: Test Complete Flow
1. Open http://localhost:8501
2. Ask questions
3. Verify RAG responses

### Task 7: Modify Prompt
Edit the prompt template in api.py.

---

## Repository
https://github.com/amornpan/Generic-RAG

## Deliverables
- [ ] Ollama running
- [ ] LLM tested
- [ ] Complete RAG working
- [ ] Streamlit UI working

## Deadline
Sunday 23:59
