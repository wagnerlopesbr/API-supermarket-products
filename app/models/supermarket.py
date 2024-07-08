from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base
from .supermarket_product import supermarket_product


class Supermarket(Base):
    __tablename__ = 'supermarkets'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String, index=True)
    products = relationship("Product", secondary=supermarket_product, back_populates="supermarkets")
