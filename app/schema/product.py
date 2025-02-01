from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, HttpUrl


class CreateProduct(BaseModel):
    name: str
    description: Optional[str]
    price: float
    stock: Optional[int] = 0


class ProductResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float
    stock: Optional[int] = 0

    class Config:
        from_attributes = True
