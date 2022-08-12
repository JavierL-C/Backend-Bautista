from typing import Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel
from sqlalchemy import false

T = TypeVar("T")

class CommentSchema(BaseModel):
    comment_content:Optional[str]=None
    comment_is_approved:Optional[bool]=False
    comment_author:Optional[str]=None
    comment_post_id:Optional[int]=Field(default=None, foreign_key="posts.post_id")

    class Config:
        orm_mode=True

class RequestComment(BaseModel):
    parameter:CommentSchema=Field(...)

class CommentResponse(GenericModel, Generic[T]):
    code:str
    status:str
    message:str
    result:Optional[T]