from contextlib import asynccontextmanager

from fastapi import FastAPI


# Pizza
from app.db import create_db_and_tables, seed_db_if_empty
from app.routers.auth_routes import router as auth_router
from app.routers.order_routes import router as order_router
from app.routers.customer_routes import router as customer_router
from app.core.middlewares import CustomMiddleware
from app.services.printer_service import PrinterService

printer_service = PrinterService()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    printer_service.print_debug("Create DB AND TABLES")
    await seed_db_if_empty()
    yield


app = FastAPI(lifespan=lifespan, title="PizzaDeliveryApp")

# Add Middlewares
app.add_middleware(CustomMiddleware)

# Include router from different API
app.include_router(auth_router)
app.include_router(order_router)
app.include_router(customer_router)


@app.get("/")
def root():
    return {"Hello welcome to my first FastAPI real world Project called Delivery API"}
