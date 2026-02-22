from contextlib import asynccontextmanager

from fastapi import FastAPI

from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from app.db import create_db_and_tables, seed_db_if_empty
from app.routers.auth_routes import router as auth_router
from app.routers.order_routes import router as order_router
from app.routers.customer_routes import router as customer_router
from app.core.middlewares import CustomMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
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
