from datetime import date, datetime
from optparse import Option
from typing import Optional, Generic, TypeVar, Union
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel
from app.schemas.comment_schemas import CommentSchema, RequestComment
from sqlalchemy import false

T = TypeVar("T")

class PostSchema(BaseModel):
    post_content: Optional[str]=None
    post_title: Optional[str]=None
    post_is_approved: Optional[bool]=False
    post_user_id: Optional[int]=Field(default=None, foreign_key="users.user_id")
    post_image: Optional[str]=None

    class Config:
        orm_mode = True

class PostCommentSchema(BaseModel):
    post_content: Optional[str]=None
    post_title: Optional[str]=None
    post_is_approved: Optional[bool]=False
    post_user_id: Optional[int]=Field(default=None, foreign_key="users.user_id")
    post_create_date: Optional[date]=None
    post_update_date: Optional[date]=None
    post_image: Optional[str]=None
    post_comments: Union[list, None]=None

class RequestPost(BaseModel):
    parameter: PostSchema = Field(...)

class RequestPostComment(BaseModel):
    parameter: PostCommentSchema = Field(...)

class PostResponse(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]