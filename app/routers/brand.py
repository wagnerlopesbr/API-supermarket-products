from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import brand as crud
from app.schemas import Brand, BrandCreate, BrandUpdate
from app.database import SessionLocal


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @router.post("/", response_model=Brand)
# def create_brand(brand: BrandCreate, db: Session = Depends(get_db)):
#     return crud.create_brand(db=db, brand=brand)


@router.get("/{brand_id}", response_model=Brand)
def read_brand(brand_id: int, db: Session = Depends(get_db)):
    db_brand = crud.get_brand(db=db, brand_id=brand_id)
    if db_brand is None:
        raise HTTPException(status_code=404, detail="Brand not found")
    return db_brand


# @router.put("/{brand_id}", response_model=Brand)
# def update_brand(brand_id: int, brand: BrandUpdate, db: Session = Depends(get_db)):
#     db_brand = crud.get_brand(db=db, brand_id=brand_id)
#     if db_brand is None:
#         raise HTTPException(status_code=404, detail="Brand not found")
#     return crud.update_brand(db=db, brand_id=brand_id, brand=brand)


# @router.delete("/{brand_id}", response_model=Brand)
# def delete_brand(brand_id: int, db: Session = Depends(get_db)):
#     db_brand = crud.get_brand(db=db, brand_id=brand_id)
#     if db_brand is None:
#         raise HTTPException(status_code=404, detail="Brand not found")
#     return crud.delete_brand(db=db, brand_id=brand_id)


@router.get("/", response_model=list[Brand])
def read_brands(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    brands = crud.get_brands(db=db, skip=skip, limit=limit)
    return brands
