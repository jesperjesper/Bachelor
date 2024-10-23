from scapy.all import *
from scapy.utils import rdpcap
from scapy.all import IP

receiverIP = '10.5.0.9'

# Open a persistent L3 socket to send packets
socket = conf.L3socket()

# Read packets from the PCAP file
packets = rdpcap("packets.pcap")

# Set destination IP and send the packets
for packet in packets:
    package = packet[IP]
    package.dst = receiverIP
    del(package.chksum)
    # Try to send packet using the persistent L3socket
    try:
        socket.send(package)
    except:
        pass

