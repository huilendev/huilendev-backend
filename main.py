from fastapi import FastAPI
from routers import users, products

app = FastAPI(title="Huilendev Backend API")

app.include_router(users.router)
app.include_router(products.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
