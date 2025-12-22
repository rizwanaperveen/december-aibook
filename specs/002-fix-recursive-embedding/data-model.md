# Data Model: Fix Recursive Embedding and Module Coverage for Qdrant RAG

**Feature**: 002-fix-recursive-embedding | **Date**: 2025-12-22
**Input**: Feature specification from `/specs/002-fix-recursive-embedding/spec.md`

## Overview

This data model describes the entities and structures needed to support recursive embedding of all four modules (1-4) in the Qdrant RAG system. The changes focus on ensuring proper module detection and metadata during the ingestion process while maintaining backward compatibility.

## Entity: DocumentRecord

**Description**: Represents a processed document from the book content that gets embedded in Qdrant

### Fields
- **id** (string): Unique identifier for the document record (UUID format)
- **module** (string): Module name with full description (e.g., "Module 1: Robotic Nervous System (ROS 2)")
- **chapter** (string): Chapter name derived from filename
- **anchor** (string, optional): Specific section anchor within the chapter
- **text** (string): The actual text content that gets embedded
- **source_file** (string): Original filename with path
- **chunk_index** (integer): Index position when document was chunked
- **qdrant_id** (string): Unique identifier in Qdrant collection
- **created_at** (datetime): Timestamp of when record was created
- **updated_at** (datetime): Timestamp of last update

### Validation Rules
- **module**: Must be one of ["Module 1: Robotic Nervous System (ROS 2)", "Module 2: Digital Twin (Gazebo + Unity)", "Module 3: The AI-Robot Brain (NVIDIA Isaac)", "Module 4: Vision-Language-Action (VLA)"]
- **text**: Required, minimum 10 characters, maximum 10,000 characters per chunk
- **id**: Required, must be valid UUID format
- **qdrant_id**: Required, must be unique within Qdrant collection

## Entity: BookContent

**Description**: Represents the logical grouping of book content organized by modules and chapters

### Fields
- **id** (string): Unique identifier for the content piece
- **title** (string): Title of the content section
- **content** (string): Full text content (before chunking)
- **module** (string): Module identifier (see validation rules above)
- **chapter** (string): Chapter identifier within the module
- **path** (string): Relative path in the documentation structure
- **metadata** (object): Additional metadata including authors, creation date, etc.

### Relationships
- One BookContent can generate multiple DocumentRecord entries during chunking process
- DocumentRecord references BookContent through source_file field

## Entity: ModuleMetadata

**Description**: Maps directory paths to proper module names and descriptions for ingestion processing

### Fields
- **directory_pattern** (string): Pattern used to identify the module directory (e.g., "module-1", "module-3")
- **full_name** (string): Full module name with description for display and citations
- **module_number** (integer): Numeric identifier (1-4) for the module
- **description** (string): Brief description of the module content

### Values
1. **directory_pattern**: "module-1", **full_name**: "Module 1: Robotic Nervous System (ROS 2)", **module_number**: 1
2. **directory_pattern**: "module-2", **full_name**: "Module 2: Digital Twin (Gazebo + Unity)", **module_number**: 2
3. **directory_pattern**: "module-3", **full_name**: "Module 3: The AI-Robot Brain (NVIDIA Isaac)", **module_number**: 3
4. **directory_pattern**: "module-4", **full_name**: "Module 4: Vision-Language-Action (VLA)", **module_number**: 4

## Qdrant Collection Schema

### Collection Name: "embodied_ai_book"

### Vector Configuration
- **Size**: 384 (for BGE small embeddings)
- **Distance**: Cosine
- **On Disk**: false

### Payload Structure
- **doc_id** (keyword): Document record ID (from DocumentRecord.id)
- **module** (keyword): Module name for filtering (from DocumentRecord.module)
- **chapter** (keyword): Chapter name for context (from DocumentRecord.chapter)
- **text** (text): The actual content text (from DocumentRecord.text)
- **source_file** (keyword): Original source file (from DocumentRecord.source_file)
- **chunk_index** (integer): Position of chunk in original document
- **qdrant_id** (keyword): Unique Qdrant identifier

### Payload Indexes
- **module**: Keyword index for filtering by module
- **chapter**: Keyword index for chapter-level queries
- **source_file**: Keyword index for source tracking

## State Transitions

### Document Processing States
1. **Queued**: File identified for processing
2. **Processing**: File content is being extracted and processed
3. **Embedded**: Content successfully embedded in Qdrant
4. **Failed**: Processing failed (with error details)

### State Transition Rules
- **Queued → Processing**: When ingestion process begins on a file
- **Processing → Embedded**: When all chunks are successfully added to Qdrant
- **Processing → Failed**: When processing errors occur during extraction or embedding
- **Failed → Queued**: When retry is initiated for failed files

## Validation Rules Summary

### For All Modules (1-4)
- Content must be in valid markdown format
- Module names must match exactly the predefined full names
- Text chunks must be between 10 and 800 tokens (approximately 100-10,000 characters)
- File paths must be valid and accessible during ingestion
- All metadata fields must be properly populated

### Module-Specific Constraints
- **Module 1**: Must relate to ROS 2 content
- **Module 2**: Must relate to Digital Twin content
- **Module 3**: Must relate to AI-Robot Brain/NVIDIA Isaac content
- **Module 4**: Must relate to Vision-Language-Action content

## Backward Compatibility

### Preserved Elements
- Qdrant collection structure remains unchanged
- Existing document records are preserved
- API contracts remain unchanged
- Citation format (Module → Chapter) remains consistent

### New Elements
- Additional module values in the module field
- More content available in the text search
- Extended coverage for modules 3 and 4

## Data Flow

### Ingestion Process
1. **File Discovery**: Recursively find all .md files in docs/ and subdirectories
2. **Module Detection**: Determine module based on directory path
3. **Content Extraction**: Extract text content from markdown files
4. **Chunking**: Split content into appropriately sized chunks
5. **Embedding**: Generate embeddings for each chunk
6. **Storage**: Store in Qdrant with proper metadata
7. **Indexing**: Ensure proper indexing for fast retrieval