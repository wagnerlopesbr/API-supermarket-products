from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    price: int
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
