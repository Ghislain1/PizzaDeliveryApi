from fastapi import APIRouter, Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from fastapi.exceptions import HTTPException

# Own import
from backend.core.dependencies import CustomerServiceDep
from backend.core.security import oauth2_scheme

from backend.schemas.customer_schema import CustomerCreate

# Router definition for Authentication
router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    username = form_data.username
    return {"access_token": username, "token_type": "bearer"}


# To Register a customer
@router.post("/signup")
async def signup(customer_create: CustomerCreate, customer_service: CustomerServiceDep):

    customer_service.create_customer2(customer_create)
