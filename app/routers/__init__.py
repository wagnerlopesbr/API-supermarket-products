from fastapi import APIRouter

from .brand import router as brand_router
from .category import router as category_router
from .product import router as product_router
from .supermarket import router as supermarket_router
from .api import router as api

router = APIRouter()
router.include_router(brand_router, prefix="/api/brands", tags=["brands"])
router.include_router(category_router, prefix="/api/categories", tags=["categories"])
router.include_router(product_router, prefix="/api/products", tags=["products"])
router.include_router(supermarket_router, prefix="/api/supermarkets", tags=["supermarkets"])
router.include_router(api, prefix="/api", tags=["api"])
