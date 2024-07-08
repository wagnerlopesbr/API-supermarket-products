from fastapi import HTTPException
from app.database import SessionLocal
from app import crud
import random
from datetime import datetime


def update_prices_daily():
    db = SessionLocal()

    try:
        db.begin()
        for product in crud.get_products(db):
            new_price = round((product.price * random.uniform(0.9, 1.1)))
            if new_price != product.price:
                product.price = new_price
                db.add(product)
            print(f"{datetime.now()}: Product {product.name} updated to {new_price}.")
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()
        print(f"\n{datetime.now()}: Products updated successfully and session closed.\n\n\n")
