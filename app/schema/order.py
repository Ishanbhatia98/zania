
from pydantic import BaseModel, HttpUrl
from typing import Dict, Optional, List
from app.type.order_status import OrderStatus
from datetime import datetime

class CreateOrder(BaseModel):
    products: List[Dict[str, int]]

class OrderResponse(BaseModel): 
    products: List[Dict[str, int]]
    id: int
    total_price: float
    status: OrderStatus

    class Config:
        orm_mode = True