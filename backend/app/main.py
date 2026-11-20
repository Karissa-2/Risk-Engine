from fastapi import FastAPI
from .api.routes import health, predictions, orders

# Create FastAPI instance
# Add openapi_url later go to FastAPI defition to see how to add openapi_url
app = FastAPI(title="Risk Scoring Engnine API", 
              description="This is a risk scoring engine API", 
              version="1.0.0")

# tells FastAPI that the function right below is in charge of handling requests that go to: the path / using a get operation
@app.get("/")
def home():
    return "Hello"

app.include_router(
    health.router, 
    prefix="/api/v1"
)

app.include_router(
    predictions.router,
    prefix="/api/v1"
)

app.include_router(
    orders.router,
    prefix="/api/v1"
)

