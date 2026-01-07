# Lab 4: OpenSearch Integration (3.75%)

## Objectives
- Connect to OpenSearch from Python
- Implement hybrid search
- Index and search documents

---

## Tasks

### Task 1: Connect to OpenSearch
```python
from opensearchpy import OpenSearch

client = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],
    use_ssl=False
)
print(client.info())
```

### Task 2: Create Index
```python
index_body = {
    "settings": {"index": {"knn": True}},
    "mappings": {
        "properties": {
            "content": {"type": "text"},
            "content_vector": {
                "type": "knn_vector",
                "dimension": 1024
            }
        }
    }
}
client.indices.create(index="documents", body=index_body)
```

### Task 3: Index Documents
```python
doc = {
    "content": "Sample document text",
    "content_vector": [0.1, 0.2, ...]  # 1024 dims
}
client.index(index="documents", body=doc)
```

### Task 4: Implement Search
Implement hybrid search combining vector and BM25.

---

## Repository
https://github.com/amornpan/Generic-RAG

## Deliverables
- [ ] Connection working
- [ ] Index created
- [ ] Documents indexed
- [ ] Search implemented

## Deadline
Sunday 23:59
