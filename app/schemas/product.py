from pydantic import BaseModel
from typing import Dict


class ProductBase(BaseModel):
    name: str
    prices: Dict[int, int]
    brand_id: int
    category_id: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True
