import google.generativeai as genai
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session as DBSession
from app.db.session import get_db
from app.api.deps import get_current_user
from app.models.user import User
from app.models.message import Message
from app.models.session import Session as ChatSession
from app.schemas.message import MessageCreate, MessageResponse
from app.core.config import settings

router = APIRouter(prefix="/messages", tags=["Messages"])


genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

@router.post("/{session_id}", response_model=MessageResponse)
def send_message(
    session_id: str,
    message_in: MessageCreate,
    db: DBSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
   
    chat_session = db.query(ChatSession).filter(
        ChatSession.id == session_id, 
        ChatSession.user_id == current_user.id
    ).first()
    
    if not chat_session:
        raise HTTPException(status_code=404, detail="Session not found")


    user_msg = Message(
        session_id=session_id,
        role="user",
        content=message_in.content
    )
    db.add(user_msg)
    
   
    try:
        
        response = model.generate_content(message_in.content)
        ai_content = response.text
    except Exception as e:
        ai_content = "Sorry, I'm having trouble connecting to my brain right now."

   
    ai_msg = Message(
        session_id=session_id,
        role="assistant",
        content=ai_content
    )
    db.add(ai_msg)
    
    db.commit()
    db.refresh(ai_msg)
    return ai_msg