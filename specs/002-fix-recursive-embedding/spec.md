# Feature Specification: Fix Recursive Embedding and Module Coverage for Qdrant RAG

**Feature Branch**: `002-fix-recursive-embedding`
**Created**: 2025-12-22
**Status**: Draft
**Input**: User description: "sp.specify << 'EOF'
Title: Fix Recursive Embedding and Module Coverage for Qdrant RAG

Context:
The current Embodied AI Book implementation contains four modules:
- Module 1: ROS 2
- Module 2: Digital Twin
- Module 3: The AI-Robot Brain
- Module 4: Vision-Language-Action

However, the original specification defined only two modules.
Additionally, the Qdrant ingestion pipeline does not embed content from
module subdirectories (module-3/, module-4/), causing incomplete RAG coverage.

Problem Statement:
1. The ingestion script (backend/populate_db.py) only processes Markdown files
   in the root docs/ directory using a non-recursive glob.
2. Content inside docs/module-3/ and docs/module-4/ is never embedded into Qdrant.
3. Module detection logic only recognizes Modules 1 and 2.
4. The specification does not reflect the actual four-module structure,
   creating a mismatch between spec, implementation, and RAG behavior.

Goals:
- Ensure all Markdown files under docs/ (including subdirectories) are embedded.
- Ensure modules 1–4 are correctly detected, tagged, and retrievable.
- Prevent the RAG system from hallucinating or omitting module-specific answers.
- Update the specification to reflect the existing four-module structure.
- Do NOT modify or rewrite any existing book chapters.

Non-Goals:
- No changes to chapter text or documentation content.
- No restructuring of the docs folder.
- No changes to frontend UI or Docusaurus navigation.

Requirements:
1. Ingestion must recursively process all Markdown files under docs/**.
2. Each embedded chunk must include correct module metadata (module-1 … module-4).
3. Module detection must be path-based and future-proof.
4. RAG responses must be grounded strictly in embedded content.
5. The spec must explicitly define all four modules.

Acceptance Criteria:
- Queries about Modules 3 and 4 return grounded answers from their chapters.
- Qdrant collection contains vectors from all module directories.
- Module metadata is accurate and query-filtera"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Query Modules 3 and 4 Content (Priority: P1)

Readers need to ask questions about the content in modules 3 and 4 and receive accurate, cited responses based on the book material, just like they can for modules 1 and 2.

**Why this priority**: This is the core value proposition - ensuring all book content is accessible through the RAG system. Currently, modules 3 and 4 are effectively invisible to the system.

**Independent Test**: Can be fully tested by asking questions specifically about modules 3 and 4 content and verifying the responses are grounded in the correct chapters with proper citations.

**Acceptance Scenarios**:

1. **Given** a user has access to the RAG chatbot, **When** they ask a question about "whole body control" from module 3, **Then** they receive a response grounded in module 3 content with proper citations
2. **Given** a user has access to the RAG chatbot, **When** they ask a question about "vision-language-action pipelines" from module 4, **Then** they receive a response grounded in module 4 content with proper citations

---

### User Story 2 - Consistent Module Detection and Tagging (Priority: P2)

The system needs to correctly identify and tag content from all four modules during the ingestion process to ensure proper retrieval and citation accuracy.

**Why this priority**: Without proper module detection, users cannot get accurate citations or filter by specific modules, reducing the educational value of the system.

**Independent Test**: Can be tested by examining the embedded content metadata to verify that all modules are properly tagged and retrievable.

**Acceptance Scenarios**:

1. **Given** the ingestion process runs on all documentation, **When** content from module-3/ is processed, **Then** it is correctly tagged as "Module 3: The AI-Robot Brain (NVIDIA Isaac)"
2. **Given** the ingestion process runs on all documentation, **When** content from module-4/ is processed, **Then** it is correctly tagged as "Module 4: Vision-Language-Action (VLA)"

---

### User Story 3 - Recursive Content Processing (Priority: P3)

The system must process all markdown files in the documentation structure recursively, including files in subdirectories, to ensure complete content coverage.

**Why this priority**: This addresses the root cause of the issue - the current non-recursive processing that misses content in subdirectories.

**Independent Test**: Can be tested by verifying that all markdown files in all subdirectories are processed and embedded in the Qdrant database.

**Acceptance Scenarios**:

1. **Given** markdown files exist in nested directories like docs/module-3/, **When** the ingestion pipeline runs, **Then** all files are processed and embedded with correct metadata
2. **Given** new modules might be added in the future with subdirectories, **When** the ingestion pipeline runs, **Then** it processes all markdown files regardless of directory depth

---

## Edge Cases

- What happens when the system encounters deeply nested directory structures beyond the expected module levels?
- How does the system handle markdown files with identical names in different modules?
- What occurs if a module subdirectory contains non-markdown files - are they properly ignored?
- How does the system behave when processing an empty or malformed markdown file in a subdirectory?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST recursively process all Markdown files under docs/ directory and all subdirectories
- **FR-002**: System MUST correctly identify module names based on directory path structure (module-1/, module-2/, module-3/, module-4/)
- **FR-003**: System MUST embed content from all four modules (1-4) into the Qdrant vector database with accurate metadata
- **FR-004**: System MUST provide citations showing Module → Chapter for all chatbot responses, including those from modules 3 and 4
- **FR-005**: System MUST return grounded responses for queries about modules 3 and 4 content with proper source citations
- **FR-006**: System MUST maintain existing functionality for modules 1 and 2 while adding support for modules 3 and 4
- **FR-007**: System MUST preserve existing book chapter content without modification during the ingestion process

### Key Entities *(include if feature involves data)*

- **BookContent**: Represents book chapters and sections with module, chapter, and anchor information across all four modules
- **DocumentRecord**: Contains text content with metadata (module, chapter, anchor) and references to Qdrant vector ID for all modules
- **ModuleMetadata**: Information that maps directory paths to proper module names and descriptions for modules 1-4

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Queries about modules 3 and 4 return grounded answers with citations 95% of the time for relevant questions
- **SC-002**: All markdown files in module subdirectories are successfully embedded in Qdrant database (100% coverage)
- **SC-003**: Module metadata is accurate and query-filterable for all four modules in the RAG system
- **SC-004**: RAG response quality for modules 3 and 4 matches the quality achieved for modules 1 and 2
- **SC-005**: System maintains backward compatibility - modules 1 and 2 functionality remains unchanged