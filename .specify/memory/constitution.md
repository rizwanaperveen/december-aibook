<!--
SYNC IMPACT REPORT:
Version change: N/A → 1.0.0
Modified principles: N/A (new constitution)
Added sections: All sections (new constitution)
Removed sections: N/A
Templates requiring updates: ⚠ pending - .specify/templates/plan-template.md, .specify/templates/spec-template.md, .specify/templates/tasks-template.md
Follow-up TODOs: None
-->
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