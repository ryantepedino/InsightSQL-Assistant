from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models import Sale


def get_sales_summary(db: Session) -> dict:
    total_sales = db.query(func.count(Sale.id)).scalar() or 0
    total_revenue = db.query(func.sum(Sale.amount)).scalar() or 0
    average_ticket = total_revenue / total_sales if total_sales else 0

    return {
        "total_sales": total_sales,
        "total_revenue": float(total_revenue),
        "average_ticket": round(float(average_ticket), 2),
    }
