from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from .message import MessageResponse

class SessionCreate(BaseModel):
    title: Optional[str] = "New Conversation"

class SessionResponse(BaseModel):
    id: str
    user_id: str
    title: str
    created_at: datetime
   

    class Config:
        from_attributes = True