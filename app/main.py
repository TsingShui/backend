# app 导入
from fastapi import FastAPI
# 注册数据库导入
from models import Base
from db.database import engine

# 导入模块路由
from moudles import user
from moudles import playground
# 跨域
from fastapi.middleware.cors import CORSMiddleware

# 主程序
Base.metadata.create_all(bind=engine)
app = FastAPI()

# 跨域设置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_credentials=False,
    allow_headers=["*"],

)

# 包含路由
app.include_router(user.router)
app.include_router(playground.router)
