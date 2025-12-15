import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient

# Load environment variables
load_dotenv()

# Initialize Qdrant client
try:
    qdrant_client = QdrantClient(
        url=os.getenv("QDRANT_URL"),
        api_key=os.getenv("QDRANT_API_KEY"),
        timeout=10
    )
    print("Successfully connected to Qdrant")

    # Check available methods
    print("Available methods containing 'search':")
    methods = [method for method in dir(qdrant_client) if 'search' in method.lower()]
    for method in methods:
        print(f"  - {method}")

    print("\nAll methods:")
    all_methods = [method for method in dir(qdrant_client) if not method.startswith('_')]
    for method in sorted(all_methods):
        print(f"  - {method}")

except Exception as e:
    print(f"Failed to connect to Qdrant: {e}")