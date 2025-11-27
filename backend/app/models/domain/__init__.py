# backend/app/models/domain/__init__.py

from app.db.base import Base  # make sure Base is defined first

from .tenant import Tenant
from .user import User
from .knowledge_base import KnowledgeBase
from .document import Document
from .chat import ChatSession, Message

__all__ = [
    "Tenant",
    "User",
    "KnowledgeBase",
    "Document",
    "ChatSession",
    "Message",
]
