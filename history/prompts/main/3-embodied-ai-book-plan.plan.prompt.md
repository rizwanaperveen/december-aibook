---
id: 3
title: Embodied AI Book Plan Creation
stage: plan
date: 2025-12-12
surface: agent
model: Claude Sonnet 4.5
feature: main
branch: main
user: user
command: /sp.plan
labels: [plan,embodied-ai,book,rag,chatbot]
links:
  spec: specs/001-embodied-ai-book/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/main/plan.md
 - specs/main/research.md
 - specs/main/data-model.md
 - specs/main/quickstart.md
 - specs/main/contracts/openapi.yaml
tests:
 - none
---

## Prompt

```text
$ARGUMENTS
```

## Response snapshot

# Implementation Plan: Embodied AI Systems Book + RAG Chatbot

**Branch**: `main` | **Date**: 2025-12-12 | **Spec**: [link](../001-embodied-ai-book/spec.md)
**Input**: Feature specification from `/specs/001-embodied-ai-book/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implementation of a Docusaurus-based technical book with two modules (ROS 2 & Digital Twin), enhanced with an integrated RAG chatbot connected to a FastAPI backend, Qdrant vector DB, and Neon Postgres. The system provides grounded AI responses based on book content with proper citations and selected-text mode functionality.

## Technical Context

**Language/Version**: Python 3.12, TypeScript/JavaScript, Node.js 20+
**Primary Dependencies**: FastAPI, Docusaurus, Qdrant Client, React, Google Generative AI, @google/generative-ai
**Storage**: Qdrant Cloud (vector database), Neon Postgres (metadata), GitHub Pages (static hosting)
**Testing**: pytest, Jest, React Testing Library
**Target Platform**: Web application (Linux server backend, cross-platform frontend)
**Project Type**: web - with separate frontend and backend components
**Performance Goals**: <2 seconds response time for RAG queries, 99.9% uptime for book and chatbot services
**Constraints**: <200ms p95 for API responses, secure API key handling, offline-capable documentation
**Scale/Scope**: Support 100 concurrent users, 10k+ book content chunks in vector database

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- ✅ Documentation-First Approach: Docusaurus-based book content with comprehensive documentation
- ✅ Grounded AI Responses: RAG chatbot responses grounded in book content with citations
- ✅ Modular Architecture: Separate services for book (Docusaurus), backend (FastAPI), vector storage (Qdrant Cloud), and database (Neon Postgres)
- ✅ Performance and Reliability: Target <2s response time for semantic search
- ✅ Open Source and Accessibility: Deployed on GitHub Pages for public access

## Project Structure

### Documentation (this feature)

```text
specs/main/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── populate_db.py       # Content ingestion script
├── gemini_chat.py       # Gemini integration module
└── .env                 # Environment variables

frontend/my-aibook/
├── docs/                # Book content markdown files
├── src/
│   ├── components/
│   │   └── Chatbot/     # Chatbot React component
│   ├── utils/
│   │   └── bookContent.ts # Book content utilities
│   └── pages/
│       └── chat.tsx     # Chat interface page
├── docusaurus.config.ts # Docusaurus configuration
├── sidebars.ts          # Navigation configuration
└── package.json         # Frontend dependencies

scripts/
├── process-docs.js      # Process book content for frontend consumption

specs/
├── 001-embodied-ai-book/ # Original specification
└── main/                # Current plan and research artifacts
```

**Structure Decision**: Web application with separate backend and frontend components to enable modular architecture as required by the constitution. The backend handles RAG processing and API endpoints, while the frontend manages the book presentation and chat interface.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Multiple services | Required for modular architecture per constitution | Tight coupling would violate "Modular Architecture" principle |
| Vector database | Required for semantic search functionality | Keyword search would not provide adequate RAG capabilities |

## Outcome

- ✅ Impact: Created comprehensive implementation plan for Embodied AI Systems Book + RAG Chatbot project
- 🧪 Tests: none
- 📁 Files: specs/main/plan.md, specs/main/research.md, specs/main/data-model.md, specs/main/quickstart.md, specs/main/contracts/openapi.yaml
- 🔁 Next prompts: /sp.tasks to generate implementation tasks
- 🧠 Reflection: The plan establishes a solid foundation for the project with clear architecture and implementation phases.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A