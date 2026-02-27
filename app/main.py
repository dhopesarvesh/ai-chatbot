import os
from fastapi import FastAPI
from app.api import auth

from app.api import auth, session, messages




app = FastAPI(title="AI Chatbot API")


app.include_router(auth.router, prefix="/api")
app.include_router(session.router, prefix="/api")
app.include_router(messages.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Chatbot API"}
