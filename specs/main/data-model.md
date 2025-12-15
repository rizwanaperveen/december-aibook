# Data Model: Embodied AI Systems Book + RAG Chatbot

## Core Entities

### BookContent
**Definition**: Represents book chapters and sections with module, chapter, and anchor information
- **id**: string - Unique identifier for the content chunk
- **module**: string - Module identifier (e.g., "Module 1: Robotic Nervous System (ROS 2)")
- **chapter**: string - Chapter identifier (e.g., "ROS 2 Basics", "Digital Twins")
- **anchor**: string (optional) - Specific section anchor within chapter
- **text**: string - The actual content text
- **qdrant_id**: string - Reference to Qdrant vector ID

**Relationships**:
- One BookContent may have multiple citations in ChatSession responses

### DocumentRecord (Qdrant Payload)
**Definition**: Contains text content with metadata (module, chapter, anchor) and references to Qdrant vector ID
- **doc_id**: string - Reference to the original document
- **module**: string - Module identifier
- **chapter**: string - Chapter identifier
- **text**: string - Content text
- **score**: float (computed) - Similarity score from vector search

**Relationships**:
- Maps to vector embeddings in Qdrant collection
- Referenced by semantic search results

### ChatSession
**Definition**: Represents user interactions with the chatbot including queries and responses
- **id**: string - Unique session identifier
- **user_id**: string (optional) - User identifier if authenticated
- **query**: string - Original user query
- **response**: string - AI-generated response
- **citations**: string[] - List of source citations (module → chapter)
- **timestamp**: datetime - When the interaction occurred
- **use_selected_text**: boolean - Whether selected-text mode was used
- **selected_text_context**: string (optional) - The selected text used as context

**Relationships**:
- Contains references to BookContent entities via citations

## Database Schema (Neon Postgres)

### documents table
- id: UUID (primary key)
- module: VARCHAR(255)
- chapter: VARCHAR(255)
- anchor: VARCHAR(255) NULL
- text_content: TEXT
- qdrant_vector_id: VARCHAR(255)
- created_at: TIMESTAMP
- updated_at: TIMESTAMP

### chat_sessions table
- id: UUID (primary key)
- user_id: UUID (foreign key) NULL
- query_text: TEXT
- response_text: TEXT
- citations: JSONB
- use_selected_text: BOOLEAN
- selected_text: TEXT NULL
- created_at: TIMESTAMP

## Qdrant Collection Schema

### Collection: "embodied_ai_book"
**Vector Configuration**:
- Size: 384 (BGE small embedding dimensions)
- Distance: Cosine

**Payload Fields**:
- id: string
- module: string
- chapter: string
- text: string
- source_file: string
- chunk_index: integer

## Validation Rules

### BookContent
- text must be between 50 and 1000 characters
- module must be one of predefined values: ["Introduction", "Module 1: Robotic Nervous System (ROS 2)", "Module 2: Digital Twin (Gazebo + Unity)"]
- chapter must not be empty
- id must be unique

### ChatSession
- query must be between 1 and 1000 characters
- response must be provided when status is "complete"
- citations array must contain valid module → chapter references
- selected_text_context must be provided when use_selected_text is true

## State Transitions

### ChatSession States
1. **pending**: Query received, awaiting processing
2. **processing**: AI model generating response
3. **complete**: Response generated with citations
4. **error**: Processing failed

## Indexes

### Postgres
- documents(module, chapter) for fast content lookup
- documents(qdrant_vector_id) for linking with Qdrant
- chat_sessions(user_id, created_at) for user session history

### Qdrant
- Vector index on embedding vectors for semantic search
- Payload index on module and chapter fields for filtering