from fastapi import APIRouter, Header, Depends
from sqlalchemy.orm import Session
from app.db.config import SessionLocal
from app.db import comment
from app.schemas.comment_schemas import CommentResponse, RequestComment

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
        _comments = comment.get_comment(db, 0, 100)
        return CommentResponse(code=200, status="ok", message="Success fetch data", result=_comments)
    except:
        return CommentResponse(code=401, status="fail",message="Invalid token")

# @router.get("/{post_id}")
# async def get_comment(post_id, db:Session=Depends(get_db)):
#     try:
#         intId = int(post_id)
#         _comment = comment.get_comment_by_post(db, intId)
#         return CommentResponse(code=200, status='ok', message='Success fetch comment', result=_comment)
#     finally:
#         return CommentResponse(code=401, status="fail",message="Invalid token")

# @router.post("/update/{comment_id}")
# async def update_comment(request:CommentResponse, comment_id, db:Session=Depends(get_db)):
#     try:
#         intId = int(comment_id)
#         exist_comment = comment.get_comment_by_id(db, intId)
#         if exist_comment != None:
#             return CommentResponse(code=200, status="ok",message="Another post already has that email")

#         _comment = comment.update_comment(db, request, intId)

#         if _comment is None:
#             return CommentResponse(
#                 code=404,
#                 status='Fail',
#                 message='Comment not found',
#                 result=_comment
#             )
#     except:
#         return CommentResponse(code=401, status="fail",message="Invalid token")

# @router.delete("/delete/{comment_id}")
# async def update_comment(comment_id, db:Session=Depends(get_db)):
#     try:
#         exist_comment = comment.get_comment_by_id(db, comment_id)
#         if exist_comment == None:
#             return CommentResponse(code=200, status="ok",message="the post does not exist")

#         comment.remove_comment(db, comment_id)
#         return CommentResponse(code=200, status="ok",message="success delete post")
#     except:
#         return CommentResponse(code=401, status="fail",message="Invalid token")

# @router.post("/create")
# async def create(request:RequestComment, db:Session=Depends(get_db)):
#     _new_comment = comment.create_comment(db, request)
#     if _new_comment is None:
#         return  CommentResponse(code=404, status="fail", message="Post can not be create")

#     return CommentResponse(code=200, status="ok", message="Post was create successfully", result=_new_comment).dict(exclude_none=True)
