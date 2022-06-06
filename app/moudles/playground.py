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
from typing import List

router = APIRouter(
    prefix='/playground',
    tags=['playground']
)


# 获取所有文章

class PlayGroundAuthor(BaseModel):
    id: int | None
    name: str | None
    avatar: str | None

    class Config:
        orm_model = True


class PlayGroundPaper(BaseModel):
    id: int | None
    author: PlayGroundAuthor | None
    title: str | None
    content: str | None
    date: str | None
    tags: List[str] | None

    class Config:
        orm_model = True


@router.get('/papers')
def get_papers(db: Session = Depends(get_db)):
    import random
    """
    返回随机排序的文章
    """
    paper_list: List[models.Paper] = db.query(models.Paper).all()
    new_paper_list = []
    for paper in paper_list:
        play_ground_paper = PlayGroundPaper()
        play_ground_paper.author = PlayGroundAuthor()
        play_ground_paper.id = paper.id
        play_ground_paper.date = paper.pub_time
        play_ground_paper.title = paper.title
        play_ground_paper.content = paper.text
        play_ground_paper.tags = [i.tag for i in paper.tags]
        play_ground_paper.author.id = paper.author.id
        play_ground_paper.author.name = paper.author.user_name
        play_ground_paper.author.avatar = 'https://s3.bmp.ovh/imgs/2022/03/5524b1bf3e53ec04.jpg'
        new_paper_list.append(play_ground_paper)
    random.shuffle(new_paper_list)
    return new_paper_list
# https://s3.bmp.ovh/imgs/2022/03/5524b1bf3e53ec04.jpg