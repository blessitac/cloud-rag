from fastapi import APIRouter, Depends
from app.api.deps_auth import get_current_user
from app.models.domain.user import User
from app.models.schemas.user_schemas import UserOut

router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/me", response_model=UserOut)
def get_me(current_user: User = Depends(get_current_user)):
    """
    Get current user information.
    Requires X-Demo-User-Id header with a valid user UUID.
    """
    return current_user