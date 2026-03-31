from sqlalchemy import Column, Integer, Float, String

from app.database import Base


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    product = Column(String, nullable=False)
    region = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
