"""
数据库模板内容基本不用动
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# 数据库位置
SQLALCHEMY_DATABASE_URL = "sqlite:///./data.db"
# 连接数据库
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# 会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base Model
Base = declarative_base()