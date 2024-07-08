from sqlalchemy.orm import Session
from app.models.supermarket import Supermarket as SupermarketModel
from app.schemas.supermarket import SupermarketCreate, SupermarketUpdate


def get_supermarket(db: Session, supermarket_id: int):
    return db.query(SupermarketModel).filter(SupermarketModel.id == supermarket_id).first()


def get_supermarkets(db: Session, skip: int = 0, limit: int = None):
    return db.query(SupermarketModel).offset(skip).limit(limit).all()


def create_supermarket(db: Session, supermarket: SupermarketCreate):
    db_supermarket = SupermarketModel(name=supermarket.name, address=supermarket.address)
    db.add(db_supermarket)
    db.commit()
    db.refresh(db_supermarket)
    return db_supermarket


def update_supermarket(db: Session, supermarket_id: int, supermarket: SupermarketUpdate):
    db_supermarket = get_supermarket(db, supermarket_id)
    if db_supermarket:
        db_supermarket.name = supermarket.name
        db_supermarket.address = supermarket.address
        db.commit()
        db.refresh(db_supermarket)
    return db_supermarket


def delete_supermarket(db: Session, supermarket_id: int):
    db_supermarket = get_supermarket(db, supermarket_id)
    if db_supermarket:
        db.delete(db_supermarket)
        db.commit()
    return db_supermarket
