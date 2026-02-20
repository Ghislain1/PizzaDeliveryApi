from fastapi import APIRouter, Depends

# from app.db.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db import get_session

from app.models.user import User


router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.get("/")
async def read_users(session: AsyncSession = Depends(get_session)):

    result = await session.execute(select(User))

    users = [row for row in result.scalars().all()]

    return {"posts": users}


""" 
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder

auth_router = APIRouter(prefix="/auth")
session = Session(bind=engine)


@auth_router.get("/")
async def hello():
    return {"message": "Hello world"}


@auth_router.post("/signup")
async def signup(user: SignUpModel, status_code=status.HTTP_201_CREATED):
    db_email = session.query(User).filter(User.email == user.email).first()

    if db_email is not None:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="user with the email already exists",
        )
    db_username = session.query(User).filter(User.username == user.username).first()

    if db_username is not None:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="user with the name already exists",
        )
    # new_user = User(**user)
    new_user = User(
        username=user.username,
        email=user.email,
        password=generate_password_hash(user.password),
        is_active=user.is_active,
        is_staff=user.is_staff,
    )

    session.add(new_user)
    session.commit()
    return new_user


@auth_router.post("/login")
async def login(user: LoginModel, Authorize: AuthJWT = Depends()):
    db_user = session.query(User).filter(User.username == user.username).first()
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid username",
        )
    password_ok = check_password_hash(db_user.password, user.password)
    if not password_ok:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid Passwords",
        )
    # Everthing is ok...
    access_token = Authorize.create_access_token(subject=db_user.username)
    refresh_token = Authorize.create_refresh_token(subject=db_user.username)

    response = {"access": access_token, "refresh": refresh_token}
    return jsonable_encoder(response)
"""
