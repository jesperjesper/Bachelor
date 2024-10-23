import json
import pytest
import os
from scapy.all import rdpcap

@pytest.fixture(scope="module")
def log_data():
    log_file_path = "logs/clean_logs.json"  
    with open(log_file_path, "r") as f:
        log_data = json.load(f)
    return log_data
   

def check_packet_payload(packet, log_data):
    if 'TCP' in packet and packet['TCP'].payload:
        payload = packet['TCP'].payload.load.decode('utf-8').lower()  
        print("Payload:", payload)
        for log_entry in log_data:
            alert_content = log_entry.get("alert", "").lower() 
            if payload in alert_content:
                return  
        raise AssertionError(f"Payload '{payload}' not found in log data.")

@pytest.mark.parametrize("packet", rdpcap("./sender/packets.pcap"))
def test_network_payload_presence(packet, log_data):
    #Test network payload presence.
    check_packet_payload(packet, log_data)
