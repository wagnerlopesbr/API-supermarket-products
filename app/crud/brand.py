from sqlalchemy.orm import Session
from app.models.brand import Brand as BrandModel
from app.schemas.brand import BrandCreate, BrandUpdate


def get_brand(db: Session, brand_id: int):
    return db.query(BrandModel).filter(BrandModel.id == brand_id).first()


def get_brands(db: Session, skip: int = 0, limit: int = None):
    return db.query(BrandModel).offset(skip).limit(limit).all()


def create_brand(db: Session, brand: BrandCreate):
    db_brand = BrandModel(name=brand.name)
    db.add(db_brand)
    db.commit()
    db.refresh(db_brand)
    return db_brand


def update_brand(db: Session, brand_id: int, brand: BrandUpdate):
    db_brand = get_brand(db, brand_id)
    if db_brand:
        db_brand.name = brand.name
        db.commit()
        db.refresh(db_brand)
    return db_brand


def delete_brand(db: Session, brand_id: int):
    db_brand = get_brand(db, brand_id)
    if db_brand:
        db.delete(db_brand)
        db.commit()
    return db_brand
