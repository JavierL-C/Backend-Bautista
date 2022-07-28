from datetime import datetime
from optparse import Option
from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar("T")

class RolesSchema(BaseModel):
    roles_id: Optional[int]=None
    roles_name: Optional[str]=None

    class Config:
        orm_mode = True

class UserSchema(BaseModel):
    user_name: Optional[str]=None
    user_email: Optional[str]=None
    user_password: Optional[str]=None
    user_id_rol: Optional[int]= Field(default=None, foreign_key="roles.roles_id")
    user_status: Optional[str]=None

    class Config:
        orm_mode = True

class RequestUser(BaseModel):
    parameter: UserSchema = Field(...)

class UserResponse(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
    
class LoginModel(BaseModel):
    user_email : Optional[str]=None
    user_password: Optional[str]=None
    pass

class RequestLogin(BaseModel):
    parameter: LoginModel = Field(...)