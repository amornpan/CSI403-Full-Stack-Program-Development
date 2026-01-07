"""
Week 03: Test OpenSearch Connection
Simple script to verify OpenSearch is working
"""

from opensearchpy import OpenSearch


def main():
    print("Testing OpenSearch Connection...")
    
    client = OpenSearch(
        hosts=[{"host": "localhost", "port": 9200}],
        use_ssl=False
    )
    
    try:
        # Get cluster info
        info = client.info()
        print(f"\n✅ Connection successful!")
        print(f"   Cluster: {info['cluster_name']}")
        print(f"   Version: {info['version']['number']}")
        
        # Get cluster health
        health = client.cluster.health()
        print(f"   Status: {health['status']}")
        print(f"   Nodes: {health['number_of_nodes']}")
        
        # List indices
        indices = client.cat.indices(format="json")
        print(f"\n   Indices: {len(indices)}")
        for idx in indices:
            print(f"   - {idx['index']}")
            
    except Exception as e:
        print(f"\n❌ Connection failed: {e}")
        print("\nMake sure OpenSearch is running:")
        print("  docker-compose up -d")


if __name__ == "__main__":
    main()
