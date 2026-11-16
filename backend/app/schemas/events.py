from pydantic import BaseModel, Field

# Model for the request body of the prediction endpoint
class NetworkEvent(BaseModel):
    duration: float = Field(ge=0)
    protocol_type: str = Field(max_length=4, min_length=3)
    service: str = Field(max_length=11, min_length=3)
    flag: str = Field(max_length=6, min_length=2)
    src_bytes: float = Field(ge=0)
    dst_bytes: float = Field(ge=0)
    land: str = Field(max_length=1, min_length=1)
    wrong_fragment: float = Field(ge=0)
    urgent: float = Field(ge=0)
    hot: float = Field(ge=0)
    num_failed_logins: float = Field(ge=0)
    logged_in: str = Field(max_length=1, min_length=1)
    num_compromised: float = Field(ge=0)
    root_shell: float = Field(ge=0)
    su_attempted: float = Field(ge=0)
    num_root: float = Field(ge=0)
    num_file_creations: float = Field(ge=0)
    num_shells: float = Field(ge=0)
    num_access_files: float = Field(ge=0)
    num_outbound_cmds: float = Field(ge=0)
    is_host_login: str = Field(max_length=1, min_length=1)
    is_guest_login: str = Field(max_length=1, min_length=1)
    count: float = Field(ge=0)
    srv_count: float = Field(ge=0)
    serror_rate: float = Field(ge=0)
    srv_serror_rate: float = Field(ge=0)
    rerror_rate: float = Field(ge=0)
    srv_rerror_rate: float = Field(ge=0)
    same_srv_rate: float = Field(ge=0)
    diff_srv_rate: float = Field(ge=0)
    srv_diff_host_rate: float = Field(ge=0)
    dst_host_count: float = Field(ge=0)
    dst_host_srv_count: float = Field(ge=0)
    dst_host_same_srv_rate: float = Field(ge=0)
    dst_host_diff_srv_rate: float = Field(ge=0)
    dst_host_same_src_port_rate: float = Field(ge=0)
    dst_host_srv_diff_host_rate: float = Field(ge=0)
    dst_host_serror_rate: float = Field(ge=0)
    dst_host_srv_serror_rate: float = Field(ge=0)
    dst_host_rerror_rate: float = Field(ge=0)
    dst_host_srv_rerror_rate: float = Field(ge=0)

# Model for the response of the prediction endpoint
class PredictionResponse(BaseModel):
    risk_probability: float = Field(ge=0, le=1) 
    risk_level: str 
 
sample_network_event = {"duration": 0, "protocol_type": "tcp", "service": "private", "flag": "REJ", "src_bytes": 0, "dst_bytes": 0, "land": "0", "wrong_fragment": 0, "urgent": 0, "hot": 0, "num_failed_logins": 0, "logged_in": "0", "num_compromised": 0, "root_shell": 0, "su_attempted": 0, "num_root": 0, "num_file_creations": 0, "num_shells": 0, "num_access_files": 0, "num_outbound_cmds": 0, "is_host_login": "0", "is_guest_login": "0", "count": 229, "srv_count": 10, "serror_rate": 0.00, "srv_serror_rate": 0.00, "rerror_rate": 1.00, "srv_rerror_rate": 1.00, "same_srv_rate": 0.04, "diff_srv_rate": 0.06, "srv_diff_host_rate": 0.00, "dst_host_count": 255, "dst_host_srv_count": 10, "dst_host_same_srv_rate": 0.04, "dst_host_diff_srv_rate": 0.06, "dst_host_same_src_port_rate": 0.00, "dst_host_srv_diff_host_rate": 0.00, "dst_host_serror_rate": 0.00, "dst_host_srv_serror_rate": 0.00, "dst_host_rerror_rate": 1.00, "dst_host_srv_rerror_rate": 1.00}
valid_network_event = NetworkEvent(**sample_network_event)
print(valid_network_event)
