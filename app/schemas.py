from pydantic import BaseModel


class SalesRecordBase(BaseModel):
    region: str
    product: str
    category: str
    sales_amount: float
    sales_month: str


class SalesRecordCreate(SalesRecordBase):
    pass


class SalesRecordResponse(SalesRecordBase):
    id: int

    class Config:
        from_attributes = True