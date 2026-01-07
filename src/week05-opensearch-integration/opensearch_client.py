"""
Week 05: OpenSearch Client Wrapper
Provides easy-to-use interface for OpenSearch operations
"""

from typing import List, Dict, Any, Optional
from opensearchpy import OpenSearch
from dataclasses import dataclass


@dataclass
class OpenSearchConfig:
    host: str = "localhost"
    port: int = 9200
    index_name: str = "documents"
    use_ssl: bool = False


class OpenSearchClient:
    """Wrapper for OpenSearch operations"""
    
    def __init__(self, config: Optional[OpenSearchConfig] = None):
        self.config = config or OpenSearchConfig()
        self.client = OpenSearch(
            hosts=[{"host": self.config.host, "port": self.config.port}],
            http_auth=None,
            use_ssl=self.config.use_ssl,
            verify_certs=False,
            ssl_show_warn=False
        )
    
    def is_connected(self) -> bool:
        """Check connection"""
        try:
            self.client.info()
            return True
        except:
            return False
    
    def create_index(self, dimension: int = 1024) -> bool:
        """Create index with vector field"""
        if self.client.indices.exists(index=self.config.index_name):
            return False
        
        index_body = {
            "settings": {
                "index": {
                    "knn": True,
                    "knn.algo_param.ef_search": 100
                }
            },
            "mappings": {
                "properties": {
                    "content": {"type": "text"},
                    "content_vector": {
                        "type": "knn_vector",
                        "dimension": dimension,
                        "method": {
                            "name": "hnsw",
                            "space_type": "cosinesimil",
                            "engine": "nmslib"
                        }
                    },
                    "title": {"type": "text"},
                    "source": {"type": "keyword"},
                    "chunk_id": {"type": "integer"}
                }
            }
        }
        
        self.client.indices.create(index=self.config.index_name, body=index_body)
        return True
    
    def delete_index(self) -> bool:
        """Delete index"""
        if not self.client.indices.exists(index=self.config.index_name):
            return False
        self.client.indices.delete(index=self.config.index_name)
        return True
    
    def index_document(self, doc: Dict[str, Any], doc_id: Optional[str] = None) -> str:
        """Index a single document"""
        response = self.client.index(
            index=self.config.index_name,
            body=doc,
            id=doc_id,
            refresh=True
        )
        return response["_id"]
    
    def bulk_index(self, documents: List[Dict[str, Any]]) -> int:
        """Bulk index documents"""
        actions = []
        for doc in documents:
            actions.append({"index": {"_index": self.config.index_name}})
            actions.append(doc)
        
        response = self.client.bulk(body=actions, refresh=True)
        return len(documents) - len(response.get("errors", []))
    
    def search_keyword(self, query: str, top_k: int = 5) -> List[Dict]:
        """Keyword (BM25) search"""
        search_body = {
            "size": top_k,
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["content", "title"]
                }
            }
        }
        
        response = self.client.search(
            index=self.config.index_name,
            body=search_body
        )
        
        return self._format_results(response)
    
    def search_vector(self, vector: List[float], top_k: int = 5) -> List[Dict]:
        """Vector (KNN) search"""
        search_body = {
            "size": top_k,
            "query": {
                "knn": {
                    "content_vector": {
                        "vector": vector,
                        "k": top_k
                    }
                }
            }
        }
        
        response = self.client.search(
            index=self.config.index_name,
            body=search_body
        )
        
        return self._format_results(response)
    
    def search_hybrid(self, query: str, vector: List[float], top_k: int = 5) -> List[Dict]:
        """Hybrid search (Vector + BM25)"""
        search_body = {
            "size": top_k,
            "query": {
                "hybrid": {
                    "queries": [
                        {
                            "multi_match": {
                                "query": query,
                                "fields": ["content", "title"]
                            }
                        },
                        {
                            "knn": {
                                "content_vector": {
                                    "vector": vector,
                                    "k": top_k
                                }
                            }
                        }
                    ]
                }
            }
        }
        
        response = self.client.search(
            index=self.config.index_name,
            body=search_body,
            params={"search_pipeline": "hybrid-search-pipeline"}
        )
        
        return self._format_results(response)
    
    def _format_results(self, response: Dict) -> List[Dict]:
        """Format search results"""
        results = []
        for hit in response["hits"]["hits"]:
            result = {
                "id": hit["_id"],
                "score": hit["_score"],
                **hit["_source"]
            }
            # Remove vector from results
            result.pop("content_vector", None)
            results.append(result)
        return results
    
    def count_documents(self) -> int:
        """Count documents in index"""
        response = self.client.count(index=self.config.index_name)
        return response["count"]


if __name__ == "__main__":
    # Test client
    client = OpenSearchClient()
    
    if client.is_connected():
        print("✅ Connected to OpenSearch")
        print(f"   Documents: {client.count_documents()}")
    else:
        print("❌ Not connected")
