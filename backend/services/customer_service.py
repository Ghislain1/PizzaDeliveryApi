#  passlib[bcrypt] must be installed
from passlib.context import CryptContext
from sqlmodel import select
from fastapi.exceptions import HTTPException
from starlette import status

from backend.models.customer import Customer
from sqlalchemy.ext.asyncio import AsyncSession

from backend.schemas.customer_schema import CustomerCreate


class CustomerService:
    def __init__(self, session: AsyncSession):
        # Argon2 (no length limit, more modern)
        self.pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
        self.session = session

    async def create_customer(self, customer_create: CustomerCreate) -> Customer:
        """Create a new customer with hashed password"""
        # Hash the plain password
        hashed_password = self.pwd_context.hash(customer_create.password)

        # Create DB model
        # Magic: model_validate copies fields + adds hashed_password
        db_customer = Customer.model_validate(
            customer_create, update={"hashed_password": hashed_password}
        )
        self.session.add(db_customer)
        await self.session.commit()
        await self.session.refresh(db_customer)
        return db_customer

    async def load_customers(self, offset: int, limit: int) -> list[Customer]:
        """Load all customers from database"""
        statement = select(Customer)
        customers = await self.session.exec(statement.offset(offset).limit(limit)).all()
        return customers

    async def is_table_empty(self) -> bool:
        """Load all customers from database"""
        statement = select(Customer)
        response = await self.session.exec(statement.offset(0).limit(1)).all()
        return len(response) == 0

    def get_customer_by_email(self, email: str):
        """Get Customer  from database"""
        statement = select(Customer)
        db_customer = self.session.exec(
            statement.filter(Customer.email == email).first()
        )

        if db_customer is not None:
            return HTTPException(402, detail="email is already used!..")

        #  Check name

        return db_customer

    async def token(self, email, password) -> str:
        """Valide the credentials"""

        condition_on_email = Customer.email == email
        # Select the table like the name of method @TODO Ghis select from sqlmodel
        select(Customer).where(condition_on_email)

        statement = self.session.get(
            Customer, email
        )  # TODO@Ghislain: So  create a statement using Session

        result = await self.session.execute(statement=statement)
        customer: Customer = result.scalar()

        if customer is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="[Ghis]> The Customer with that email is not found!!",
            )

        # Check Password
        is_ok = self.pwd_context.verify(password, customer.hashed_password)
        if not is_ok:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="[Ghis]> The Customer with that Password is incorrect!",
            )

        # Generate Token

        return
