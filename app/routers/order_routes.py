from fastapi import APIRouter, Depends

from typing import Annotated

from fastapi.security import OAuth2PasswordBearer
from app.core.security import oauth2_scheme


# fastapi_jwt_auth must be installed

# tags ist for documentation title
router = APIRouter(prefix="/order", tags=["Orders"])


@router.get("/")
async def hello(token: str):
    return {"message": "Hello world------"}


@router.get("/security/")
async def read_items(token: str):
    return {"token": token}


@router.post("/")
async def create_order():
    return ""


@router.get("/user/order/{id}/")
async def get_specific_order(
    id: int, authorize: Annotated[OAuth2PasswordBearer, Depends(oauth2_scheme)]
):
    pass
