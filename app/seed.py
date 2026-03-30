from sqlalchemy.orm import Session

from app import models


def seed_sales_data(db: Session):
    existing_records = db.query(models.SalesRecord).count()

    if existing_records > 0:
        return

    sample_data = [
        models.SalesRecord(
            region="Sudeste",
            product="Notebook Pro 15",
            category="Eletrônicos",
            sales_amount=12500.50,
            sales_month="2026-03"
        ),
        models.SalesRecord(
            region="Sul",
            product='Monitor UltraWide 34"',
            category="Eletrônicos",
            sales_amount=4200.00,
            sales_month="2026-03"
        ),
        models.SalesRecord(
            region="Nordeste",
            product="Cadeira Office Plus",
            category="Móveis",
            sales_amount=1850.90,
            sales_month="2026-02"
        ),
        models.SalesRecord(
            region="Centro-Oeste",
            product="Mesa Executiva",
            category="Móveis",
            sales_amount=3100.00,
            sales_month="2026-02"
        )
    ]

    db.add_all(sample_data)
    db.commit()