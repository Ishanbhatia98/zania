from datetime import datetime, timedelta
from typing import Callable, List

from fastapi import APIRouter

from app.model.order import Order
from app.model.product import Product
from app.schema.order import CreateOrder, OrderResponse
from app.schema.product import CreateProduct, ProductResponse

router = APIRouter(
    tags=["MANAGE"],
)


@router.post("/products", response_model=ProductResponse)
def add_product(payload: CreateProduct):
    return Product.create(payload)


@router.get("/products", response_model=List[ProductResponse])
def fetch_available_products():
    return Product.filter()


@router.post("/orders", response_model=OrderResponse)
def create_order(
    payload: CreateOrder,
):
    return Order.create(payload)
