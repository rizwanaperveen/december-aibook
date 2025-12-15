# Quickstart Guide: Embodied AI Systems Book + RAG Chatbot

## Prerequisites

- **Node.js**: Version 20.x or higher
- **Python**: Version 3.12 or higher
- **Git**: Version control system
- **Access to Qdrant Cloud**: With API key and cluster URL
- **Google Generative AI API Key**: For Gemini integration

## Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env with your Qdrant and Gemini API keys
```

### 3. Frontend Setup
```bash
cd frontend/my-aibook

# Install dependencies
npm install

# Configure environment variables
cp .env.example .env
# Edit .env with your Gemini API key
```

## Configuration

### Backend Configuration (.env)
```
QDRANT_API_KEY="your_qdrant_api_key"
QDRANT_URL="https://your-cluster-url.gcp.cloud.qdrant.io"
GEMINI_API_KEY="your_gemini_api_key"
```

### Frontend Configuration (.env)
```
REACT_APP_GEMINI_API_KEY="your_gemini_api_key"
GEMINI_API_KEY="your_gemini_api_key"
```

## Initialization

### 1. Populate Qdrant Database
```bash
cd backend
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Process book content and populate Qdrant
python populate_db.py
```

### 2. Process Book Content for Frontend
```bash
cd frontend/my-aibook

# Process documentation files
npm run process-docs
```

## Running the Application

### 1. Start Backend Server
```bash
cd backend
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Start the FastAPI server
python -m uvicorn main:app --reload
```

### 2. Start Frontend Server
```bash
cd frontend/my-aibook

# Start the Docusaurus development server
npm run start
```

### 3. Access the Application
- **Frontend**: http://localhost:3000
- **Backend API Docs**: http://localhost:8000/docs
- **Chat Interface**: http://localhost:3000/chat

## Using the Chatbot

### Basic Queries
1. Navigate to the "AI Assistant" page
2. Type a question about the book content
3. Press "Send" to get a response with citations

### Selected-Text Mode
1. Highlight text in any book chapter
2. Check the "Use selected text only" checkbox
3. Type a question related to the highlighted text
4. The response will be grounded only in the selected text

## API Endpoints

### Backend Endpoints
- `GET /health`: Health check
- `POST /chat`: Main chat endpoint with RAG functionality
- `POST /retrieve`: Semantic search in the knowledge base
- `POST /embed`: Generate embeddings for text
- `POST /add_document`: Add documents to the knowledge base

### Frontend Pages
- `/`: Main book content
- `/chat`: AI Assistant interface
- `/login`: User authentication
- `/docs/*`: Individual book chapters

## Troubleshooting

### Common Issues

#### Qdrant Connection Error
- Verify QDRANT_URL and QDRANT_API_KEY in backend/.env
- Check internet connectivity to Qdrant cluster
- Ensure the Qdrant collection exists

#### Gemini API Error
- Verify GEMINI_API_KEY in both frontend and backend
- Check if API key has proper permissions
- Ensure API is enabled in Google Cloud Console

#### Frontend Build Error
- Run `npm install` again to reinstall dependencies
- Clear npm cache: `npm cache clean --force`
- Delete node_modules and package-lock.json, then reinstall

#### Empty Book Content
- Run `npm run process-docs` to regenerate book-content.json
- Verify that markdown files exist in frontend/my-aibook/docs/
- Check that book-content.json is in the static directory

## Development Tips

### Adding New Book Content
1. Add markdown files to `frontend/my-aibook/docs/`
2. Run `npm run process-docs` to update the content index
3. Restart the frontend server to see changes

### Modifying the Chatbot
1. Update the component in `frontend/my-aibook/src/components/Chatbot/Chatbot.tsx`
2. Modify the backend logic in `backend/main.py`
3. Test both selected-text mode and regular queries

### Testing Changes
- Use the backend API documentation at `/docs` for testing endpoints
- Verify citations appear correctly in chat responses
- Test with various query types to ensure grounding works