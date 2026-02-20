from fastapi import APIRouter, Depends


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# tags ist for documentation title
router = APIRouter(prefix="/order", tags=["Orders"])


@router.get("/")
async def hello(token: str):
    return {"message": "Hello world------"}


@router.get("/security/")
async def read_items(token: str):
    return {"token": token}


@router.post("/")
async def create_order():
    return ""
