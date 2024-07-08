from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import supermarket as crud
from app.schemas import Supermarket, SupermarketCreate, SupermarketUpdate
from app.database import SessionLocal


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @router.post("/", response_model=Supermarket)
# def create_supermarket(supermarket: SupermarketCreate, db: Session = Depends(get_db)):
#     return crud.create_supermarket(db=db, supermarket=supermarket)


@router.get("/{supermarket_id}", response_model=Supermarket)
def read_supermarket(supermarket_id: int, db: Session = Depends(get_db)):
    db_supermarket = crud.get_supermarket(db=db, supermarket_id=supermarket_id)
    if db_supermarket is None:
        raise HTTPException(status_code=404, detail="Supermarket not found")
    return db_supermarket


# @router.put("/{supermarket_id}", response_model=Supermarket)
# def update_supermarket(supermarket_id: int, supermarket: SupermarketUpdate, db: Session = Depends(get_db)):
#     db_supermarket = crud.get_supermarket(db=db, supermarket_id=supermarket_id)
#     if db_supermarket is None:
#         raise HTTPException(status_code=404, detail="Supermarket not found")
#     return crud.update_supermarket(db=db, supermarket_id=supermarket_id, supermarket=supermarket)


# @router.delete("/{supermarket_id}", response_model=Supermarket)
# def delete_supermarket(supermarket_id: int, db: Session = Depends(get_db)):
#     db_supermarket = crud.get_supermarket(db=db, supermarket_id=supermarket_id)
#     if db_supermarket is None:
#         raise HTTPException(status_code=404, detail="Supermarket not found")
#     return crud.delete_supermarket(db=db, supermarket_id=supermarket_id)


@router.get("/", response_model=list[Supermarket])
def read_supermarkets(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    supermarkets = crud.get_supermarkets(db=db, skip=skip, limit=limit)
    return supermarkets
