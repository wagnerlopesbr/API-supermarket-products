from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def read_formatted_data(db: Session = Depends(get_db)):
    try:
        supermarkets = crud.get_supermarkets(db)
        formatted_supermarkets = {
            "total": len(supermarkets),
            "list": [supermarket.name for supermarket in supermarkets]
        }

        brands = crud.get_brands(db)
        brand_dict = {brand.id: brand.name for brand in brands}
        formatted_brands = {
            "total": len(brands),
            "list": [brand.name for brand in brands]
        }

        categories = crud.get_categories(db)
        category_dict = {category.id: category.name for category in categories}
        formatted_categories = {
            "total": len(categories),
            "list": [category.name for category in categories]
        }

        products = crud.get_products(db)
        formatted_products = []
        for product in products:
            cents = f"{str(product.price)[-2:]}"
            if product.price < 100:
                price_str = f"0.{cents}"
            else:
                price_str = f"{str(product.price)[:-2]}.{cents}"
            formatted_product = {
                "product": f"{product.name} - {brand_dict.get(product.brand_id)}",
                "category": category_dict.get(product.category_id),
                "price": price_str
            }
            formatted_products.append(formatted_product)
        formatted_products_response = {
            "total": len(formatted_products),
            "list": formatted_products
        }

        return {
            "supermarkets": formatted_supermarkets,
            "brands": formatted_brands,
            "categories": formatted_categories,
            "products": formatted_products_response
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"deu ruim: {e}")


@router.get("/dev")
def read_raw_data(db: Session = Depends(get_db)):
    try:
        supermarkets = crud.get_supermarkets(db)
        brands = crud.get_brands(db)
        categories = crud.get_categories(db)
        products = crud.get_products(db)
        return {
            "supermarkets": supermarkets,
            "brands": brands,
            "categories": categories,
            "products": products,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"deu ruim: {e}")
