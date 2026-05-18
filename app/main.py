from fastapi import FastAPI
from app.old.api.routes import auth
from app.old.db.base import Base
from app.old.db.session import engine
from app.old.api.routes import task

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(task.router, prefix="/tasks", tags=["Tasks"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])

@app.get("/")
def home():
    return {"message": "API + Postgres OK 🚀"}