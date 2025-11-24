from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager
from app.core.config import settings

# Only create engine if connection string is provided
engine = None
SessionLocal = None

if settings.SUPABASE_DB_CONNECTION_STRING:
    engine = create_engine(
        settings.SUPABASE_DB_CONNECTION_STRING,
        echo=settings.DB_ECHO,
        future=True,
    )
    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

def get_db():
    if not SessionLocal:
        raise RuntimeError("Database not configured. Please set SUPABASE_DB_CONNECTION_STRING in your environment.")
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()