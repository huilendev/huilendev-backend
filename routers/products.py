from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/")
def get_products():
    return [{"id": 1, "name": "Widget", "price": 9.99}]
