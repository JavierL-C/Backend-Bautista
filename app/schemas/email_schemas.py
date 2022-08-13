from optparse import Option
from typing import Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel
from sqlalchemy import false

T = TypeVar("T")


class EmailSchema(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    content: Optional[str] = None

    class Config:
        orm_mode = True


class RequestEmail(BaseModel):
    parameter: EmailSchema = Field(...)


class EmailResponse(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
