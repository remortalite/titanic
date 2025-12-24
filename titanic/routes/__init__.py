from fastapi import APIRouter
from sqlalchemy.orm import Session

from titanic.dto import engine


router = APIRouter()


@router.get('/')
async def start():
    with Session(engine) as session:
        session.commit()
    return "Hello, world!"

