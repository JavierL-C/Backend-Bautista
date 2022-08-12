from pickle import FALSE
from sqlalchemy.orm import Session
from datetime import datetime
from app.models.user import Post
from app.schemas.post_schemas import RequestPost
import base64

def get_post(db:Session, skip:int=0, limit:int=1):
    return db.query(Post).offset(skip).limit(limit).all()

def create_post(db:Session, post:RequestPost):
    _post = Post(
        post_content = post.parameter.post_content,
        post_is_approved = False,
        post_title = post.parameter.post_title,
        post_create_date = datetime.now(),
        post_update_date = datetime.now(),
        post_user_id = post.parameter.post_user_id,
        post_image = base64.b64encode(post.parameter.post_image)
    )
    db.add(_post)
    db.commit()
    db.refresh(_post)
    return _post


def get_post_by_id(db:Session, post_id:int):
    return db.query(Post).filter(Post.post_id == post_id).first()

def update_post(db:Session, post:RequestPost, post_id:int):
    _post = get_post_by_id(db=db, post_id=post_id)
    _post.post_content = post.parameter.post_content
    _post.post_title = post.parameter.post_title,
    _post.post_is_approved = post.parameter.post_is_approved
    _post.post_user_id = post.parameter.post_user_id
    _post.post_image = base64.b64encode(post.parameter.post_image)
    _post.post_update_date = datetime.now()
    db.commit()
    db.refresh(_post)
    return _post

def remove_post(db:Session, post_id:int):
    _post = get_post_by_id(db=db, post_id=post_id)
    db.delete(_post)
    db.commit()