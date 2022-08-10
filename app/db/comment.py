from datetime import datetime
from sqlalchemy.orm import Session
from app.models.user import Comment
from app.schemas.comment_schemas import RequestComment, CommentSchema

# def create_comment(db:Session, comment:CommentSchema):
#     _comment = Comment(
#         comment_content=comment.comment_content,
#         comment_is_approved=comment.comment_is_approved,
#         comment_author=comment.comment_author,
#         comment_creation_date=datetime.now(),
#         comment_post_id=comment.comment_post_id
#     )
#     db.add(_comment)
#     db.commit()
#     db.refresh(_comment)
#     return _comment

def get_comment(db:Session, skip:int=0, limit:int=1):
    return db.query(Comment).offset(skip).limit(limit).all()

# def get_comment_by_id(db:Session, comment_id:int):
#     return db.query(Comment).filter(Comment.comment_id==comment_id).first()

# def get_comment_by_post(db:Session, post_id:int):
#     return db.query(Comment).filter(Comment.comment_post_id==post_id).all()

# def update_comment(db:Session, comment:RequestComment, comment_id:int):
#     _comment=get_comment_by_id(db=db, comment_id=comment_id)
#     _comment.comment_content=comment.parameter.comment_content
#     _comment.comment_is_approved=comment.parameter.comment_is_approved
#     _comment.comment_author=comment.parameter.comment_author
#     db.commit()
#     db.refresh(_comment)
#     return _comment

# def remove_comment(db:Session, comment_id:int):
#     _comment=get_comment_by_id(db=db, comment_id=comment_id)
#     db.delete(_comment)
#     db.commit()
