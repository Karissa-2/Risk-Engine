# Accepts network events, calls the scoring service, and returns risk predictions. Also retrieves previously calculated predictions.

from fastapi import APIRouter
from ...schemas.events import NetworkEvent

# Allows the endpoint to be defined outside main.py
router = APIRouter(prefix="/predictions", tags=["predictions"])

#use @router.get instead of @app.get to define the endpoint
@router.get("/")
def get_predictions():
    return {"prediction": "threat detected"}

@router.post("/predict")
def create_prediction(network_event: NetworkEvent):
    return {"message": "Event received", 
            "duration": network_event.duration,
            "protocol_type": network_event.protocol_type,
            "service": network_event.service,
            "flag": network_event.flag,
            "src_bytes": network_event.src_bytes,
            "dst_bytes": network_event.dst_bytes,
            "land": network_event.land,
            "wrong_fragment": network_event.wrong_fragment,
            "urgent": network_event.urgent,
            "hot": network_event.hot,
            "num_failed_logins": network_event.num_failed_logins,
            "logged_in": network_event.logged_in,
            "num_compromised": network_event.num_compromised,
            "root_shell": network_event.root_shell,
            "su_attempted": network_event.su_attempted,
            "num_root": network_event.num_root,
            "num_file_creations": network_event.num_file_creations,
            "num_shells": network_event.num_shells,
            "num_access_files": network_event.num_access_files,
            "num_outbound_cmds": network_event.num_outbound_cmds,
            "is_host_login": network_event.is_host_login,
            "is_guest_login": network_event.is_guest_login,
            "count": network_event.count,
            "srv_count": network_event.srv_count,
            "serror_rate": network_event.serror_rate,
            "srv_serror_rate": network_event.srv_serror_rate,
            "rerror_rate": network_event.rerror_rate,
            "srv_rerror_rate": network_event.srv_rerror_rate,
            "same_srv_rate": network_event.same_srv_rate,
            "diff_srv_rate": network_event.diff_srv_rate,
            "srv_diff_host_rate": network_event.srv_diff_host_rate,
            "dst_host_count": network_event.dst_host_count,
            "dst_host_srv_count": network_event.dst_host_srv_count,
            "dst_host_same_srv_rate": network_event.dst_host_same_srv_rate,
            "dst_host_diff_srv_rate": network_event.dst_host_diff_srv_rate,
            "dst_host_same_src_port_rate": network_event.dst_host_same_src_port_rate,
            "dst_host_srv_diff_host_rate": network_event.dst_host_srv_diff_host_rate,
            "dst_host_serror_rate": network_event.dst_host_serror_rate,
            "dst_host_srv_serror_rate": network_event.dst_host_srv_serror_rate,
            "dst_host_rerror_rate": network_event.dst_host_rerror_rate,
            "dst_host_srv_rerror_rate": network_event.dst_host_srv_rerror_rate
            }