# Lab 5: Embeddings (3.75%)

## Objectives
- Run embedding.py
- Understand chunking
- Add new documents

---

## Tasks

### Task 1: Study embedding.py
Review the pipeline:
1. Load documents from md_corpus/
2. Chunk documents
3. Create embeddings (bge-m3)
4. Index to OpenSearch

### Task 2: Run Indexing
```bash
cd Generic-RAG
conda activate rag_env
python embedding.py
```

### Task 3: Verify
```bash
curl http://localhost:9200/documents/_count
```

### Task 4: Add New Documents
Add 3 new .md files to `md_corpus/` folder.

### Task 5: Re-index
```bash
python embedding.py
```

### Task 6: Test Search
Search for content from your new documents.

---

## Repository
https://github.com/amornpan/Generic-RAG

## Deliverables
- [ ] Indexing completed
- [ ] Documents verified
- [ ] New documents added
- [ ] Search tested

## Deadline
Sunday 23:59
