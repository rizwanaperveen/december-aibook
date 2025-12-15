"""
Script to populate the Qdrant database with book content from the Docusaurus docs
"""
import os
import asyncio
from pathlib import Path
from typing import List
import re
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.http import models
from fastembed import TextEmbedding
import uuid

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
except Exception as e:
    print(f"Failed to connect to Qdrant: {e}")
    exit(1)

# Initialize embedding model
try:
    embedding_model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")
    print("Successfully loaded embedding model")
except Exception as e:
    print(f"Failed to load embedding model: {e}")
    exit(1)

# Collection name
COLLECTION_NAME = "embodied_ai_book"

def chunk_text(text: str, chunk_size: int = 800, overlap: int = 100) -> List[str]:
    """
    Split text into overlapping chunks
    """
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks

def extract_content_from_md(file_path: Path) -> str:
    """
    Extract content from a markdown file, removing frontmatter
    """
    content = file_path.read_text(encoding='utf-8')

    # Remove frontmatter if present
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            content = parts[2]

    return content.strip()

def get_module_from_path(file_path: Path) -> str:
    """
    Determine the module based on the file path
    """
    if 'ros2' in file_path.name.lower() or 'basics' in file_path.name.lower():
        return "Module 1: Robotic Nervous System (ROS 2)"
    elif 'digital' in file_path.name.lower() or 'twin' in file_path.name.lower():
        return "Module 2: Digital Twin (Gazebo + Unity)"
    else:
        return "Introduction"

def get_chapter_from_path(file_path: Path) -> str:
    """
    Determine the chapter name from the file path
    """
    # Remove extension and convert underscores/hyphens to spaces
    stem = file_path.stem.replace('-', ' ').replace('_', ' ').title()
    return stem

def populate_qdrant():
    """
    Populate Qdrant with book content
    """
    print("Starting to populate Qdrant database...")

    # Check if collection exists, create if not
    try:
        qdrant_client.get_collection(collection_name=COLLECTION_NAME)
        print(f"Collection {COLLECTION_NAME} already exists")
    except:
        qdrant_client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=models.VectorParams(
                size=384,  # Size of BGE small embedding
                distance=models.Distance.COSINE
            )
        )
        print(f"Created Qdrant collection: {COLLECTION_NAME}")

    # Path to the Docusaurus docs
    docs_path = Path("../frontend/my-aibook/docs")

    if not docs_path.exists():
        print(f"Docs path not found: {docs_path}")
        return

    # Process each markdown file in the docs directory
    md_files = list(docs_path.glob("*.md"))
    print(f"Found {len(md_files)} markdown files to process")

    total_chunks = 0

    for md_file in md_files:
        print(f"Processing {md_file.name}...")

        # Extract content from markdown file
        content = extract_content_from_md(md_file)

        # Skip if content is too short
        if len(content) < 10:
            print(f"  Skipping {md_file.name} - content too short")
            continue

        # Determine module and chapter
        module = get_module_from_path(md_file)
        chapter = get_chapter_from_path(md_file)

        print(f"  Module: {module}, Chapter: {chapter}")

        # Chunk the content
        chunks = chunk_text(content, chunk_size=800, overlap=100)
        print(f"  Created {len(chunks)} chunks")

        # Process each chunk
        points = []
        for i, chunk in enumerate(chunks):
            if len(chunk.strip()) < 10:  # Skip very short chunks
                continue

            # Generate embedding for the chunk
            try:
                embeddings = list(embedding_model.embed([chunk]))
                embedding_vector = embeddings[0]

                # Create payload
                payload = {
                    "id": str(uuid.uuid4()),
                    "module": module,
                    "chapter": chapter,
                    "text": chunk,
                    "source_file": md_file.name,
                    "chunk_index": i
                }

                # Create a unique ID for Qdrant
                qdrant_id = str(uuid.uuid4())

                # Create point
                point = models.PointStruct(
                    id=qdrant_id,
                    vector=embedding_vector.tolist(),
                    payload=payload
                )

                points.append(point)
            except Exception as e:
                print(f"  Error processing chunk {i}: {e}")
                continue

        # Upload points to Qdrant in batches
        if points:
            batch_size = 100  # Process in batches to avoid timeouts
            for i in range(0, len(points), batch_size):
                batch = points[i:i + batch_size]
                try:
                    qdrant_client.upsert(
                        collection_name=COLLECTION_NAME,
                        points=batch
                    )
                    print(f"  Uploaded batch {i//batch_size + 1} of {(len(points)-1)//batch_size + 1}")
                except Exception as e:
                    print(f"  Error uploading batch: {e}")
                    continue

            total_chunks += len(points)
            print(f"  Uploaded {len(points)} chunks for {md_file.name}")

    print(f"\nSuccessfully uploaded {total_chunks} total chunks to Qdrant!")
    print("Database population complete.")

if __name__ == "__main__":
    populate_qdrant()