from sqlalchemy import Table, Column, Integer, ForeignKey
from app.database import Base


supermarket_product = Table(
    'supermarket_product',
    Base.metadata,
    Column('supermarket_id', Integer, ForeignKey('supermarkets.id'), primary_key=True),
    Column('product_id', Integer, ForeignKey('products.id'), primary_key=True)
)
