from fastapi import APIRouter


router = APIRouter()


@router.get('/')
async def start():
    return "Hello, world!"

