# 导入路由
from fastapi import APIRouter
# 导入Depends
from fastapi import Depends
from dependecy import get_db
# 导入 FastApi 请求模型
import schemas
# 导入 Session
from sqlalchemy.orm import Session

# 导入 ORM models
import models # 你应该先对数据库进行检查！

# 导入 Crud
import crud

# 路由实例
router = APIRouter(
    prefix='/user',
    tags=['user']
)



#
@router.post('',response_model=schemas.User)
def create_user(user:schemas.UserCreate,db:Session = Depends(get_db)):
    return crud.create_user(db=db,user=user)