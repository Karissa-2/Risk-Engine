# What columns/features will the model receive? 

## KDDTrain+.arff

```python
numeric = [
    "wrong_fragment", "num_failed_logins", "num_compromised",
    "num_shells", "srv_count", "serror_rate", "rerror_rate",
    "same_srv_rate", "dst_host_srv_count", "dst_host_same_srv_rate",
    "dst_host_same_src_port_rate", "dst_host_serror_rate" "dst_host_srv_serror_rate",
]

categorical = [
    "flag", "land", "is_host_login",
]
```

| Attribute | Line | Description |
|----|---|-------|
| flag | line 5 | connections the computers send to eacch other |
| land | line 8 | LAND attack detects Denial of Service (DoS)|
| wrong_fragment | line 9 | tampered or invalid pieces of an IP packet designed to confuse firewalls, bypass intrusion detection systems (IDS), or crash a target system during packet reassembly |
| num_failed_logins | line 12 | the count of failed login attempts during a network connection |
| num_compromised | line 14 | the number of "compromised" conditions or security breaches observed in a network connection. |
| num_shells | line 19 | represents the number of shell prompts invoked during a network connection or session # > 0 = suspicous activity |
| is_host_login | line 22 | host login = 1, not logged in = 0|
| srv_count | line 25 | the number of connections to the same service as the current connection within the past 2 seconds |
| serror_rate | line 26 | the percentage of connections that have SYN errors specifically, the S0, S1, S2, or S3 flag indicating a failed or incomplete TCP connection handshake |
| rerror_rate | line 28 | the percentage of network connections that have REJ (Reject) errors |
| same_srv_rate | line 30 | the percentage of connections to the same service out of all connections examined in a specific time window. Indicates normal heavy traffic to a popular service or specific denial-of-service (DoS) and probing attacks that repeatedly hit the same service port in a short time frame.|
| dst_host_srv_count | line 34 | this looks at a window of the last 100 connections to the same destination host. It counts how many of those 100 connections used the same service as the current connection. |
| dst_host_same_srv_rate | line 35 | the percentage of connections that were to the same service.  Host-based window. It looks across a sample of past connections that share the same destination host IP address. |
| dst_host_same_src_port_rate | line 37 | represents the percentage of connections to the same source port among the host-based traffic features. |
| dst_host_serror_rate | line 39 | The percentage of connections to the same destination host that activated the SYN error flag. |
| dst_host_srv_serror_rate | line 40 | It represents the percentage of connections to the specified destination host and service that have an S0 (SYN) error. |

## Implement Later
| Attribute | Line | Description |
|----|---|-------|
| root_shell | line 15 | highest-level administrative privileges that shouldn only be accessed by certain people but can be exploited |
|num_root | line 17 | number of root accesses or operattions performed during a network connection. connects to root shell & su attempted|
| num_file_creations | line 18 | the number of file creation operations recorded within a network connection |
| srv_serror_rate | line 27 | a numerical feature that represents the percentage of connections that have SYN (synchronization) errors for the same service indicator for |
| srv_rerror_rate | line 29 | represents the percentage of connections to the same service that have a REJ (Connection Rejected) error flag. |
| srv_diff_host_rate | line 32 | the percentage of connections that were made to different hosts among the connections aggregated by service. |
| diff_srv_rate | line 31 | the percentage of connections to different services among the connections aggregated in the past time window. High values of diff_srv_rate can indicate port scanning, probe attacks, or distributed denial-of-service (DDoS) behavior.|
| dst_host_diff_srv_rate | line 36 | the percentage of connections to different services among the last 100 connections targeting the same destination host. |
| dst_host_srv_diff_host_rate | line 38 | the percentage of connections to the same service that originated from different source hosts. |
| dst_host_rerror_rate | line 41 | continuous numeric feature representing the percentage network anomalies like port scanning or denial-of-service (DoS) attacks, where a malicious source attempts to rapidly connect to closed ports on a target host, triggering a high volume of connection rejections |
| dst_host_srv_rerror_rate | line  42 | The percentage of connections to the specified host (dst_host) and service (srv) that currently have an RSTO error (REJ - connection rejected or reset flag behavior). |