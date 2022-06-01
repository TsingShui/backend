# app 导入
from fastapi import FastAPI
# 注册数据库导入
from models import Base
from db.database import engine

# 导入模块路由
from moudles import user

# 主程序
Base.metadata.create_all(bind=engine)
app = FastAPI()

# 包含路由
app.include_router(user.router)