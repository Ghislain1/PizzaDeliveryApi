import pytest
from app.models.customer import Customer
from app.services.customer_service import CustomerService
from app.schemas.custom_schema import CustomerCreate


@pytest.mark.parametrize(
    "username,email,password",
    [
        ("alice", "alice@example.com", "secret123"),
        ("bob", "bob@example.com", "mypassword"),
    ],
)
def test_create_customer(session, username, email, password):
    """Test create_customer works with valid data"""
    service = CustomerService(session)
    customer_data = CustomerCreate(username=username, email=email, password=password)

    # Act
    result = service.create_customer(customer_data)

    # Assert
    assert result.username == username
    assert result.email == email
    assert result.hashed_password != password  # Should be hashed!
    assert result.id is not None
    assert result.is_active is False

    # Verify in database
    db_customer = session.get(Customer, result.id)
    assert db_customer is not None


def test_create_customer_duplicate_email(session):
    """Test duplicate email raises error"""
    service = CustomerService(session)

    # Create first customer
    customer1 = service.create_customer(
        CustomerCreate(username="alice", email="test@example.com", password="secret")
    )

    # Try duplicate
    with pytest.raises(Exception):  # Unique constraint violation
        service.create_customer(
            CustomerCreate(username="bob", email="test@example.com", password="secret")
        )


def test_load_customers_empty(session):
    """Test load_customers returns empty list when no customers"""
    service = CustomerService(session)
    customers = service.load_customers()
    assert len(customers) == 0


def test_load_customers_with_data(session):
    """Test load_customers returns all customers"""
    service = CustomerService(session)

    # Create 3 customers
    customers_data = [
        CustomerCreate(username="alice", email="alice@example.com", password="secret1"),
        CustomerCreate(username="bob", email="bob@example.com", password="secret2"),
        CustomerCreate(username="carol", email="carol@example.com", password="secret3"),
    ]

    for data in customers_data:
        service.create_customer(data)

    # Load all
    all_customers = service.load_customers()
    assert len(all_customers) == 3
    assert all_customers[0].username == "alice"
    assert all_customers[1].username == "bob"
