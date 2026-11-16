
from fastapi import APIRouter
from ...schemas.order import CoffeeOrder

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/")
def create_order(order: CoffeeOrder):
    return {
        "message": "Order received",
        "customer": order.customer_name,
        "coffee": order.coffee,
        "quantity": order.quantity,
        "total": order.quantity * order.price
    }
