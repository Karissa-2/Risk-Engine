from pydantic import BaseModel

class CoffeeOrder(BaseModel):
    customer_name: str
    coffee: str
    quantity: int
    price: float
