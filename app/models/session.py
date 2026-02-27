import uuid
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.db.base import Base

class Session(Base):
    __tablename__ = "sessions"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(255), default="New Conversation")
    created_at = Column(DateTime(timezone=True), server_default=func.now())