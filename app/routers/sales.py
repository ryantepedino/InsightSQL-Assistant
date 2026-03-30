from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app import models, schemas

router = APIRouter(prefix="/sales", tags=["sales"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("")
def list_sales(db: Session = Depends(get_db)):
    sales = db.query(models.SalesRecord).all()

    return {
        "total_records": len(sales),
        "data": sales
    }


@router.get("/region/{region_name}")
def list_sales_by_region(region_name: str, db: Session = Depends(get_db)):
    sales = db.query(models.SalesRecord).filter(
        models.SalesRecord.region == region_name
    ).all()

    return {
        "region": region_name,
        "total_records": len(sales),
        "data": sales
    }


@router.get("/summary")
def sales_summary(db: Session = Depends(get_db)):
    total_records = db.query(models.SalesRecord).count()
    total_sales = db.query(
        func.coalesce(func.sum(models.SalesRecord.sales_amount), 0)
    ).scalar()

    return {
        "total_records": total_records,
        "total_sales_amount": total_sales
    }


@router.post("", response_model=schemas.SalesRecordResponse)
def create_sale(sale: schemas.SalesRecordCreate, db: Session = Depends(get_db)):
    new_sale = models.SalesRecord(
        region=sale.region,
        product=sale.product,
        category=sale.category,
        sales_amount=sale.sales_amount,
        sales_month=sale.sales_month
    )

    db.add(new_sale)
    db.commit()
    db.refresh(new_sale)

    return new_sale