from datetime import datetime, timedelta

from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

from app.database import db_instance
from app.router.manage import router as manage_router

app = FastAPI(
    title="E commerce API",
    description="API for an e-commerce platform",
    version="0.1",
    docs_url="/comm/docs",
    redoc_url="/comm/redoc",
)
db_instance.base.metadata.create_all(bind=db_instance._engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/comm/health")
def health():
    return {"status": "ok"}


app.include_router(manage_router, prefix="/comm")
