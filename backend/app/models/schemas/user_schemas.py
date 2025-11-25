from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class UserOut(BaseModel):
    id: UUID
    tenant_id: UUID
    email: str
    display_name: Optional[str] = None
    role: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }