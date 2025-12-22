---
description: "Task list for Embodied AI Systems Book + RAG Chatbot implementation"
---

# Tasks: Embodied AI Systems Book + RAG Chatbot

**Input**: Design documents from `/specs/001-embodied-ai-book/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `backend/src/`, `frontend/src/`
- Paths shown below assume web app structure based on plan.md

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan with backend/ and frontend/my-aibook/ directories
- [X] T002 [P] Initialize backend Python project with FastAPI, Qdrant client, Google Generative AI dependencies in backend/requirements.txt
- [X] T003 [P] Initialize frontend Docusaurus project with React, Google Generative AI dependencies in frontend/my-aibook/package.json
- [X] T004 [P] Configure linting and formatting tools for both backend and frontend

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T005 Setup Qdrant collection schema for "embodied_ai_book" with proper vector dimensions and payload fields
- [X] T006 [P] Create backend FastAPI application structure in backend/main.py with proper routing
- [X] T007 [P] Setup environment configuration management for API keys in backend/.env and frontend/.env
- [X] T008 Create data models for DocumentRecord and ChatSession in backend models
- [X] T009 Configure CORS middleware in backend to allow frontend communication
- [X] T010 Implement basic health check endpoint in backend/main.py
- [X] T011 Setup database connection for Neon Postgres if needed

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Read Technical Book Content (Priority: P1) 🎯 MVP

**Goal**: Provide Docusaurus-based book content with Module 1 (ROS 2) and Module 2 (Digital Twin) content accessible to readers

**Independent Test**: Can be fully tested by navigating through book chapters and verifying content readability and structure

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T012 [P] [US1] Contract test for frontend book content accessibility in tests/contract/test_book_content.py
- [ ] T013 [P] [US1] Integration test for book navigation in tests/integration/test_book_navigation.py

### Implementation for User Story 1

- [X] T014 [P] [US1] Create Docusaurus configuration in frontend/my-aibook/docusaurus.config.ts with proper GitHub Pages settings
- [X] T015 [P] [US1] Create sidebar navigation in frontend/my-aibook/sidebars.ts for both modules
- [X] T016 [US1] Add initial book content for Module 1: Robotic Nervous System (ROS 2) in frontend/my-aibook/docs/
- [X] T017 [US1] Add initial book content for Module 2: Digital Twin (Gazebo + Unity) in frontend/my-aibook/docs/
- [X] T018 [US1] Implement book content processing script in frontend/my-aibook/scripts/process-docs.js to convert markdown to searchable JSON
- [X] T019 [US1] Create book content utility functions in frontend/my-aibook/src/utils/bookContent.ts to fetch and search content
- [X] T020 [US1] Test book content accessibility and navigation in development environment

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Ask Questions About Book Content (Priority: P2)

**Goal**: Provide a RAG chatbot that answers questions based only on book content with selected-text mode and citations

**Independent Test**: Can be tested by asking various questions about book content and verifying the responses are accurate and properly cited

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T021 [P] [US2] Contract test for /chat endpoint in backend/tests/contract/test_chat_endpoint.py
- [ ] T022 [P] [US2] Integration test for chatbot question-answering in backend/tests/integration/test_chatbot.py

### Implementation for User Story 2

- [X] T023 [P] [US2] Create Gemini chat integration module in backend/gemini_chat.py
- [X] T024 [US2] Implement /chat endpoint in backend/main.py with RAG functionality
- [X] T025 [US2] Implement /retrieve endpoint in backend/main.py for semantic search
- [X] T026 [US2] Implement /embed endpoint in backend/main.py for generating embeddings
- [X] T027 [US2] Create Qdrant client integration functions in backend for vector search
- [X] T028 [US2] Implement selected-text mode functionality in backend RAG logic
- [X] T029 [US2] Add citation generation to chat responses with Module → Chapter references
- [X] T030 [P] [US2] Create React Chatbot component in frontend/my-aibook/src/components/Chatbot/Chatbot.tsx
- [X] T031 [US2] Implement Google Generative AI integration in frontend Chatbot component
- [X] T032 [US2] Add selected-text mode UI functionality to Chatbot component
- [X] T033 [US2] Implement citation display in Chatbot component responses
- [X] T034 [US2] Connect frontend Chatbot to backend /chat endpoint
- [X] T035 [US2] Test chatbot functionality with various book content questions

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Search and Retrieve Book Information (Priority: P3)

**Goal**: Enable efficient navigation and information discovery across the book content through search functionality

**Independent Test**: Can be tested by entering search queries and verifying relevant content is returned with proper citations

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T036 [P] [US3] Contract test for /retrieve endpoint in backend/tests/contract/test_retrieve_endpoint.py
- [ ] T037 [P] [US3] Integration test for search functionality in backend/tests/integration/test_search.py

### Implementation for User Story 3

- [X] T038 [P] [US3] Enhance book content search utility in frontend/my-aibook/src/utils/bookContent.ts
- [X] T039 [US3] Implement advanced text chunking algorithm in backend/populate_db.py (800 tokens, 100 overlap)
- [X] T040 [US3] Create content ingestion pipeline in backend/populate_db.py to process markdown files
- [X] T041 [US3] Implement vector embedding generation and storage in Qdrant from book content
- [X] T042 [US3] Add semantic search functionality with proper scoring and relevance ranking
- [ ] T043 [US3] Create search UI component integrated with book navigation in frontend
- [ ] T044 [US3] Test search functionality with various queries and verify citation accuracy

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Ingest Pipeline Implementation

**Goal**: Implement the full pipeline to read markdown files, chunk text, generate embeddings, and store in Qdrant and Neon Postgres

- [X] T045 [P] Implement text chunking utility in backend/utils/text_chunker.py (800 tokens, 100 overlap)
- [X] T046 [P] Create markdown parser utility in backend/utils/markdown_parser.py to extract content with metadata
- [X] T047 Create ingestion pipeline script in backend/populate_db.py that processes all docs/ content
- [X] T048 Implement embedding generation and Qdrant upload functionality in backend
- [X] T049 Create document record storage in Neon Postgres with proper metadata
- [X] T050 Test full ingestion pipeline with sample book content

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T051 [P] Documentation updates in docs/README.md and specs/main/quickstart.md
- [X] T052 Code cleanup and refactoring across backend and frontend
- [X] T053 Performance optimization for RAG query response times
- [ ] T054 [P] Add unit tests for backend API endpoints in backend/tests/unit/
- [X] T055 Security hardening for API key handling and input validation
- [X] T056 Run quickstart.md validation to ensure deployment works correctly
- [X] T057 Configure GitHub Pages deployment workflow
- [X] T058 Add error handling for edge cases (no content found, API errors, etc.)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Ingest Pipeline (Phase 6)**: Depends on Foundational phase completion
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence