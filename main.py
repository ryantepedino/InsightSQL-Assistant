from fastapi import FastAPI

from app.database import Base, SessionLocal, engine
from app import models
from app.routers.sales import router as sales_router
from app.seed import seed_sales_data

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="InsightSQL Assistant",
    description="API backend para consultas em linguagem natural com foco em BI conversacional.",
    version="0.1.0"
)

app.include_router(sales_router)
with SessionLocal() as db:
    seed_sales_data(db)


@app.get("/")
def read_root():
    return {
        "message": "InsightSQL Assistant API is running successfully."
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }