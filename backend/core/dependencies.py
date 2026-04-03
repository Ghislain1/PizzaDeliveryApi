# Singleton using @lru_cache
from functools import lru_cache
from typing import Annotated
from fastapi import Depends
from backend.db.database import get_async_session
from backend.services.customer_service import CustomerService
from backend.services.order_service import OrderService
from backend.services.printer_service import PrinterService
from sqlalchemy.ext.asyncio import AsyncSession


@lru_cache
def get_order_service(session: Annotated[AsyncSession, Depends(get_async_session)]):
    return OrderService(session=session)


@lru_cache
def get_printer_service():
    return PrinterService()


@lru_cache
def get_customer_service(session: Annotated[AsyncSession, Depends(get_async_session)]):
    return CustomerService(session)


# AsyncSessionDep = Annotated[AsyncSession, Depends(get_async_session)]
CustomerServiceDep = Annotated[CustomerService, Depends(get_customer_service)]
OrderServiceDep = Annotated[OrderService, Depends(get_order_service)]
PrinterDep = Annotated[PrinterService, Depends(get_printer_service)]
