---
id: 2
title: Create Embodied AI Systems Spec
stage: spec
date: 2025-12-10
surface: agent
model: Claude Sonnet 4.5
feature: embodied-ai-book
branch: 001-embodied-ai-book
user: user
command: /sp.specify
labels: [spec,embodied-ai,book,rag]
links:
  spec: specs/001-embodied-ai-book/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-embodied-ai-book/spec.md
 - specs/001-embodied-ai-book/checklists/requirements.md
tests:
 - none
---

## Prompt

```text
# sp.specification (Simplified)

This specification defines the **scope, structure, and tasks** for the *Embodied AI Systems Book + RAG Chatbot* project, based directly on the simplified constitution.

---

## 1. Project Summary

A Docusaurus-based technical book with two modules (ROS 2 & Digital Twin), enhanced with an integrated RAG chatbot connected to a FastAPI backend, Qdrant vector DB, and Neon Postgres.

---

## 2. Objectives

* Write a clear, structured technical book.
* Deploy book to GitHub Pages.
* Build a RAG chatbot with selected-text answering capability.
* Maintain simple, clean, developer-friendly architecture.

---

## 3. Book Structure

### Module 1: Robotic Nervous System (ROS 2)

* ROS 2 Nodes, Topics, Services
* rclpy agent → ROS control bridge
* URDF basics for humanoids

### Module 2: Digital Twin (Gazebo + Unity)

* Physics simulation basics
* Unity-based high‑fidelity visualization
* Sensor simulations (LiDAR, Depth Camera, IMU)

---

## 4. System Architecture (High-Level)

```
Docusaurus Site (Book)
   │
   ├─ ChatKit Chat Widget (Frontend)
   │
FastAPI RAG Backend
   │
   ├─ Qdrant Cloud (Vectors)
   └─ Neon Postgres (Text + Metadata)
```

---

## 5. Functional Requirements

### Book

* Chapters written using Spec-Kit + Claude Code.
* Markdown structured for Docusaurus.
* Includes examples, diagrams, and code snippets.

### Chatbot

* Answers questions based on book content.
* Selected-text mode: restrict LLM answer ONLY to highlighted text.
* Provide citations: Module → Chapter.

### Backend

* Endpoints:

  * `/chat`
  * `/retrieve`
  * `/embed`
  * `/health`
* Embedding + chunking pipeline.
* Qdrant semantic search.

---

## 6. Data Model

### Document Record (Neon)

* id
* module
* chapter
* anchor
* text
* qdrant_id

### Qdrant Payload

* doc_id
* module
* chapter
* score

---

## 7. Ingest Pipeline

1. Read markdown files.
2. Chunk text (800 tokens, 100 overlap).
3. Generate embeddings.
4. Upload to Qdrant + Neon.

---

## 8. Developer Tasks

### Phase 1: Authoring

* Create project folders: `spec/`, `website/`, `api/`.
* Write Module 1 chapters.

### Phase 2: Backend

* Implement FastAPI RAG.
* Set up Neon tables.
* Create Qdrant collections.

### Phase 3: Frontend

* Add ChatKit widget to Docusaurus.
* Add selected-text button.

### Phase 4: Deployment

* Deploy book to GitHub Pages.
* Deploy API container (local/cloud).

---

## 9. Acceptance Criteria

* Book deployed + readable.
* Chatbot answers grounded + cited responses.
* Selected text mode works.
* Retrieval accuracy validated with tests.

---

## 10. Simplicity Rules

* Avoid complex architectures.
* Minimal configuration.
* Foc
```

## Response snapshot

# Feature Specification: Embodied AI Systems Book + RAG Chatbot

**Feature Branch**: `001-embodied-ai-book`
**Created**: 2025-12-10
**Status**: Draft
**Input**: User description: "sp.specification (Simplified)

This specification defines the **scope, structure, and tasks** for the *Embodied AI Systems Book + RAG Chatbot* project, based directly on the simplified constitution.

---

## 1. Project Summary

A Docusaurus-based technical book with two modules (ROS 2 & Digital Twin), enhanced with an integrated RAG chatbot connected to a FastAPI backend, Qdrant vector DB, and Neon Postgres.

---

## 2. Objectives

* Write a clear, structured technical book.
* Deploy book to GitHub Pages.
* Build a RAG chatbot with selected-text answering capability.
* Maintain simple, clean, developer-friendly architecture.

---

## 3. Book Structure

### Module 1: Robotic Nervous System (ROS 2)

* ROS 2 Nodes, Topics, Services
* rclpy agent → ROS control bridge
* URDF basics for humanoids

### Module 2: Digital Twin (Gazebo + Unity)

* Physics simulation basics
* Unity-based high‑fidelity visualization
* Sensor simulations (LiDAR, Depth Camera, IMU)

---

## 4. System Architecture (High-Level)

```
Docusaurus Site (Book)
   │
   ├─ ChatKit Chat Widget (Frontend)
   │
FastAPI RAG Backend
   │
   ├─ Qdrant Cloud (Vectors)
   └─ Neon Postgres (Text + Metadata)
```

---

## 5. Functional Requirements

### Book

* Chapters written using Spec-Kit + Claude Code.
* Markdown structured for Docusaurus.
* Includes examples, diagrams, and code snippets.

### Chatbot

* Answers questions based on book content.
* Selected-text mode: restrict LLM answer ONLY to highlighted text.
* Provide citations: Module → Chapter.

### Backend

* Endpoints:

  * `/chat`
  * `/retrieve`
  * `/embed`
  * `/health`
