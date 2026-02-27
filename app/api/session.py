from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session as DBSession
from typing import List

from app.db.session import get_db
from app.api.deps import get_current_user
from app.models.user import User
from app.models.session import Session as ChatSession
from app.schemas.session import SessionCreate, SessionResponse

router = APIRouter(prefix="/sessions", tags=["Sessions"])

@router.post("/", response_model=SessionResponse)
def create_session(
    session_in: SessionCreate, 
    db: DBSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new chat session for the logged-in user."""
    new_session = ChatSession(
        user_id=current_user.id,
        title=session_in.title
    )
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return new_session

@router.get("/", response_model=List[SessionResponse])
def list_sessions(
    db: DBSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Fetch all chat sessions belonging to the current user."""
    sessions = db.query(ChatSession).filter(ChatSession.user_id == current_user.id).all()
    return sessions