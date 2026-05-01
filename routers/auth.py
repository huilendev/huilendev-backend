from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def login():
    return {"token": "fake-jwt-token"}
