# Embodied AI Systems RAG Backend

This is the backend server for the Embodied AI Systems Book RAG chatbot. It provides API endpoints for semantic search and question answering based on the book content.

## Features

- FastAPI-based REST API
- Qdrant vector database integration
- Semantic search capabilities
- Selected-text mode for focused answers
- Proper citation of sources
- Content ingestion pipeline

## API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `POST /chat` - Main chat endpoint for RAG responses
- `POST /embed` - Generate embeddings for text
- `POST /retrieve` - Semantic search in the knowledge base
- `POST /add_document` - Add documents to the knowledge base

## Setup

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up environment variables in `.env`:
   ```
   QDRANT_API_KEY="your_qdrant_api_key"
   QDRANT_URL="your_qdrant_cluster_url"
   GEMINI_API_KEY="your_gemini_api_key"  # Optional
   ```

3. Populate the database with book content:
   ```bash
   python populate_db.py
   ```

4. Start the server:
   ```bash
   python -m uvicorn main:app --reload
   ```

   Or use the start script:
   ```bash
   chmod +x start.sh
   ./start.sh
   ```

## Environment Variables

- `QDRANT_API_KEY` - Your Qdrant Cloud API key
- `QDRANT_URL` - Your Qdrant Cloud cluster URL
- `GEMINI_API_KEY` - Google Gemini API key (optional, for future enhancements)

## Architecture

The backend follows a RAG (Retrieval-Augmented Generation) pattern:

1. User query comes through the `/chat` endpoint
2. Query is embedded using a text embedding model
3. Vector search is performed in Qdrant to find relevant content
4. Relevant content is used to generate a contextual response
5. Citations are provided to indicate the source of information

## Development

For development, use the `--reload` flag with uvicorn to automatically reload the server when code changes are detected.

## Testing

The API includes comprehensive error handling and validation. Endpoints return appropriate HTTP status codes and error messages.