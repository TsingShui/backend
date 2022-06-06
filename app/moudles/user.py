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


class Settings(BaseModel):
    authjwt_secret_key: str = "4f04a9eaf0e325f6c79726365f185e180281578a449f25e743259d21a68d7a0d"


# callback to get your configuration
@AuthJWT.load_config
def get_config():
    return Settings()


# JWT


# 路由实例
router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.post('/sign_up')
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user.user_name = user.user_name.upper()
    # 用户数据表
    user_in_db = db.query(models.User.user_name).all()
    # 判断数据是否存在用户名
    if (user.user_name,) in user_in_db:
        return JSONResponse(status_code=401, content={
            'error_msg': 'user_name has existed'
        })
    
    return crud.create_user(db=db, user=user)


@router.post('/sign_in')
def login_user(user: schemas.UserLogin, db: Session = Depends(get_db), Auth: AuthJWT = Depends()):

    user_in_db = db.query(models.User).filter(models.User.user_name == user.user_name).first()
    if user_in_db.passwd != user.passwd:
        return JSONResponse(
            status_code=401,
            content={
                "login_fault": "密码或用户名错误"
            }
        )

    token = Auth.create_access_token(subject=user_in_db.id)
    return JSONResponse(
        status_code=200,
        content={
            'token':token
        }
    )

@router.post('/post')
def post(db:Session = Depends(get_db),Auth: AuthJWT= Depends()):
    Auth.jwt_required()
    db.query()
    pass
