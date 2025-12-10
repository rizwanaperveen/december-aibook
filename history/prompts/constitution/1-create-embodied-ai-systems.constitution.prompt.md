---
id: 1
title: Create Embodied AI Systems Constitution
stage: constitution
date: 2025-12-10
surface: agent
model: Claude Sonnet 4.5
feature: none
branch: master
user: user
command: /sp.constitution
labels: [constitution,spec,embodied-ai]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

```text
Create a simple, clear, and practical specification for the **Embodied AI Systems Book + RAG Chatbot** project. This constitution guides writing, development, deployment, and chatbot integration.


---
## 2. Project Overview
- Write a book using **Docusaurus**.
- Use **Spec-Kit Plus** and **Claude Code** for structured authoring.
- Deploy book to **GitHub Pages**.
- Build a **RAG chatbot** that answers questions from book content using:
- FastAPI backend
- Qdrant Cloud (vectors)
- Neon Serverless Postgres (text + metadata)
- OpenAI Agents/ChatKit (frontend chat)
- Provide "Answer based on selected text" mode.


---
## 3. Book Structure
### Module 1 — **Robotic Nervous System (ROS 2)**
- ROS 2 Nodes, Topics, Services
- rclpy agent-to-ROS bridge
- URDF basics for humanoid robots


### Module 2 — **Digital Twin (Gazebo + Unity)**
- Physics simulation basics
- Unity rendering & HRI
- LiDAR, Camera, IMU sensor simulation


---
## 4. Deliverables
- Docusaurus-based book
- RAG backend (FastAPI)
- Ingestion pipeline (chunk → embed → upload)
- Chat widget embedded in book (ChatKit)
- GitHub Pages deployment


---
## 5. RAG Chatbot Requirements
- Answers must be grounded in retrieved book text.
- Selected-text mode must only use user-highlighted content.
- Provide citations (module/chapter).
- Avoid hallucinations.


---
## 6. Technical Architecture (Short)
```
Docusaurus (Book) <-> ChatKit UI
│
FastAPI RAG Backend
│
Neon Postgres + Qdrant Cloud
```


---
## 7. Data Flow
1. Book content → chunked → embedded → stored in Qdrant + Neon.
2. User query → retrieve vectors → gather relevant text.
3. LLM generates grounded answer.
4. Frontend displays answer + citations.


---
## 8. API Summary
- `/chat` — main RAG endpoint
- `/retrieve` — semantic search
- `/embed` — embeddings
```

## Response snapshot

# Embodied AI Systems Book + RAG Chatbot Constitution

## Core Principles

### I. Documentation-First Approach
Every feature and component starts with clear, comprehensive documentation in Docusaurus; All content must be well-structured, versioned, and accessible; Clear purpose and user journey required - no undocumented functionality.

### II. Grounded AI Responses (NON-NEGOTIABLE)
All RAG chatbot responses must be grounded in retrieved book text; Selected-text mode must only use user-highlighted content; Citations (module/chapter) required for all answers; No hallucinations permitted - fail gracefully if no relevant content exists.

### III. Modular Architecture
Separate services for book (Docusaurus), backend (FastAPI), vector storage (Qdrant Cloud), and database (Neon Postgres); Clear API contracts between services; Independent deployment and scaling capabilities.

### IV. Test-Driven Development
TDD mandatory: Tests written → User approved → Tests fail → Then implement; Red-Green-Refactor cycle strictly enforced; Unit tests for all RAG pipeline components.

### V. Performance and Reliability
FastAPI backend must handle concurrent queries efficiently; Semantic search responses under 2 seconds; 99.9% uptime for book and chatbot services; Proper error handling and fallback mechanisms.

### VI. Open Source and Accessibility
All code and documentation available under open source license; Deployed on GitHub Pages for public access; Accessible UI/UX following WCAG guidelines.

## Technical Architecture
- Docusaurus-based book with embedded ChatKit widget
- FastAPI RAG backend with semantic search capabilities
- Qdrant Cloud for vector embeddings and similarity search
- Neon Serverless Postgres for text content and metadata storage
- OpenAI integration for chat and embedding generation
- GitHub Actions for CI/CD and deployment automation

## Development Workflow
- Use Spec-Kit Plus and Claude Code for structured authoring
- Feature branches with pull requests for all changes
- Automated testing required before merge
- Code reviews by at least one other team member
- Pre-commit hooks to ensure code quality standards
- Semantic versioning for releases

## Governance
All development must align with this constitution; Amendments require documentation, team approval, and migration plan; All PRs/reviews must verify compliance with documentation-first and grounded AI principles; Code quality and accessibility standards must be maintained.

**Version**: 1.0.0 | **Ratified**: 2025-12-10 | **Last Amended**: 2025-12-10

## Outcome

- ✅ Impact: Created new constitution file for Embodied AI Systems Book + RAG Chatbot project
- 🧪 Tests: none
- 📁 Files: .specify/memory/constitution.md
- 🔁 Next prompts: None
- 🧠 Reflection: The constitution establishes core principles and guidelines for the project, ensuring documentation-first approach, grounded AI responses, modular architecture, and test-driven development.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A