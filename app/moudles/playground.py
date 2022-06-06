# 导入路由
from fastapi import APIRouter
# 导入Depends
from fastapi import Depends
from dependecy import get_db
# 导入 FastApi 请求模型
import schemas
from pydantic import BaseModel
# 导入 Session
from sqlalchemy.orm import Session
# 导入 ORM models
import models  # 你应该先对数据库进行检查！
# 导入 jwt
from fastapi_jwt_auth import AuthJWT
# 导入响应
from fastapi.exceptions import HTTPException
# 导入 Crud
import crud
# 导入 JsonResponse
from fastapi.responses import JSONResponse


router = APIRouter(
    prefix='/playground',
    tags = ['playground']
)


# 获取所有文章

# @router.get('/papers')
# async def get_papers(db:Session=Depends(get_db)):
#     """
#     返回排序过的所有文章
#     """

