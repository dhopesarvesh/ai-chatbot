#  AI Chatbot 

A production-grade RESTful API built with **FastAPI**, **MySQL**, and **Google Gemini AI**. This system supports secure user authentication, persistent chat sessions, and context-aware AI conversations.

---

## Architecture Explanation

The project follows **Clean Architecture** principles, ensuring that the business logic is decoupled from the database and the API framework.



* **API Layer (`app/api`)**: Controllers that handle request routing, Pydantic validation, and dependency injection.
* **Database Layer (`app/db` & `app/models`)**: Managed by SQLAlchemy ORM. It handles connection pooling and maps Python classes to MySQL tables.
* **Core Layer (`app/core`)**: Centralized configuration management and security (JWT/Hashing) logic.
* **Schemas (`app/schemas`)**: Pydantic models for data serialization and strict type enforcement.

---

## Setup Instructions

### 1. Prerequisites
* Python 3.10+
* MySQL Server
* Gemini API Key ([Get it here](https://aistudio.google.com/))

### 2. Environment Configuration
Create a `.env` file in the root directory:
```env
MYSQL_USER=your_user
MYSQL_PASSWORD=your_password
MYSQL_SERVER=localhost
MYSQL_PORT=3306
MYSQL_DB=chatbot_db

SECRET_KEY=your_super_secret_random_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

GEMINI_API_KEY=your_actual_gemini_key
```

# 1. Create virtual environment
python -m venv chatbot_env

# 2. Activate environment
# On Mac/Linux:
source chatbot_env/bin/activate 
# On Windows:
.\chatbot_env\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the server
uvicorn app.main:app --reload

# Tech Stack
Framework: FastAPI

Database: MySQL

ORM: SQLAlchemy

AI: Google Generative AI (Gemini)

Auth: JWT (JSON Web Tokens)

# For APIS refer to localhost:8000/docs (after successfull running of application)
