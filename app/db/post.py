from sqlalchemy.orm import Session
from datetime import datetime
from app.models.user import Post
from app.schemas.post_schemas import RequestPost

def get_post(db:Session, skip:int=0, limit:int=1):
    return db.query(Post).offset(skip).limit(limit).all()

def create_post(db:Session, post:Post):
    _post = Post(
        post_content = post.post_content,
        post_is_approved = post.post_is_approved,
        post_create_date = post.post_create_date,
        post_update_date = post.post_update_date,
        post_user_id = datetime.now(),
        post_image = datetime.now(),
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
    _post.post_is_approved = post.parameter.post_is_approved
    _post.post_user_id = post.parameter.post_user_id
    _post.post_image = post.parameter.post_image
    db.commit()
    db.refresh(_post)
    return _post

def remove_post(db:Session, post_id:int):
    _post = get_post_by_id(db=db, post_id=post_id)
    db.delete(_post)
    db.commit()