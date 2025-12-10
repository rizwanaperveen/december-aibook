# Embodied AI Systems Book + RAG Chatbot

A comprehensive educational platform for learning about embodied AI systems, featuring a Docusaurus-based book with integrated RAG chatbot functionality.

## Overview

This project combines educational content about embodied AI systems with an AI-powered chatbot that can answer questions based on the book content. The system includes:

- **Docusaurus-based book**: Structured content covering ROS 2 and Digital Twins
- **RAG Chatbot**: AI assistant that answers questions based on book content
- **Selected-text mode**: Option to restrict answers to highlighted text only
- **Proper citations**: All responses include module and chapter references

## Features

### Book Content
- Module 1: Robotic Nervous System (ROS 2)
  - ROS 2 Nodes, Topics, Services
  - rclpy agent-to-ROS bridge
  - URDF basics for humanoid robots
- Module 2: Digital Twin (Gazebo + Unity)
  - Physics simulation basics
  - Unity-based high-fidelity visualization
  - Sensor simulations (LiDAR, Depth Camera, IMU)

### AI Chatbot
- Semantic search across book content
- Selected-text mode for focused answers
- Proper citation of sources
- Responsive web interface

### Technical Architecture
- Frontend: Docusaurus with React components
- Backend: FastAPI with Qdrant vector database
- Vector search: Semantic similarity matching
- Deployment: GitHub Pages with CI/CD

## Project Structure

```
├── frontend/                 # Docusaurus website
│   └── my-aibook/           # Book content and UI
├── backend/                  # FastAPI backend
│   ├── main.py              # Main API server
│   ├── populate_db.py       # Content ingestion script
│   └── requirements.txt     # Python dependencies
├── specs/                    # Project specifications
└── .github/                  # CI/CD workflows
```

## Setup and Development

### Prerequisites

- Node.js (v18 or higher)
- Python (v3.9 or higher)
- Qdrant Cloud account (for vector database)

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend/my-aibook
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run start
   ```

4. Open [http://localhost:3000](http://localhost:3000) to view the book in your browser.

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables in `.env`:
   ```
   QDRANT_API_KEY="your_qdrant_api_key"
   QDRANT_URL="your_qdrant_cluster_url"
   GEMINI_API_KEY="your_gemini_api_key"  # Optional
   ```

5. Populate the database with book content:
   ```bash
   python populate_db.py
   ```

6. Start the backend server:
   ```bash
   python -m uvicorn main:app --reload
   ```

7. The backend will be available at [http://localhost:8000](http://localhost:8000)

### Running Both Together

For the complete experience, run both the frontend and backend:

1. In one terminal, start the backend:
   ```bash
   cd backend
   python -m uvicorn main:app --reload
   ```

2. In another terminal, start the frontend:
   ```bash
   cd frontend/my-aibook
   npm start
   ```

## Deployment

### GitHub Pages

The frontend is configured for deployment to GitHub Pages. The CI/CD workflow in `.github/workflows/deploy.yml` will automatically deploy the site when changes are pushed to the main branch.

### Backend Deployment

The backend can be deployed to any cloud platform that supports Python applications (e.g., Heroku, Render, AWS, Google Cloud). Update the frontend to point to your deployed backend URL.

## API Documentation

The backend API provides the following endpoints:

- `GET /` - Health check and root endpoint
- `GET /health` - System health status
- `POST /chat` - Main chat endpoint for RAG responses
- `POST /embed` - Generate embeddings for text
- `POST /retrieve` - Semantic search in the knowledge base
- `POST /add_document` - Add documents to the knowledge base

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions, please open an issue in the GitHub repository.