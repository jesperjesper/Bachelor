
import json
from datetime import datetime
from scapy.all import sniff, IP, TCP

# Define a list of signatures with rate-limiting parameters
signatures = [
    {"name": "Testing123 Message on Port 9999", "ports": [9999], "pattern": "testing123", "case_sensitive": False},
]

log_filename = "ids_logs.txt"
log_file = open(log_filename, "a")
alerts = []

def match_signature(packet, signature):
    if "ports" in signature:
        # Check if the packet's source or destination port matches any in the signature
        return packet[TCP].sport in signature["ports"] or packet[TCP].dport in signature["ports"]
    elif "pattern" in signature:
        # Check if the packet payload contains the signature pattern
        payload = str(packet[TCP].payload)
        if not signature.get("case_sensitive", True):
            payload = payload.lower()
        return signature["pattern"] in payload
    return False

def packet_handler(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP): #Checks if the network packet uses an IP and TCP
        for signature in signatures: #loops through the signatures
            if match_signature(packet, signature): #Matches the packet with the signature
                generate_alert(packet, signature) #Calls upon the function to generate an alert if it matches

def generate_alert(packet, signature):
    alert = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "alert": f"Suspicious activity detected - {signature['name']}",
        "source_ip": packet[IP].src,
        "source_port": packet[TCP].sport,
        "destination_ip": packet[IP].dst,
        "destination_port": packet[TCP].dport,
    }
    alerts.append(alert)
    print(alerts)

#Start the sniffing process
sniff(prn=packet_handler, store=0, filter="tcp", iface="eth0")

log_file.write(json.dumps(alerts, indent=4)) # Write all alerts to the log file as a JSON array
print(alerts)
log_file.close()



