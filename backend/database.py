"""Database module for Neon Postgres connection and models"""

from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, JSON, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database URL - using Neon Postgres
DATABASE_URL = os.getenv("NEON_DATABASE_URL", "postgresql://username:password@localhost/dbname")

# Create engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class DocumentRecord(Base):
    """Document record model for Neon Postgres"""
    __tablename__ = "documents"

    id = Column(String, primary_key=True, index=True)
    module = Column(String, index=True)
    chapter = Column(String, index=True)
    anchor = Column(String, nullable=True)
    text_content = Column(Text)
    qdrant_vector_id = Column(String, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())


class ChatSession(Base):
    """Chat session model for Neon Postgres"""
    __tablename__ = "chat_sessions"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, index=True, nullable=True)
    query_text = Column(Text)
    response_text = Column(Text)
    citations = Column(JSON)  # Store as JSON array
    use_selected_text = Column(Boolean, default=False)
    selected_text = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=func.now())


# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create tables
def create_tables():
    """Create all tables in the database"""
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()
    print("Tables created successfully!")