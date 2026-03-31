from pydantic import BaseModel, ConfigDict


class SaleBase(BaseModel):
    product: str
    region: str
    amount: float


class SaleCreate(SaleBase):
    pass


class SaleResponse(SaleBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
