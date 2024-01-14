


from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field, field_serializer


class TimestampSchema(BaseModel):
    created_at: datetime = Field(default_factory=lambda:  datetime.utcnow().replace(tzinfo=None))
    updated_at: datetime|None = Field(default=None)

    @field_serializer("created_at")
    def serialize_dt(self, created_at: datetime | None, _info: Any) -> str | None:
        if created_at is not None:
            return created_at.isoformat()
        
        return None

    @field_serializer("updated_at")
    def serialize_updated_at(self, updated_at: datetime | None, _info: Any) -> str | None:
        if updated_at is not None:
            return updated_at.isoformat()

        return None