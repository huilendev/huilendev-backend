from fastapi import FastAPI
from routers import users, products, auth

app = FastAPI(title="Huilendev Backend API")

app.include_router(users.router)
app.include_router(products.router)
app.include_router(auth.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
