from urllib import response
from fastapi import APIRouter, HTTPException, Path, Depends, status
from requests import session
from sqlalchemy import null
from sqlalchemy.orm import Session
import os
import jwt

from app.db.config import SessionLocal
from app.schemas.user_schemas import UserSchema, RequestUser, UserResponse, RequestLogin
from app.db import user
from app.utils.auth import Encrypter

secret_pass = os.getenv("SECRET_PASS", "0000")

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
    return UserResponse(code=200, status="ok",message="Success fetch all data", result=_user)
    
@router.post('/register')
async def create(request:RequestUser,db:Session=Depends(get_db)):

    exist_user = user.get_user_by_email(db, request.parameter.user_email)
    if exist_user != None:
        return UserResponse(code=200, status="ok",message="User already exist")

    password_hashed= Encrypter.encript( request.parameter.user_password)
    
    user.create_user(db, request.parameter, password_hashed=password_hashed)
    token : str = jwt.encode({"user_name" : request.parameter.user_name}, secret_pass, algorithm= "HS256")
    return UserResponse(code=200, status="ok", message="User created successfully", result=token).dict(exclude_none=True)
    
@router.post('/login')
async def login_user(request: RequestLogin, db:Session=Depends(get_db)):
    try:
        _user = user.get_user_login(db, request.parameter.user_email, request.parameter.user_password)
    except:
         return UserResponse(
            code=404,
            status="Fail",
            message="Emial or Password is wrong"
        )

    if _user is None:
        return UserResponse(
            code=404,
            status="Fail",
            message="User not found",
            result=_user
        )
    
    token : str = jwt.encode({"user_name" : request.parameter.user_email}, secret_pass, algorithm= "HS256")
    return UserResponse(code=200, status="ok", message="Login successfully", result=token).dict(exclude_none=True)

@router.post('/update/{user_id}')
async def update_user(request: RequestUser, user_id, db:Session=Depends(get_db)):
    intId = int(user_id)

    exist_user = user.get_user_by_email(db, request.parameter.user_email)
    if exist_user != None:
        return UserResponse(code=200, status="ok",message="Another user already has that email")

    _user = user.update_user(db, request, intId)

    if _user is None:
        return UserResponse(
            code=404,
            status="Fail",
            message="User not found",
            result=_user
        )
    
    return UserResponse(code=200, status="ok", message="Update successfully")
