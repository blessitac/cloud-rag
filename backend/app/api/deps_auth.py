from fastapi import Depends, HTTPException, Header
from sqlalchemy.orm import Session
from uuid import UUID
from typing import Optional
from app.db.database import get_db
from app.models.domain.user import User

def get_current_user(
    db: Session = Depends(get_db),
    x_demo_user_id: Optional[str] = Header(default=None)
) -> User:
    """
    Get the current user based on X-Demo-User-Id header.
    This is a simple stub for development - NOT production ready.
    """
    if not x_demo_user_id:
        raise HTTPException(
            status_code=401,
            detail="X-Demo-User-Id header is required"
        )
    
    try:
        user_id = UUID(x_demo_user_id)
    except ValueError:
        raise HTTPException(
            status_code=401,
            detail="Invalid user ID format"
        )
    
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )
    
    return user