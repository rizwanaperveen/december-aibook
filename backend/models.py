"""Data models for the Embodied AI Systems Book RAG Chatbot"""

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
import uuid


class DocumentRecord(BaseModel):
    """Model for document records in the system"""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    module: str
    chapter: str
    anchor: Optional[str] = None
    text: str
    qdrant_id: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ChatSession(BaseModel):
    """Model for chat session records"""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    user_id: Optional[str] = None
    query: str = Field(..., min_length=1, max_length=1000)
    response: str
    citations: List[str] = []
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    use_selected_text: bool = False
    selected_text: Optional[str] = None


class ChatRequest(BaseModel):
    """Request model for chat endpoint"""
    query: str = Field(..., min_length=1, max_length=1000)
    use_selected_text: bool = False
    selected_text: Optional[str] = None


class ChatResponse(BaseModel):
    """Response model for chat endpoint"""
    response: str
    citations: List[str]
    query: str
    timestamp: datetime


class HealthResponse(BaseModel):
    """Response model for health check endpoint"""
    status: str
    timestamp: datetime


class Document(BaseModel):
    """Model for document operations"""
    id: str
    module: str
    chapter: str
    anchor: Optional[str] = None
    text: str
    qdrant_id: Optional[str] = None


class RetrieveRequest(BaseModel):
    """Request model for retrieve endpoint"""
    query: str
    limit: int = Field(default=5, ge=1, le=20)


class RetrieveResponse(BaseModel):
    """Response model for retrieve endpoint"""
    results: List[Dict[str, Any]]