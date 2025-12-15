# Research: Embodied AI Systems Book + RAG Chatbot

## Decision: Tech Stack Selection
**Rationale**: Selected proven technologies that align with the project requirements and constitution principles.
- **Frontend**: Docusaurus + React for documentation-first approach and extensibility
- **Backend**: FastAPI for high-performance async API with excellent TypeScript compatibility
- **Vector DB**: Qdrant for semantic search capabilities and cloud availability
- **AI**: Google Generative AI for grounded responses with citation support

## Alternatives Considered:
- **Frontend alternatives**: Gatsby, VuePress, Sphinx - Docusaurus chosen for React ecosystem compatibility
- **Backend alternatives**: Flask, Express, Django - FastAPI chosen for async performance and OpenAPI docs
- **Vector DB alternatives**: Pinecone, Weaviate, Supabase - Qdrant chosen for open-source flexibility
- **AI alternatives**: OpenAI, Anthropic, HuggingFace - Google GenAI chosen for integration capabilities

## Decision: Architecture Pattern
**Rationale**: Microservices architecture with separate frontend and backend to ensure modularity per constitution.
- **Frontend service**: Docusaurus static site with embedded chat widget
- **Backend service**: FastAPI with RAG pipeline and vector search
- **Data layer**: Qdrant for embeddings, Neon Postgres for metadata

## Decision: Content Processing Pipeline
**Rationale**: Efficient pipeline to convert book content to searchable vector representations.
- **Source**: Markdown files in Docusaurus docs structure
- **Processing**: Chunking with overlap, embedding generation, vector upload
- **Storage**: Qdrant Cloud for semantic search, Neon for metadata

## Decision: Selected-Text Mode Implementation
**Rationale**: Browser text selection API with context restriction for grounded responses.
- **Mechanism**: JavaScript selection API to capture highlighted text
- **Restriction**: Send selected text as context to LLM, limiting response scope
- **Citation**: Mark responses as "Selected Text Only" for transparency

## Decision: Deployment Strategy
**Rationale**: GitHub Pages for frontend (static), cloud provider for backend (dynamic) for cost-effectiveness.
- **Frontend**: GitHub Pages for static Docusaurus site
- **Backend**: Container deployment (Docker) for FastAPI app
- **CDN**: For asset delivery and performance optimization