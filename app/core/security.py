from datetime import datetime, timedelta
import hashlib
from typing import Any, Union
from jose import jwt
from passlib.context import CryptContext
from app.core.config import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Returns a hashed version of the raw password."""
  
    safe_password = password.encode('utf-8')[:72]
    return pwd_context.hash(safe_password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Checks if the plain password matches the stored hash."""
    
    safe_password = plain_password.encode('utf-8')[:72]
    return pwd_context.verify(safe_password, hashed_password)

def create_access_token(subject: Union[str, Any]) -> str:
    """Generates a JWT token valid for a specific duration."""
    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(
        to_encode, 
        settings.SECRET_KEY, 
        algorithm=settings.ALGORITHM
    )
    return encoded_jwt