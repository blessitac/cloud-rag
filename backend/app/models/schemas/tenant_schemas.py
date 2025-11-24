from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class TenantOut(BaseModel):
    id: UUID
    name: str
    slug: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }