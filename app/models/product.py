from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.database import Base
from .supermarket_product import supermarket_product


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    prices = Column(JSON)
    brand_id = Column(Integer, ForeignKey("brands.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))  # I was about to use a ARRAY type, but SQLAlchemy does not support it with foreign keys

    brand = relationship("Brand", back_populates="products")
    category = relationship("Category", back_populates="products")
    supermarkets = relationship("Supermarket", secondary=supermarket_product, back_populates="products")
