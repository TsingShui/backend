# 导入 ORM 库字段
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
# 导入基类
from db.database import Base

"""

此处为 数据库模型,对应数据库的表、字段

"""


class User(Base):
    __tablename__ = 'users'
    # 用户账号属性
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, unique=True, index=True)
    passwd = Column(String)

    # 用户个人信息
    gender = Column(String)
    join_time = Column(Integer)
    profile = Column(String)
    links = Column(String)  # 用户 Github Links

    # 用户连接文章
    papers = relationship("Paper", back_populates="author")


class Paper(Base):
    __tablename__ = 'papers'
    # UID
    id = Column(Integer, primary_key=True, index=True)
    # 内容
    title = Column(String(50))
    text = Column(String)
    pub_time = Column(Integer)
    tag = Column(String)
    # author
    author_id = Column(Integer, ForeignKey('users.id'))
    author = relationship('User', back_populates='papers')
