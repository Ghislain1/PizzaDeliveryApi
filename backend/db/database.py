from typing import AsyncGenerator

from passlib.context import CryptContext
from sqlmodel import SQLModel, select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from backend.models.customer import Customer


# POSTGRES_URL = "postgresql://postgres:namej345@localhost/pizza_deliver_db"
DATABASE_URL = "sqlite+aiosqlite:///./pizza_deliver.db"  # U must install aiosqlite


# 1. ---------------------------------------------------------- Classes --------------------------------------
class Base(SQLModel):
    pass


# 2. -------------------------------------------------------- Engine and Session  ------------------------------------
engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


# 3. ------------------------------ Methods ------------------------------------------
async def create_db_and_tables():
    async with engine.begin() as connection:
        await connection.run_sync(SQLModel.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def check_db_empty():

    async with async_session_maker() as session:
        result = await session.execute(select(Customer))
        customers = result.scalars().all()
        return len(customers) == 0


async def generate_dummy_data():

    pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

    dummy_customers = [
        {
            "username": "john_doe",
            "email": "john.doe@example.com",
            "password": "password123",
        },
        {
            "username": "jane_smith",
            "email": "jane.smith@example.com",
            "password": "password123",
        },
        {
            "username": "mike_johnson",
            "email": "mike.johnson@example.com",
            "password": "password123",
        },
        {
            "username": "sarah_wilson",
            "email": "sarah.wilson@example.com",
            "password": "password123",
        },
        {
            "username": "david_brown",
            "email": "david.brown@example.com",
            "password": "password123",
        },
        {
            "username": "lisa_davis",
            "email": "lisa.davis@example.com",
            "password": "password123",
        },
        {
            "username": "chris_miller",
            "email": "chris.miller@example.com",
            "password": "password123",
        },
        {
            "username": "amy_taylor",
            "email": "amy.taylor@example.com",
            "password": "password123",
        },
    ]

    async with async_session_maker() as session:
        for customer_data in dummy_customers:
            hashed_password = pwd_context.hash(customer_data["password"])
            customer = Customer(
                username=customer_data["username"],
                email=customer_data["email"],
                hashed_password=hashed_password,
                is_active=True,
            )
            session.add(customer)
        await session.commit()
