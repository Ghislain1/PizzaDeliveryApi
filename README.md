# PizzaDeliveryApi
A learning-focused FastAPI repository built around a simple Pizza Delivery API. This project is designed to learn FastAPI and SQLModel by reading [official documentation](https://fastapi.tiangolo.com/learn/) and applying concepts step by step in a real-world CRUD API.

## Commands and Findings
- .venv\Scripts\activate  ==> activate my virtual environment
- fastapi dev app/main.py  ==> to  Run app in dev Mode
- uv run pytest tests/ . -v ==> Run all py test cmd
- uv run ruff check . --fix  ==> ruff must be installed
- uv pip freeze > requirements.txt : in that file you see all used package
- uv pip true 

## External packages
- 
---





## 🎯 Learning Goals

* Understand **FastAPI fundamentals**
* Learn **SQLModel** (Pydantic + SQLAlchemy together)
* Build a **clean REST API**
* Learn **dependency injection**
* Practice **database modeling & relationships**
* Read and apply **official docs**, not magic code

---

## 🍕 Why a Pizza Delivery API?

Because it’s:

* Simple but realistic
* Has **real entities** (Pizza, Order, Customer)
* Covers **CRUD**, relationships, and business logic
* Easy to extend later **(auth, payments, async, etc.)**

---

## 🧠 What You’ll Learn (Step by Step)

### 1️⃣ FastAPI Basics

* Path operations (`GET`, `POST`, `PUT`, `DELETE`)
* Request & response models
* Automatic OpenAPI docs (`/docs`)
* Validation with Pydantic

### 2️⃣ SQLModel Basics

* Defining models
* Table vs schema models
* SQLite for fast iteration
* Sessions and engine
* Relationships (Order ↔ Pizza)

### 3️⃣ API Design

* CRUD endpoints
* Clear route structure
* Separation of concerns
* Error handling

### 4️⃣ Real-World Patterns

* Dependency injection (`Depends`)
* Database sessions per request
* Reusable schemas
* Simple business logic (order total, availability)

---

## 🗂️ Suggested Repo Structure

```
fastapi-sqlmodel-pizza-delivery/
│
├── app/
│   ├── main.py          # FastAPI app entry point
|   ├── __init__.py      # ← Empty file, makes 'app' as package
│   ├── db.py            # Engine & session
│   ├── models/          # SQLModel models
│   ├── schemas/         # Request/response schemas ie. CustomerPublic
│   ├── services/        # Database operations and combine table model and data model i.e CustomerService
│   ├── routes/
│   │   ├── pizzas.py
│   │   ├── orders.py
│   │   └── customers.py
│
├── README.md
├── requirements.txt
└── pizza.db             # SQLite database
```

---

## 🔄 Example Domain Model

* **Pizza**

  * id
  * name
  * price
  * available

* **Customer**

  * id
  * name
  * address

* **Order**

  * id
  * customer_id
  * pizza_id
  * quantity
  * total_price

---

## 🧭 How to Learn with This Repo

1. **Read FastAPI docs**
2. Implement *one endpoint*
3. Test it in `/docs`
4. Read SQLModel docs
5. Improve the model
6. Repeat 🚀

No rushing. No copy-paste hell.

---

## 🖼️ Mental Model (What’s Happening)

Request → FastAPI → Validation → SQLModel → Database → Response

---

## 🚀 Next Natural Extensions

Once you’re comfortable:

* Authentication (JWT)
* Async database
* Alembic migrations
* Pagination & filtering
* Docker

---

