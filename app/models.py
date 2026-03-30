from sqlalchemy import Column, Integer, Float, String
from app.database import Base


class SalesRecord(Base):
    __tablename__ = "sales_records"

    id = Column(Integer, primary_key=True, index=True)
    region = Column(String, nullable=False)
    product = Column(String, nullable=False)
    category = Column(String, nullable=False)
    sales_amount = Column(Float, nullable=False)
    sales_month = Column(String, nullable=False)