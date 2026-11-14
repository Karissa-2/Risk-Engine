# Accepts network events, calls the scoring service, and returns risk predictions. Also retrieves previously calculated predictions.

from fastapi import APIRouter

# Allows the endpoint to be defined outside main.py
router = APIRouter()

#use @router.get instead of @app.get to define the endpoint
@router.get("/predictions")
def get_predictions():
    return {"prediction": "threat detected"}