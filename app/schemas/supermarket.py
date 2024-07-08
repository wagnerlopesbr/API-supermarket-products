from pydantic import BaseModel


class SupermarketBase(BaseModel):
    name: str
    address: str


class SupermarketCreate(SupermarketBase):
    pass


class SupermarketUpdate(SupermarketBase):
    pass


class Supermarket(SupermarketBase):
    id: int

    class Config:
        from_attributes = True
