from fastapi import FastAPI

from app.database import Base, engine
from app.routers.sales import sales_router
from app.seed import seed_data

Base.metadata.create_all(bind=engine)
seed_data()

app = FastAPI(title="InsightSQL Assistant")

app.include_router(sales_router)


@app.get("/")
def root():
    return {"message": "InsightSQL Assistant API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}
