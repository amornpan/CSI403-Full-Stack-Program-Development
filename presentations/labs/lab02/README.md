# Lab 2: Docker + OpenSearch (3.75%)

## Objectives
- Install Docker Desktop
- Run OpenSearch container
- Configure Hybrid Search Pipeline

---

## Tasks

### Task 1: Install Docker Desktop
1. Download from https://docker.com
2. Install and start
3. Verify: `docker --version`

### Task 2: Run OpenSearch
```bash
docker run -d --name opensearch-node \
  -p 9200:9200 -p 9600:9600 \
  -e "discovery.type=single-node" \
  -e "DISABLE_SECURITY_PLUGIN=true" \
  opensearchproject/opensearch:2.11.1
```

### Task 3: Verify
```bash
curl http://localhost:9200
```

### Task 4: Setup Hybrid Search Pipeline
```bash
curl -X PUT "localhost:9200/_search/pipeline/hybrid-search-pipeline" \
  -H "Content-Type: application/json" \
  -d '{
    "phase_results_processors": [{
      "normalization-processor": {
        "normalization": {"technique": "min_max"},
        "combination": {
          "technique": "arithmetic_mean",
          "parameters": {"weights": [0.3, 0.7]}
        }
      }
    }]
  }'
```

### Task 5: Check Health
```bash
curl http://localhost:9200/_cluster/health?pretty
```

---

## Deliverables
- [ ] Docker installed
- [ ] OpenSearch running
- [ ] Pipeline created
- [ ] Screenshots

## Deadline
Sunday 23:59
