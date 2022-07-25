from cgi import print_form
import string
from time import timezone
from xmlrpc.client import DateTime
from psycopg2 import Date
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.config import Base

class Roles(Base):
    __tablename__ = "roles"

    roles_id=Column(Integer, primary_key=True)
    roles_name=Column(String)

    user= relationship("User", back_populates="rol")


class User(Base): 
    __tablename__ = "users"

    user_id=Column(Integer, primary_key=True)
    user_name=Column(String)
    user_password=Column(String)
    user_email=Column(String)
    user_id_rol=Column(Integer, ForeignKey("roles.roles_id"))
    user_status=Column(String)
    user_creation_date=Column(DateTime)
    user_update_date=Column(DateTime)

    rol= relationship("Roles", back_populates="user")
#    post = relationship("Posts", backref="user")

#class Posts(Base):
#    __tablename__= "posts"
#
#    post_id=Column(Integer, primary_key=True)
#    post_content=Column(String)
#    post_status=Column(String)
#    post_create_date=Column(DateTime)
#    post_update_date=Column(DateTime)
#    post_user_id=Column(Integer, ForeignKey("users.user_id"))
#    post_image=Column(String)
#
#    user = relationship("User", back_populates="post")