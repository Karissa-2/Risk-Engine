# Checks whether the API is running and responding correctly.

from fastapi import APIRouter

# Allows the endpoint to be defined outside main.py
router = APIRouter()

#use @router.get instead of @app.get to define the endpoint
@router.get("/health")
def health():
    return {"status": "healthy"}






