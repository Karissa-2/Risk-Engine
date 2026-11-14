from pydantic import BaseModel, Field

class NetworkEvent(BaseModel):
    duration: float
    protocol_type: str
    service: str
    flag: str
    src_bytes: float
    dst_bytes: float
    land: str
    wrong_fragment: float
    urgent: float
    hot: float
    num_failed_logins: float
    logged_in: str
    num_compromised: float
    root_shell: float
    su_attempted: float
    num_root: float
    num_file_creations: float
    num_shells: float
    num_access_files: float
    num_outbound_cmds: float
    is_host_login: str
    is_guest_login: str
    count: float
    srv_count: float
    serror_rate: float
    srv_serror_rate: float
    rerror_rate: float
    srv_rerror_rate: float
    same_srv_rate: float
    diff_srv_rate: float
    srv_diff_host_rate: float
    dst_host_count: float
    dst_host_srv_count: float
    dst_host_same_srv_rate: float
    dst_host_diff_srv_rate: float
    dst_host_same_src_port_rate: float
    dst_host_srv_diff_host_rate: float
    dst_host_serror_rate: float
    dst_host_srv_serror_rate: float


class PredictionResponse(BaseModel):
    risk_probability: float = Field(ge=0, le=100) 
    risk_level: str 
 
sample_network_event = {"duration": 0, "protocol_type": "tcp", "service": "private", "flag": "REJ", "src_bytes": 0, "dst_bytes": 0, "land": "0", "wrong_fragment": 0, "urgent": 0, "hot": 0, "num_failed_logins": 0, "logged_in": "0", "num_compromised": 0, "root_shell": 0, "su_attempted": 0, "num_root": 0, "num_file_creations": 0, "num_shells": 0, "num_access_files": 0, "num_outbound_cmds": 0, "is_host_login": "0", "is_guest_login": "0", "count": 229, "srv_count": 10, "serror_rate": 0.00, "srv_serror_rate": 0.00, "rerror_rate": 1.00, "srv_rerror_rate": 1.00, "same_srv_rate": 0.04, "diff_srv_rate": 0.06, "srv_diff_host_rate": 0.00, "dst_host_count": 255, "dst_host_srv_count": 10, "dst_host_same_srv_rate": 0.04, "dst_host_diff_srv_rate": 0.06, "dst_host_same_src_port_rate": 0.00, "dst_host_srv_diff_host_rate": 0.00, "dst_host_serror_rate": 0.00, "dst_host_srv_serror_rate": 0.00, "dst_host_rerror_rate": 1.00, "dst_host_srv_rerror_rate": 1.00}
valid_network_event = NetworkEvent(**sample_network_event)
print(valid_network_event)


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