from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models import Sale


def get_region_insights(db: Session) -> list[dict]:
    results = (
        db.query(
            Sale.region,
            func.count(Sale.id).label("total_sales"),
            func.sum(Sale.amount).label("total_revenue"),
            func.avg(Sale.amount).label("average_ticket"),
        )
        .group_by(Sale.region)
        .order_by(func.sum(Sale.amount).desc())
        .all()
    )

    insights = []
    for row in results:
        insights.append(
            {
                "region": row.region,
                "total_sales": row.total_sales,
                "total_revenue": round(float(row.total_revenue or 0), 2),
                "average_ticket": round(float(row.average_ticket or 0), 2),
            }
        )

    return insights
