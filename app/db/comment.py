from datetime import datetime
from sqlalchemy.orm import Session
from app.models.user import Comment
from app.schemas.comment_schemas import RequestComment, CommentSchema
from app.db import post

def create_comment(db:Session, comment:RequestComment):
    _post = post.get_post_by_id(db,comment.parameter.comment_post_id)
    _comment = Comment(
        comment_content=comment.parameter.comment_content,
        comment_is_approved=comment.parameter.comment_is_approved,
        comment_author=comment.parameter.comment_author,
        comment_create_date=datetime.now(),
        comment_post_id=comment.parameter.comment_post_id,
        comment_post_title=_post.__dict__['post_title']
    )
    db.add(_comment)
    db.commit()
    db.refresh(_comment)
    return _comment

def get_comment(db:Session, skip:int=0, limit:int=1):
    return db.query(Comment).offset(skip).limit(limit).all()

def get_comment_by_id(db:Session, comment_id:int):
    return db.query(Comment).filter(Comment.comment_id==comment_id).first()

def get_comment_by_post(db:Session, post_id:int):
    return db.query(Comment).filter(Comment.comment_post_id==post_id).all()

def get_comment_by_post_and_comment(db:Session, post_id:int, is_approved:bool):
    return db.query(Comment).filter(Comment.comment_post_id==post_id).filter(Comment.comment_is_approved==is_approved).all()

def get_comment_left_to_approve(db:Session):
    return db.query(Comment).filter(Comment.comment_is_approved==False).all()

def update_comment(db:Session, comment:RequestComment, comment_id:int):
    _comment=get_comment_by_id(db=db, comment_id=comment_id)
    _comment.comment_content=comment.parameter.comment_content
    _comment.comment_is_approved=comment.parameter.comment_is_approved
    _comment.comment_author=comment.parameter.comment_author
    db.commit()
    db.refresh(_comment)
    return _comment

def remove_comment(db:Session, comment_id:int):
    _comment=get_comment_by_id(db=db, comment_id=comment_id)
    db.delete(_comment)
    db.commit()
