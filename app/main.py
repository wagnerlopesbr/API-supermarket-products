from fastapi import FastAPI
from app.routers import router as api_router
import schedule
import time
import threading
import update_prices_daily as up
from dotenv import load_dotenv

load_dotenv()


app = FastAPI(title="Supermarket Products API")


app.include_router(api_router)


@app.get("/")
async def read_root():
    return {
        "by @wagnerlopesbr": "Welcome to the Supermarket Products API.",
        "endpoints": {
            "infos": "/api",
            "for devs": "/api/dev",
            "supermarkets": "/api/supermarkets",
            "supermarkets by id": "/api/supermarkets/id(integer)",
            "brands": "/api/brands",
            "brands by id": "/api/brands/id(integer)",
            "categories": "/api/categories",
            "categories by id": "/api/categories/id(integer)",
            "products": "/api/products",
            "products by id": "/api/products/id(integer)",
        }
    }

def job():
    print("Updating prices...\n")
    up.update_prices_daily()


def schedule_job():
    schedule.every().day.at("08:00", "America/Sao_Paulo").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)


threading.Thread(target=schedule_job).start()
