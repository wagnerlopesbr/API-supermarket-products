from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import category as crud
from app.schemas import Category, CategoryCreate, CategoryUpdate
from app.database import SessionLocal


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @router.post("/", response_model=Category)
# def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
#     return crud.create_category(db=db, category=category)


@router.get("/{category_id}", response_model=Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.get_category(db=db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category


# @router.put("/{category_id}", response_model=Category)
# def update_category(category_id: int, category: CategoryUpdate, db: Session = Depends(get_db)):
#     db_category = crud.get_category(db=db, category_id=category_id)
#     if db_category is None:
#         raise HTTPException(status_code=404, detail="Category not found")
#     return crud.update_category(db=db, category_id=category_id, category=category)


# @router.delete("/{category_id}", response_model=Category)
# def delete_category(category_id: int, db: Session = Depends(get_db)):
#     db_category = crud.get_category(db=db, category_id=category_id)
#     if db_category is None:
#         raise HTTPException(status_code=404, detail="Category not found")
#     return crud.delete_category(db=db, category_id=category_id)


@router.get("/", response_model=list[Category])
def read_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    categories = crud.get_categories(db=db, skip=skip, limit=limit)
    return categories