* Embedding + chunking pipeline.
* Qdrant semantic search.

---

## 6. Data Model

### Document Record (Neon)

* id
* module
* chapter
* anchor
* text
* qdrant_id

### Qdrant Payload

* doc_id
* module
* chapter
* score

---

## 7. Ingest Pipeline

1. Read markdown files.
2. Chunk text (800 tokens, 100 overlap).
3. Generate embeddings.
4. Upload to Qdrant + Neon.

---

## 8. Developer Tasks

### Phase 1: Authoring

* Create project folders: `spec/`, `website/`, `api/`.
* Write Module 1 chapters.

### Phase 2: Backend

* Implement FastAPI RAG.
* Set up Neon tables.
* Create Qdrant collections.

### Phase 3: Frontend

* Add ChatKit widget to Docusaurus.
* Add selected-text button.

### Phase 4: Deployment

* Deploy book to GitHub Pages.
* Deploy API container (local/cloud).

---

## 9. Acceptance Criteria

* Book deployed + readable.
* Chatbot answers grounded + cited responses.
* Selected text mode works.
* Retrieval accuracy validated with tests.

---

## 10. Simplicity Rules

* Avoid complex architectures.
* Minimal configuration.
* Foc"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Read Technical Book Content (Priority: P1)

Readers need to access structured technical content about embodied AI systems with clear examples and diagrams.

**Why this priority**: This is the core value proposition - providing educational content about embodied AI systems.

**Independent Test**: Can be fully tested by navigating through book chapters and verifying content readability and structure.

**Acceptance Scenarios**:

1. **Given** a user visits the deployed book site, **When** they browse Module 1 on ROS 2, **Then** they see well-structured content with examples about Nodes, Topics, and Services
2. **Given** a user is reading Module 2 on Digital Twin, **When** they view content about Unity visualization, **Then** they see clear explanations with relevant diagrams and code snippets

---

### User Story 2 - Ask Questions About Book Content (Priority: P2)

Readers need to ask questions about the book content and get accurate, cited responses based on the book material.

**Why this priority**: Enhances learning experience by providing immediate answers to questions about the content.

**Independent Test**: Can be tested by asking various questions about book content and verifying the responses are accurate and properly cited.

**Acceptance Scenarios**:

1. **Given** a user has read book content about ROS 2, **When** they ask a question about ROS 2 topics in the chat widget, **Then** they receive a response grounded in the book content with proper citations
2. **Given** a user has selected specific text in the book, **When** they ask a question about that text in selected-text mode, **Then** the response is restricted to information from the highlighted content only

---

### User Story 3 - Search and Retrieve Book Information (Priority: P3)

Readers need to search for specific topics across the book and find relevant information quickly.

**Why this priority**: Enables efficient navigation and information discovery across the book content.

**Independent Test**: Can be tested by entering search queries and verifying relevant content is returned with proper citations.

**Acceptance Scenarios**:

1. **Given** a user wants to find information about URDF in the book, **When** they search for "URDF basics", **Then** they receive results from relevant chapters with module and chapter citations

---

### Edge Cases

- What happens when the RAG backend is temporarily unavailable? The system should display a user-friendly error message indicating temporary unavailability and suggest trying again later.
- How does the system handle very long user queries or questions? The system should implement a reasonable query length limit (e.g., 1000 characters) and display an informative message if the query exceeds this limit.
- What happens when no relevant content is found for a user's question? The system should respond with a message indicating that no relevant content was found in the book and suggest rephrasing the question or browsing the book content directly.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST serve Docusaurus-based book content with Module 1 (ROS 2) and Module 2 (Digital Twin) content
- **FR-002**: System MUST provide a RAG chatbot that answers questions based only on book content
- **FR-003**: System MUST provide selected-text mode that restricts answers to highlighted content only
- **FR-004**: System MUST provide citations showing Module → Chapter for all chatbot responses
- **FR-005**: System MUST store book content in Neon Postgres with metadata and Qdrant for vector search
- **FR-006**: System MUST provide FastAPI endpoints: `/chat`, `/retrieve`, `/embed`, `/health`
- **FR-007**: System MUST implement an ingestion pipeline that chunks markdown files (800 tokens, 100 overlap) and generates embeddings
- **FR-008**: System MUST deploy book to GitHub Pages for public access

### Key Entities *(include if feature involves data)*

- **BookContent**: Represents book chapters and sections with module, chapter, and anchor information
- **DocumentRecord**: Contains text content with metadata (module, chapter, anchor) and references to Qdrant vector ID
- **ChatSession**: Represents user interactions with the chatbot including queries and responses

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Book is successfully deployed to GitHub Pages and accessible to users
- **SC-002**: Chatbot provides grounded responses with citations for 95% of valid questions about book content
- **SC-003**: Selected-text mode correctly restricts responses to highlighted content in 100% of test cases
- **SC-004**: Retrieval accuracy validated with tests showing 90%+ relevant results for sample queries
- **SC-005**: System handles 100 concurrent users without degradation in response quality or performance.

## Outcome

- ✅ Impact: Created comprehensive specification for Embodied AI Systems Book + RAG Chatbot project
- 🧪 Tests: none
- 📁 Files: specs/001-embodied-ai-book/spec.md, specs/001-embodied-ai-book/checklists/requirements.md
- 🔁 Next prompts: /sp.plan to create implementation plan
- 🧠 Reflection: The specification clearly defines user stories, functional requirements, and success criteria for the book and RAG chatbot system.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A