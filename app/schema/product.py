
from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from datetime import datetime

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
        orm_mode = True