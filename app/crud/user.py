"""
用户相关的 CRUD
"""
from sqlalchemy.orm import Session
import models
import schemas

def create_user(db:Session,user:schemas.UserCreate):
    """
    创建用户
    """
    db_user = models.User(email=user.email,passwd = user.passwd)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
