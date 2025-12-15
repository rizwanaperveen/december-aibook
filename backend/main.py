from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.http import models
from fastembed import TextEmbedding
import uuid
import logging
from datetime import datetime
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Embodied AI Systems RAG API",
    description="API for the Embodied AI Systems Book RAG chatbot",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Qdrant client
qdrant_client = None
try:
    qdrant_client = QdrantClient(
        url=os.getenv("QDRANT_URL"),
        api_key=os.getenv("QDRANT_API_KEY"),
        timeout=10
    )

    # Test the connection by trying to get collections
    collections = qdrant_client.get_collections()
    logger.info("Successfully connected to Qdrant and verified connection")

    # Test if search method exists
    if hasattr(qdrant_client, 'search'):
        logger.info("Qdrant client has search capability (search method available)")
    elif hasattr(qdrant_client, 'search_points'):
        logger.info("Qdrant client has search capability (search_points method available)")
    elif hasattr(qdrant_client, 'query_points'):
        logger.info("Qdrant client has search capability (query_points method available)")
    else:
        logger.error("Qdrant client does not have required search methods")
        qdrant_client = None

except Exception as e:
    logger.error(f"Failed to connect to Qdrant: {e}")
    qdrant_client = None

# Initialize embedding model
try:
    embedding_model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")
    logger.info("Successfully loaded embedding model")
except Exception as e:
    logger.error(f"Failed to load embedding model: {e}")
    embedding_model = None

# Initialize Gemini API
try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    gemini_model = genai.GenerativeModel('gemini-2.5-flash')  # Using gemini-2.5-flash which is available
    logger.info("Successfully configured Gemini API with gemini-2.5-flash model")
except Exception as e:
    logger.error(f"Failed to configure Gemini API: {e}")
    gemini_model = None

# Define request/response models
class ChatRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=1000)
    use_selected_text: bool = False
    selected_text: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    citations: List[str]
    query: str
    timestamp: datetime

class Document(BaseModel):
    id: str
    module: str
    chapter: str
    anchor: Optional[str] = None
    text: str
    qdrant_id: Optional[str] = None

class HealthResponse(BaseModel):
    status: str
    timestamp: datetime

# Collection name for Qdrant
COLLECTION_NAME = "embodied_ai_book"

# Create collection if it doesn't exist
def initialize_qdrant_collection():
    if not qdrant_client:
        return

    try:
        # Check if collection exists
        collections = qdrant_client.get_collections()
        collection_exists = any(col.name == COLLECTION_NAME for col in collections.collections)

        if not collection_exists:
            qdrant_client.create_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=models.VectorParams(
                    size=384,  # Size of BGE small embedding
                    distance=models.Distance.COSINE
                )
            )
            logger.info(f"Created Qdrant collection: {COLLECTION_NAME}")
        else:
            logger.info(f"Qdrant collection {COLLECTION_NAME} already exists")
    except Exception as e:
        logger.error(f"Failed to initialize Qdrant collection: {e}")

# Initialize the collection on startup
@app.on_event("startup")
def startup_event():
    initialize_qdrant_collection()

