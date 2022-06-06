"""

此处为 CRUD 的模型,对应的为 FastApi 处理的 Json 请求

"""

from calendar import c
from pydantic import BaseModel
from typing import List


class UserBase(BaseModel):
    user_name: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    passwd: str
    gender: str = None
    profile: List[str] = None
    links: str = None

    class Config:
        orm_mode = True


class UserLogin(UserBase):
    passwd: str

    class Config:
        orm_mode = True


class UserToken(UserBase):
    token: str

    class Config:
        orm_mode = True


class User(UserBase):
    id: int

    class Config:
        orm_mod = True


class PaperCreate(BaseModel):
    #   基础内容
    title: str
    text: str
    tag: List[str]

    class Config:
        orm_model = True


class Paper(PaperCreate):
    author_id: int

    class Config:
        orm_model = True
