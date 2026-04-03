# https://fastapi.tiangolo.com/tutorial/sql-databases/#create-a-hero
# - table model vs. data model
# table true :D

# - Create a Customer


from typing import Annotated

from fastapi import APIRouter, Query

from backend.schemas.customer_schema import CustomerPublic
from backend.core.dependencies import CustomerServiceDep, PrinterDep

router = APIRouter(prefix="/customers", tags=["Customers"])


# ---------------------------------------------- End points --------------------------------------------


# https://fastapi.tiangolo.com/tutorial/sql-databases/#read-heroes-with-heropublic
@router.get("/", response_model=list[CustomerPublic])
async def read_customers(
    customer_service: CustomerServiceDep,
    printer: PrinterDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    customers = customer_service.load_customers(offset, limit)
    printer.print_debug("=========================== read_customers ===============")
    return customers
