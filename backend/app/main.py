from fastapi import FastAPI
from pydantic import BaseModel

# Providing the options for the model_name path parameter
class NetworkEvent(BaseModel):
    wrong_fragment: float
    num_failed_logins: float
    num_compromised: float
    num_shells: float
    srv_count: float
    serror_rate: float
    rerror_rate: float
    same_srv_rate: float
    dst_host_srv_count: float
    dst_host_same_srv_rate: float
    dst_host_same_src_port_rate: float
    dst_host_serror_rate: float
    dst_host_srv_serror_rate: float
    flag: str
    land: str
    is_host_login: str

# Create FastAPI instance
# Add openapi_url later go to FastAPI defition to see how to add openapi_url
app = FastAPI(title="Risk Scoring Engnine API", 
              description="This is a risk scoring engine API", 
              version="1.0.0")

# tells FastAPI that the function right below is in charge of handling requests that go to: the path / using a get operation
@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/network-events/{srv_count}")
def read_srv_count(srv_count: float):
    return {"srv_count": srv_count}

# 
@app.post("/network-event")
def make_network_event(network_event: NetworkEvent):
    print(network_event)
    return {"message": "Network event received", "data": network_event.model_dump()}

@app.post("/predict")
def predict(event: NetworkEvent):
    # Temporary mock prediction
    return {
        "risk_probability": 0.75,
        "risk_level": "High",
        "prediction": 1,
        "message": "Mock prediction for testing"
    }
