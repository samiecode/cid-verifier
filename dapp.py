from os import environ
import logging
import requests
import json
from multiformats import CID
from typing import Any, List

logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

rollup_server = environ["ROLLUP_HTTP_SERVER_URL"]
logger.info(f"HTTP rollup_server url is {rollup_server}")

cid_verify: List[dict[str,Any]] = []
total_verification = 0

def str_to_hex(str):
    return "0x" + str.encode("utf-8").hex()
def hex_to_str(hex):
    return bytes.fromhex(hex[2:]).decode("utf-8")

def handle_advance(data):
    logger.info(f"Received advance request data {data}")
    global total_verification
    
    payload = data['payload']
    metadata = data['metadata']

    sender = metadata['msg_sender']

    logger.info(f"Payload:: {payload}")

    status = "accept"

    try:
        
        # Ensure payload is a string and remove '0x' prefix if present
        if isinstance(payload, str):
            payload = payload[2:] if payload.startswith('0x') else payload
        else:
            raise ValueError("Payload must be a string")

        payload_str = hex_to_str(payload)
        
        cid = CID.decode(payload_str)
        logger.info(f"CID Verify ::: {cid}")
        
        response = requests.post(rollup_server + "/notice", json={"payload": str_to_hex(f"CID is valid: {cid}")})
        logger.info(f"Received notice status {response.status_code} body {response.content}")

        cid_verify.append({"sender": sender, "cid": str(cid)})
        total_verification += 1

    except Exception as e:
        status = "reject"
        
        response = requests.post(rollup_server + "/report", json={"payload": str_to_hex(f"Invalid CID {str(e)}")})
        logger.info(f"Received report status {response.status_code} body {response.content}")
    

    return status

def handle_inspect(data):
    logger.info(f"Received inspect request data {data}")

    payload = data['payload']

    route = hex_to_str(payload)
    
    if route == "cidVerify":
        msg = json.dumps({"cidVerify": cid_verify})   
    elif route == "totalVerification":
        msg = json.dumps({"total_verification": total_verification})
    else:
        msg = "Invalid route"

    response = requests.post(rollup_server + "/report", json={"payload": str_to_hex(msg)})
    logger.info(f"Received report status {response.status_code} body {response.content}") 

handlers = {
    "advance_state": handle_advance,
    "inspect_state": handle_inspect,
}

while True:
    logger.info("Sending finish")
    response = requests.post(rollup_server + "/finish", json={"status": "accept"})
    logger.info(f"Received finish status {response.status_code}")
    if response.status_code == 202:
        logger.info("No pending rollup request, trying again")
    else:
        rollup_request = response.json()
        handler = handlers[rollup_request["request_type"]]
        result = handler(rollup_request["data"])
        response = requests.post(rollup_server + "/report", json={"payload": str_to_hex(result)})
        logger.info(f"Received report status {response.status_code}")