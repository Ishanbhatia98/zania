from datetime import datetime, timedelta
from typing import Dict

from fastapi import HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum,
    Float,
    Integer,
    LargeBinary,
    String,
    Text,
)

from .main import BaseSQL, GetOr404Mixin, UniqueSlugMixin


class Product(BaseSQL, GetOr404Mixin, UniqueSlugMixin):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)

    @classmethod
    def create(cls, payload):
        return super().create(**payload.dict())

    @classmethod
    def validate_and_reserve_(cls, products: Dict):
        total_price = 0
        for product in products:
            product_instance = cls.get_or_404(id=product["id"])
            if product_instance.stock < product["quantity"]:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail=f"Insufficient stock for product: {product_instance.name}",
                )

            total_price += product_instance.price * product["quantity"]
        for product in products:
            product_instance = cls.get_or_404(id=product["id"])
            cls.edit(
                product_instance.id, stock=product_instance.stock - product["quantity"]
            )
        return total_price
