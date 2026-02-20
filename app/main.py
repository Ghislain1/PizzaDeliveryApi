from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.routers.auth_routes import router as auth_router
from app.routers.order_routes import router as order_router
from app.db.database import create_db_and_tables
from app.db.init_db import seed_db_if_empty


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    await seed_db_if_empty()
    yield


app = FastAPI(lifespan=lifespan)

"""
@AuthJWT.load_config
def get_config():
    return Settings()
"""

# Include router from different API
app.include_router(auth_router)
app.include_router(order_router)
