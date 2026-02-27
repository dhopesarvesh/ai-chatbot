import uuid
from sqlalchemy import Column, String, ForeignKey, Text, Enum, DateTime
from sqlalchemy.sql import func
from app.db.base import Base
import enum

class MessageRole(str, enum.Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"

class Message(Base):
    __tablename__ = "messages"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    session_id = Column(String(36), ForeignKey("sessions.id", ondelete="CASCADE"), nullable=False)
    role = Column(Enum(MessageRole), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())