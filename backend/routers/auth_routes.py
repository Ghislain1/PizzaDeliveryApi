from fastapi import APIRouter, Depends

from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

# Own import
from backend.core.dependencies import CustomerServiceDep

from backend.schemas.customer_schema import CustomerCreate, CustomerRead

# Router definition for Authentication
router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/token")
async def login_customer(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    customer_service: CustomerServiceDep,
):
    username = form_data.username
    password = form_data.password

    return await customer_service.token(username, password=password)


# To Register a customer
@router.post("/signup", response_model=CustomerRead)
async def register_customer(
    customer_create: CustomerCreate, customer_service: CustomerServiceDep
):

    return await customer_service.create_customer(customer_create)
