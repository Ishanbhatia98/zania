

from .main import BaseSQL, GetOr404Mixin, UniqueSlugMixin

from sqlalchemy import Column, Enum, LargeBinary, String, Text, Integer, DateTime, Boolean, Float, JSON, Enum
from datetime import datetime, timedelta
from fastapi import HTTPException, status
from fastapi.responses import RedirectResponse

from .product import Product
from app.type.order_status import OrderStatus


class Order(BaseSQL, GetOr404Mixin, UniqueSlugMixin):
    __tablename__ = "order"
    
    id = Column(Integer, primary_key=True, index=True)
    products = Column(JSON, nullable=False)
    total_price = Column(Float, default=datetime.utcnow)
    status = Column(Enum(OrderStatus), nullable=False, default=OrderStatus.PENDING)

    @classmethod
    def create(cls, payload):
        total_price = Product.validate_and_reserve_(payload.products)
        new_order = super().create(
            products=payload.products,
            total_price=total_price,
            status=OrderStatus.PENDING
        )
        return new_order