from tkinter import SE
from sqlalchemy.orm import Session
from datetime import datetime
from app.models.user import User
from app.schemas.user_schemas import RequestUser, UserSchema
from app.utils.auth import Encrypter

def get_user(db:Session, skip:int=0, limit:int=1):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db:Session, user: UserSchema, password_hashed: str):
    _user = User(user_name= user.user_name,
                user_email=user.user_email,
                user_password=password_hashed,
                user_id_rol=user.user_id_rol,
                user_status="active",
                user_creation_date=datetime.now(),
                user_update_date=datetime.now())
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user

def get_user_by_id(db:Session, user_id: int):
    return db.query(User).filter(User.user_id == user_id).first()

def get_user_by_email(db:Session, user_email: str):
    return db.query(User).filter(User.user_email == user_email).first()

def get_user_login(db:Session, user_email: str, user_password: str):
    user =  db.query(User).filter(User.user_email == user_email).first()
    if Encrypter.verify(user_password, user.__dict__["user_password"]):
        return user

def update_user(db:Session, user: RequestUser, user_id: int):
    _user = get_user_by_id(db=db,user_id=user_id)
    _user.user_name = user.parameter.user_name
    _user.user_email = user.parameter.user_email
    _user.user_id_rol = user.parameter.user_id_rol
    _user.user_status = user.parameter.user_status
    db.commit()
    db.refresh(_user)
    return _user
