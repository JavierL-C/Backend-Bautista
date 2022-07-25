from fastapi import FastAPI
from app.models import user
from app.db.config import engine
from app.routers import user_routers

user.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
async def Home():
    return "Welcome Home"

app.include_router(user_routers.router,prefix="/user", tags=["user"])