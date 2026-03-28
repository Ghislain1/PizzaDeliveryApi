# Singleton using @lru_cache
from functools import lru_cache
from typing import Annotated
from fastapi import Depends
from backend.db.database import get_async_session
from backend.services.customer_service import CustomerService
from backend.services.printer_service import PrinterService
from sqlalchemy.ext.asyncio import AsyncSession


@lru_cache
def get_printer_service():
    return PrinterService()


PrinterDep = Annotated[PrinterService, Depends(get_printer_service)]

AsyncSessionDep = Annotated[AsyncSession, Depends(get_async_session)]


@lru_cache
def get_customer_service(session: AsyncSessionDep):
    return CustomerService(session)


CustomerServiceDep = Annotated[CustomerService, Depends(get_customer_service)]
