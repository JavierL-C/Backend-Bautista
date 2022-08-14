from xmlrpc.client import DateTime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.dialects.postgresql import ARRAY, BYTEA

from app.db.config import Base

class Role(Base):
    __tablename__ = "roles"

    role_id=Column(Integer, primary_key=True)
    role_name=Column(String)

    # user = relationship("User", back_populates="rol")


class User(Base): 
    __tablename__ = "users"

    user_id=Column(Integer, primary_key=True)
    user_name=Column(String)
    user_email=Column(String)
    user_password=Column(String)
    user_id_rol=Column(Integer, ForeignKey("roles.role_id"))
    user_status=Column(String)
    user_creation_date=Column(DateTime)
    user_update_date=Column(DateTime)

    # rol = relationship("Role", back_populates="user")
    # post = relationship("Post", backref="user")

class Post(Base):
   __tablename__= "posts"

   post_id=Column(Integer, primary_key=True)
   post_title=Column(String)
   post_content=Column(String)
   post_is_approved=Column(Boolean)
   post_create_date=Column(DateTime)
   post_update_date=Column(DateTime)
   post_user_id=Column(Integer, ForeignKey("users.user_id"))
   post_image=Column(ARRAY(BYTEA))

#    user = relationship("User", back_populates="post")

class Comment(Base):
    __tablename__ = "comments"

    comment_id=Column(Integer, primary_key=True)
    comment_content=Column(String)
    comment_create_date=Column(DateTime)
    comment_author=Column(String)
    comment_post_id=Column(Integer, ForeignKey("posts.post_id"))
    comment_is_approved=Column(Boolean)
