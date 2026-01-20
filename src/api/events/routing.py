from fastapi import APIRouter
import os 
from db.config import DATABASE_URL
router = APIRouter()


@router.get("/")
def read_events():
    return {"message": "Events", "DATABASE_URL": DATABASE_URL}
