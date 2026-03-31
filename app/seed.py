from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Sale


def seed_data():
    db: Session = SessionLocal()

    try:
        existing_sales = db.query(Sale).count()

        if existing_sales == 0:
            seed_sales = [
                Sale(product="Notebook", region="Sudeste", amount=3500.0),
                Sale(product="Mouse", region="Sul", amount=120.0),
                Sale(product="Teclado", region="Nordeste", amount=250.0),
                Sale(product="Monitor", region="Sudeste", amount=899.9),
            ]

            db.add_all(seed_sales)
            db.commit()
    finally:
        db.close()
