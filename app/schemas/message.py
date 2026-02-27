from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class MessageRole(str, Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"

class MessageCreate(BaseModel):
    content: str


class MessageResponse(BaseModel):
    id: str
    session_id: str
    role: MessageRole
    content: str
    created_at: datetime

    class Config:
        from_attributes = True