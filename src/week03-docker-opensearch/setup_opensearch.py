"""
Week 03: OpenSearch Setup Script
Sets up OpenSearch with Hybrid Search Pipeline
"""

import requests
import json
from opensearchpy import OpenSearch

# Configuration
OPENSEARCH_HOST = "localhost"
OPENSEARCH_PORT = 9200
INDEX_NAME = "documents"


def get_client() -> OpenSearch:
    """Create OpenSearch client"""
    return OpenSearch(
        hosts=[{"host": OPENSEARCH_HOST, "port": OPENSEARCH_PORT}],
        http_auth=None,
        use_ssl=False,
        verify_certs=False,
        ssl_show_warn=False
    )


def check_connection(client: OpenSearch) -> bool:
    """Check if OpenSearch is running"""
    try:
        info = client.info()
        print(f"✅ Connected to OpenSearch")
        print(f"   Cluster: {info['cluster_name']}")
        print(f"   Version: {info['version']['number']}")
        return True
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False


def setup_hybrid_search_pipeline():
    """Create Hybrid Search Pipeline"""
    url = f"http://{OPENSEARCH_HOST}:{OPENSEARCH_PORT}/_search/pipeline/hybrid-search-pipeline"
    
    pipeline_body = {
        "description": "Hybrid search pipeline for RAG",
        "phase_results_processors": [
            {
                "normalization-processor": {
                    "normalization": {
                        "technique": "min_max"
                    },
                    "combination": {
                        "technique": "arithmetic_mean",
                        "parameters": {
                            "weights": [0.3, 0.7]  # 30% BM25, 70% Vector
                        }
                    }
                }
            }
        ]
    }
    
    try:
        response = requests.put(url, json=pipeline_body)
        if response.status_code in [200, 201]:
            print("✅ Hybrid Search Pipeline created")
        else:
            print(f"⚠️ Pipeline response: {response.status_code}")
    except Exception as e:
        print(f"❌ Pipeline creation failed: {e}")


def create_index(client: OpenSearch, dimension: int = 1024):
    """Create index with vector field"""
    
    index_body = {
        "settings": {
            "index": {
                "knn": True,
                "knn.algo_param.ef_search": 100
            }
        },
        "mappings": {
            "properties": {
                "content": {
                    "type": "text",
                    "analyzer": "standard"
                },
                "content_vector": {
                    "type": "knn_vector",
                    "dimension": dimension,
                    "method": {
                        "name": "hnsw",
                        "space_type": "cosinesimil",
                        "engine": "nmslib",
                        "parameters": {
                            "ef_construction": 128,
                            "m": 24
                        }
                    }
                },
                "title": {
                    "type": "text"
                },
                "source": {
                    "type": "keyword"
                },
                "created_at": {
                    "type": "date"
                }
            }
        }
    }
    
    try:
        if client.indices.exists(index=INDEX_NAME):
            print(f"⚠️ Index '{INDEX_NAME}' already exists")
            return
        
        client.indices.create(index=INDEX_NAME, body=index_body)
        print(f"✅ Index '{INDEX_NAME}' created")
    except Exception as e:
        print(f"❌ Index creation failed: {e}")


def main():
    print("=" * 50)
    print("Week 03: OpenSearch Setup")
    print("=" * 50)
    
    # Connect
    client = get_client()
    if not check_connection(client):
        print("\n⚠️ Make sure OpenSearch is running:")
        print("   docker-compose up -d")
        return
    
    # Setup pipeline
    print("\n--- Setting up Hybrid Search Pipeline ---")
    setup_hybrid_search_pipeline()
    
    # Create index
    print(f"\n--- Creating Index '{INDEX_NAME}' ---")
    create_index(client)
    
    # Show indices
    print("\n--- Current Indices ---")
    indices = client.cat.indices(format="json")
    for idx in indices:
        print(f"   {idx['index']}: {idx['docs.count']} docs")
    
    print("\n" + "=" * 50)
    print("✅ OpenSearch setup completed!")
    print("=" * 50)


if __name__ == "__main__":
    main()
