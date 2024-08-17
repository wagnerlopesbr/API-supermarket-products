from sqlalchemy.orm import Session
from app.models.product import Product as ProductModel
from app.schemas.product import ProductCreate, ProductUpdate


def get_product(db: Session, product_id: int):
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()


def get_products(db: Session, skip: int = 0, limit: int = None):
    return db.query(ProductModel).offset(skip).limit(limit).all()


def create_product(db: Session, product: ProductCreate):
    db_product = ProductModel(
        name=product.name,
        prices=product.prices,
        brand_id=product.brand_id,
        category_id=product.category_id
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, product_id: int, product: ProductUpdate):
    db_product = get_product(db, product_id)
    if db_product:
        db_product.name = product.name
        db_product.prices = product.prices
        db_product.brand_id = product.brand_id
        db_product.category_id = product.category_id
        db.commit()
        db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product
