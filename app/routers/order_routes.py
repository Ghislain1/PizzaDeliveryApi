from fastapi import APIRouter

# tags ist for documentation title
router = APIRouter(prefix="/order", tags=["Orders"])


@router.get("/")
async def hello():
    return {"message": "Hello world------"}


@router.post("/")
async def create_order():
    return ""
