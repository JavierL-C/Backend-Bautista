from sqlalchemy.orm import Session
from datetime import datetime
from app.models.user import Image

def create_Image(db:Session, post_id:int, image:bytes):
    _image = Image(
        image=image,
        image_post_id=post_id
    )
    db.add(_image)
    db.commit()
    db.refresh(_image)
    return _image  

def get_image(db:Session, post_id:int):
    return db.query(Image).filter(Image.image_post_id == post_id).first()

def update_image(db:Session, post_id:int, image:bytes):
    _image = get_image(db, post_id)
    _image.image = image

    db.commit()
    db.refresh(_image)

def delete_image(db:Session, post_id:int):
    _image = get_image(db, post_id)
    db.delete(_image)
    db.commit()
