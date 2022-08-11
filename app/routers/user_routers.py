from fastapi import APIRouter, Header, Depends
from sqlalchemy.orm import Session

from app.db.config import SessionLocal
from app.schemas.user_schemas import RequestUser, UserResponse, RequestLogin
from app.db import user
from app.utils.auth import Encrypter
from app.utils import auth

router = APIRouter()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()
    
@router.get("/")
async def get(db:Session=Depends(get_db), Authorization:str=Header(None)):
    try:
        token = Authorization.split(" ")[1]
        isValid = auth.validate_token(token, True)
        if isValid == "Invalid token":
            return UserResponse(
                code=401,
                status="fail",
                message="Invalid token"
            )

        _users = user.get_user(db, 0, 100)
        return UserResponse(
            code=200,
            status="ok",
            message="Success fetch all data",
            result=_users
        )
    except:
        return UserResponse(
            code=401,
            status="fail",
            message="Invalid token"
        )

@router.get("/current")
async def get_current_user(db:Session=Depends(get_db), Authorization:str=Header(None)):
    try:
        token = Authorization.split(" ")[1]
        isValid = auth.validate_token(token, True)
        if isValid == "Invalid token":
            return UserResponse(
                code=401,
                status="fail",
                message="Invalid token"
            )
        
        _user = user.get_user_by_email(db, isValid)
        _user.__dict__['user_password'] = ""
        return UserResponse(
            code=200,
            status="ok",
            message="Success fetch current user",
            result=_user
        )
    except:
        return UserResponse(
            code=401,
            status="fail",
            message="Invalid token"
        )

@router.post('/register')
async def create(request:RequestUser, db:Session=Depends(get_db)):

    exist_user = user.get_user_by_email(db, request.parameter.user_email)
    if exist_user != None:
        return UserResponse(
            code=200,
            status="ok",
            message="User already exist"
        )

    password_hashed= Encrypter.encript(request.parameter.user_password)
    
    user.create_user(db, request.parameter, password_hashed=password_hashed)
    token: str = auth.generate_jwt({"user_name": request.parameter.user_name})
    return UserResponse(
        code=200,
        status="ok",
        message="User created successfully",
        result=token
    ).dict(exclude_none=True)
    
@router.post('/login')
async def login_user(request:RequestLogin, db:Session=Depends(get_db)):
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
    
    token: str = auth.generate_jwt({"user_name": request.parameter.user_email})
    return UserResponse(
        code=200,
        status="ok",
        message="Login successfully",
        result=token
    ).dict(exclude_none=True)

@router.post('/update/{user_id}')
async def update_user(request:RequestUser, user_id, db:Session=Depends(get_db), Authorization:str=Header(None)):
    try:
        token = Authorization.split(" ")[1]
        isValid = auth.validate_token(token, True)
        if isValid == "Invalid token":
            return UserResponse(
                code=401,
                status="fail",
                message="Invalid token"
            )

        intId = int(user_id)

        exist_user = user.get_user_by_email(db, request.parameter.user_email)
        if exist_user != None:
            return UserResponse(
                code=200,
                status="ok",
                message="Another user already has that email"
            )

        _user = user.update_user(db, request, intId)

        if _user is None:
            return UserResponse(
                code=404,
                status="Fail",
                message="User not found",
                result=_user
            )
        
        return UserResponse(
            code=200,
            status="ok",
            message="Update successfully"
        )
    except:
        return UserResponse(
            code=401,
            status="fail",
            message="Invalid token"
        )
    

@router.delete('/delete/{user_id}')
async def update_user(user_id, db:Session=Depends(get_db), Authorization:str=Header(None)):
    try:
        token = Authorization.split(" ")[1]
        isValid = auth.validate_token(token=token, output=True)
        if isValid == "Invalid token":
            return UserResponse(
                code=401,
                status="fail",
                message="Invalid token"
            )

        intId = int(user_id)
        exist_user = user.get_user_by_id(db, intId)
        if exist_user == None:
            return UserResponse(
                code=200,
                status="ok",
                message="the user does not exist"
            )

        user.remove_user(db, intId)
        return UserResponse(
            code=200,
            status="ok",
            message="success delete user"
        )
    except:
        return UserResponse(
            code=401,
            status="fail",
            message="Invalid token"
        )
