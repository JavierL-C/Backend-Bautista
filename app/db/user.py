from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schemas import UserSchema

def get_user(db:Session, skip:int=0, limit:int=1):
    return db.query(User).offset(skip).limit(limit).all()