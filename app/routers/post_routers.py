from turtle import pos
from fastapi import APIRouter, Depends, Header
from requests import Session

from app.db.config import SessionLocal
from app.db import post
from app.schemas.post_schemas import PostResponse, RequestPost
from app.schemas.user_schemas import UserResponse
from app.utils import auth
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
    try:
        _post = post.get_post(db, 0, 100)
        return PostResponse(code=200, status="ok",message="Success fetch all data", result=_post)
    except:
         return PostResponse(code=401, status="fail",message="Invalid token")

@router.get("/{post_id}")
async def get_post(db:Session=Depends(get_db)):
    try:
        _post = post.get_post_by_id(db, 1)
        return PostResponse(code=200, status='ok', message='Success fetch post', result=_post)
    finally:
        return PostResponse(code=401, status="fail",message="Invalid token")

@router.post('/update/{post_id}')
async def update_post(request: RequestPost, post_id, db:Session=Depends(get_db)):
    try:
        intId = int(post_id)

        exist_post = post.get_post_by_id(db, request.parameter.post_email)
        if exist_post != None:
            return PostResponse(code=200, status="ok",message="Another post already has that email")

        _post = post.update_post(db, request, intId)

        if _post is None:
            return PostResponse(
                code=404,

                status="Fail",
                message="post not found",
                result=_post
            )

        return PostResponse(code=200, status="ok", message="Update successfully")
    except:
         return PostResponse(code=401, status="fail",message="Invalid token")

@router.delete('/delete/{post_id}')
async def update_post(post_id, db:Session=Depends(get_db)):
    try:
        exist_post = post.get_post_by_id(db=db, post_id=post_id)
        if exist_post == None:
            return PostResponse(code=200, status="ok",message="the post does not exist")

        post.remove_post(db=db, post_id=post_id)
        return PostResponse(code=200, status="ok",message="success delete post")
    except:
         return PostResponse(code=401, status="fail",message="Invalid token")

@router.post('/create')
async def create(request:RequestPost,db:Session=Depends(get_db)):
    
    _new_post = post.create_post(db, request)
    if _new_post is None:
        return  UserResponse(code=404, status="fail", message="Post can not be create")

    return UserResponse(code=200, status="ok", message="Post was create successfully", result=_new_post).dict(exclude_none=True)