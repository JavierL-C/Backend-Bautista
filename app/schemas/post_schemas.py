from datetime import date
from typing import Optional, Generic, TypeVar, Union
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar("T")

class PostSchema(BaseModel):
    post_content: Optional[str]=None
    post_title: Optional[str]=None
    post_is_approved: Optional[bool]=False
    post_user_id: Optional[int]=Field(default=None, foreign_key="users.user_id")
    post_content_html: Optional[str]=None

    class Config:
        orm_mode = True

    @classmethod
    def as_form(cls, post_content:str, post_title:str, post_is_approved:bool, post_user_id:int, post_content_html:str) -> 'PostSchema':
        return cls(
            post_content=post_content,
            post_title=post_title,
            post_is_approved=post_is_approved,
            post_user_id=post_user_id,
            post_content_html=post_content_html
        )

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