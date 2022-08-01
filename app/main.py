from fastapi import FastAPI
from app.models import user
from app.db.config import engine
from app.routers import user_routers
from fastapi.middleware.cors import CORSMiddleware

user.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def Home():
    return "Welcome Home"

app.include_router(user_routers.router,prefix="/user", tags=["user"])