from fastapi.testclient import TestClient
import pytest
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool
# from unittest.mock import AsyncMock

from app.main import app


SQLITE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLITE_URL, connect_args={"check_same_thread": False}, poolclass=StaticPool
)


@pytest.fixture(scope="function", autouse=True)
def session():
    """Clean database + create tables for each test"""
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        yield session


@pytest.fixture
def client(session: Session):
    """TestClient with test database"""

    def override_get_session():
        return session

    app.dependency_overrides[app.services.customer_service.get_session] = (
        override_get_session
    )
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()
