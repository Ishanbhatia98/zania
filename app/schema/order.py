from datetime import datetime
from typing import Dict, List, Optional

from pydantic import BaseModel, HttpUrl

from app.type.order_status import OrderStatus


class CreateOrder(BaseModel):
    products: List[Dict[str, int]]


class OrderResponse(BaseModel):
    products: List[Dict[str, int]]
    id: int
    total_price: float
    status: OrderStatus

    class Config:
        from_attributes = True
