from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Sale
from app.schemas import SaleCreate, SaleResponse
from app.services.analytics import get_sales_summary
from app.services.region_insights import get_region_insights

sales_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@sales_router.get("/sales", response_model=list[SaleResponse])
def get_sales(db: Session = Depends(get_db)):
    return db.query(Sale).all()


@sales_router.post("/sales", response_model=SaleResponse)
def create_sale(sale: SaleCreate, db: Session = Depends(get_db)):
    new_sale = Sale(
        product=sale.product,
        region=sale.region,
        amount=sale.amount
    )
    db.add(new_sale)
    db.commit()
    db.refresh(new_sale)
    return new_sale


@sales_router.get("/sales/region/{region_name}", response_model=list[SaleResponse])
def get_sales_by_region(region_name: str, db: Session = Depends(get_db)):
    sales = db.query(Sale).filter(Sale.region.ilike(region_name)).all()

    if not sales:
        raise HTTPException(status_code=404, detail="Nenhuma venda encontrada para essa região.")

    return sales


@sales_router.get("/sales/summary")
def sales_summary(db: Session = Depends(get_db)):
    return get_sales_summary(db)


@sales_router.get("/sales/insights/regions")
def sales_region_insights(db: Session = Depends(get_db)):
    return get_region_insights(db)
