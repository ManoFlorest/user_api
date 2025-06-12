from fastapi import FastAPI
from app.routers import users
from app.database import create_db

app = FastAPI(title="User API", version="1.0")

create_db()

app.include_router(users.router)