# API endpoints
@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        timestamp=datetime.utcnow()
    )

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Main chat endpoint that handles queries and returns RAG responses"""
    logger.info(f"Received query: {request.query[:50]}...")

    # Validate dependencies
    if not qdrant_client:
        raise HTTPException(status_code=500, detail="Qdrant client not available")
    if not embedding_model:
        raise HTTPException(status_code=500, detail="Embedding model not available")
    if not gemini_model:
        raise HTTPException(status_code=500, detail="Gemini API not available")

    try:
        # Check if collection exists
        try:
            qdrant_client.get_collection(collection_name=COLLECTION_NAME)
            logger.info(f"Collection {COLLECTION_NAME} exists")
        except Exception as e:
            logger.error(f"Collection {COLLECTION_NAME} does not exist: {e}")
            # Create collection if it doesn't exist
            qdrant_client.create_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=models.VectorParams(
                    size=384,  # Size of BGE small embedding
                    distance=models.Distance.COSINE
                )
            )
            logger.info(f"Created Qdrant collection: {COLLECTION_NAME}")

        # If using selected text mode, use only the provided text
        if request.use_selected_text and request.selected_text:
            # Generate prompt for Gemini with selected text
            prompt = f"Based on the following selected text: '{request.selected_text}', please answer this question: {request.query}"
            citations = ["Selected Text"]
        else:
            # Perform semantic search in Qdrant
            query_embedding = list(embedding_model.embed([request.query]))[0]

            # Use the appropriate search method based on Qdrant client version
            if hasattr(qdrant_client, 'search'):
                search_results = qdrant_client.search(
                    collection_name=COLLECTION_NAME,
                    query_vector=query_embedding.tolist(),  # Convert to list
                    limit=5,  # Get top 5 results
                    with_payload=True
                )
            elif hasattr(qdrant_client, 'search_points'):
                # For older versions of Qdrant client
                search_results = qdrant_client.search_points(
                    collection_name=COLLECTION_NAME,
                    vector=query_embedding.tolist(),  # Convert to list
                    limit=5,  # Get top 5 results
                    with_payload=True
                )
            elif hasattr(qdrant_client, 'query_points'):
                # For newer versions of Qdrant client
                search_results = qdrant_client.query_points(
                    collection_name=COLLECTION_NAME,
                    query=query_embedding.tolist(),  # Convert to list
                    limit=5,  # Get top 5 results
                    with_payload=True
                )
            else:
                raise Exception("Qdrant client does not have search capability")

            # Extract relevant content
            relevant_content = []
            citations = []

            for result in search_results:
                if hasattr(result, 'payload') and result.payload:
                    relevant_content.append(result.payload.get('text', ''))
                    # Create citation from module and chapter
                    module = result.payload.get('module', 'Unknown')
                    chapter = result.payload.get('chapter', 'Unknown')
                    citations.append(f"Module: {module}, Chapter: {chapter}")
                elif isinstance(result, dict) and 'payload' in result:
                    # For some versions, results might be dictionaries
                    payload = result.get('payload', {})
                    relevant_content.append(payload.get('text', ''))
                    module = payload.get('module', 'Unknown')
                    chapter = payload.get('chapter', 'Unknown')
                    citations.append(f"Module: {module}, Chapter: {chapter}")

            # Generate prompt for Gemini with retrieved content
            if relevant_content:
                context = "\n\n".join([f"Source: {citations[i]}\nContent: {content[:1000]}" for i, content in enumerate(relevant_content[:3])])  # Use top 3 results with citations
                prompt = f"Based on the following book content, please answer the question. If the content doesn't contain the answer, say so clearly.\n\n{context}\n\nQuestion: {request.query}"
            else:
                prompt = f"The user asked: '{request.query}'. I couldn't find relevant information in the book. Please acknowledge this and suggest they check other chapters or ask a different question."
                citations = []

        # Generate response using Gemini
        try:
            response = gemini_model.generate_content(prompt)
            response_text = response.text if response.text else "I couldn't generate a response. Please try again."
        except Exception as e:
            logger.error(f"Error calling Gemini API: {e}")
            response_text = f"Sorry, I encountered an error generating a response. Please try again later. Error: {str(e)}"

        return ChatResponse(
            response=response_text,
            citations=citations,
            query=request.query,
            timestamp=datetime.utcnow()
        )
    except Exception as e:
        logger.error(f"Error in chat endpoint: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.post("/embed")
async def embed_text(request: Dict[str, Any]):
    """Endpoint to generate embeddings for text"""
    if not embedding_model:
        raise HTTPException(status_code=500, detail="Embedding model not available")

    text = request.get("text", "")
    if not text:
        raise HTTPException(status_code=400, detail="Text is required")

    try:
        embeddings = list(embedding_model.embed([text]))
        return {"embeddings": embeddings[0].tolist()}
    except Exception as e:
        logger.error(f"Error in embed endpoint: {e}")
        raise HTTPException(status_code=500, detail=f"Error generating embeddings: {str(e)}")

@app.post("/retrieve")
async def retrieve_content(request: Dict[str, Any]):
    """Endpoint to retrieve similar content from Qdrant"""
    if not qdrant_client:
        raise HTTPException(status_code=500, detail="Qdrant client not available")
    if not embedding_model:
        raise HTTPException(status_code=500, detail="Embedding model not available")

    query = request.get("query", "")
    if not query:
        raise HTTPException(status_code=400, detail="Query is required")

    try:
        query_embedding = list(embedding_model.embed([query]))[0]

        # Use the appropriate search method based on Qdrant client version
        if hasattr(qdrant_client, 'search'):
            search_results = qdrant_client.search(
                collection_name=COLLECTION_NAME,
                query_vector=query_embedding.tolist(),  # Convert to list
                limit=request.get("limit", 5),
                with_payload=True
            )
        elif hasattr(qdrant_client, 'search_points'):
            # For older versions of Qdrant client
            search_results = qdrant_client.search_points(
                collection_name=COLLECTION_NAME,
                vector=query_embedding.tolist(),  # Convert to list
                limit=request.get("limit", 5),
                with_payload=True
            )
        else:
            raise Exception("Qdrant client does not have search capability")

        results = []
        for result in search_results:
            results.append({
                "id": result.id,
                "text": result.payload.get('text', ''),
                "module": result.payload.get('module', ''),
                "chapter": result.payload.get('chapter', ''),
                "score": result.score
            })

        return {"results": results}
    except Exception as e:
        logger.error(f"Error in retrieve endpoint: {e}")
        raise HTTPException(status_code=500, detail=f"Error retrieving content: {str(e)}")

@app.post("/add_document")
async def add_document(doc: Document):
    """Endpoint to add a document to the Qdrant collection"""
    if not qdrant_client:
        raise HTTPException(status_code=500, detail="Qdrant client not available")
    if not embedding_model:
        raise HTTPException(status_code=500, detail="Embedding model not available")

    try:
        # Generate embedding for the document text
        embeddings = list(embedding_model.embed([doc.text]))
        embedding_vector = embeddings[0]

        # Prepare the payload
        payload = {
            "id": doc.id,
            "module": doc.module,
            "chapter": doc.chapter,
            "text": doc.text
        }
        if doc.anchor:
            payload["anchor"] = doc.anchor

        # Generate a unique ID for Qdrant if not provided
        qdrant_id = str(uuid.uuid4()) if not doc.qdrant_id else doc.qdrant_id

        # Upload to Qdrant
        qdrant_client.upsert(
            collection_name=COLLECTION_NAME,
            points=[
                models.PointStruct(
                    id=qdrant_id,
                    vector=embedding_vector.tolist(),
                    payload=payload
                )
            ]
        )

        return {"message": "Document added successfully", "qdrant_id": qdrant_id}
    except Exception as e:
        logger.error(f"Error in add_document endpoint: {e}")
        raise HTTPException(status_code=500, detail=f"Error adding document: {str(e)}")


@app.post("/gemini_chat")
async def gemini_chat(request: ChatRequest):
    """Chat endpoint using Gemini API with book content context"""
    logger.info(f"Received Gemini query: {request.query[:50]}...")

    if not gemini_model:
        raise HTTPException(status_code=500, detail="Gemini API not available")

    try:
        # For now, we'll use a simple approach. In a real implementation, you'd want to:
        # 1. Search your book content for relevant information
        # 2. Pass that context to the Gemini API

        # Placeholder context - in real implementation, you'd retrieve relevant content from your book
        context = "The Embodied AI Systems Book covers topics like ROS 2, Digital Twins, Gazebo, Unity, and robotics."

        if request.use_selected_text and request.selected_text:
            prompt = f"Based on the following selected text: '{request.selected_text}', please answer this question: {request.query}"
            citations = ["Selected Text"]
        else:
            prompt = f"Based on the following book content, please answer the question. If the content doesn't contain the answer, say so clearly.\n\n{context}\n\nQuestion: {request.query}"
            citations = ["Embodied AI Systems Book"]

        response = gemini_model.generate_content(prompt)

        return ChatResponse(
            response=response.text,
            citations=citations,
            query=request.query,
            timestamp=datetime.utcnow()
        )
    except Exception as e:
        logger.error(f"Error in Gemini chat endpoint: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Embodied AI Systems RAG API", "status": "running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)