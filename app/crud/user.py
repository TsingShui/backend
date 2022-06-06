"""
用户相关的 CRUD
"""
from sqlalchemy.orm import Session
import models
import schemas


def create_user(db: Session, user: schemas.UserCreate):
    """
    创建用户
    """

    db_user = models.User(
        user_name=user.user_name,
        passwd=user.passwd,
        gender=user.gender ,
        profile=user.profile ,
        links=user.links ,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
