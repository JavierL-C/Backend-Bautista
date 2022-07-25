import re
from urllib import response
from fastapi import APIRouter, HTTPException, Path, Depends
from app.db.config import SessionLocal
from sqlalchemy.orm import Session
from app.schemas.user_schemas import UserSchema, RequestUser, Response
from app.db import user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()
    
@router.get("/")
async def get(db:Session=Depends(get_db)):
    _user = user.get_user(db,0,100)
    return Response(code=200, status="ok",message="Success fetch all data", result=_user)
    