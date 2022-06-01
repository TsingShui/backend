"""

此处为 CRUD 的模型,对应的为 FastApi 处理的 Json 请求

"""



from pydantic import BaseModel
class UserBase(BaseModel):
    email :str
    class Config:
        orm_mode = True

class UserCreate(UserBase):
    passwd : str
    class Config:
        orm_mode = True

class User(UserBase):
    id :int
    class Config:
        orm_mod = True