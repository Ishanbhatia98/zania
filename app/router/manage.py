
from typing import Callable, List
from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.schema.product import CreateProduct, ProductResponse
from app.schema.order import CreateOrder, OrderResponse

from app.model.product import Product
from app.model.order import Order
from app.database import db_session_wrapper

router = APIRouter(
    tags=["MANAGE"],
)

@router.post("/products", response_model=ProductResponse)
def add_product(
    payload: CreateProduct
):
    return Product.create(payload)


@router.get("/products", response_model=List[ProductResponse])
def fetch_available_products():
    return Product.filter()


@router.post("/orders", response_model=OrderResponse)
def create_order(
    payload: CreateOrder,
):
    return Order.create(payload)