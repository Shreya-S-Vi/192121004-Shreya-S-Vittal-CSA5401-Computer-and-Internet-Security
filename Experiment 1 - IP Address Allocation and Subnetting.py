import scapy.all as scapy
import matplotlib.pyplot as plt
import numpy as np
from scapy.all import sniff
def capture_packets(packet): 
    if packet.haslayer(scapy.IP): 
        print(f"Source IP: {packet[scapy.IP].src}, Destination IP: {packet[scapy.IP].dst}") 
        sniff(prn=capture_packets, count=10)  # Capture 10 packets
from collections import Counter 
import matplotlib.pyplot as plt 
 
ip_count = Counter() 
 
def capture_packets(packet): 
    if packet.haslayer(scapy.IP): 
        ip_count[packet[scapy.IP].src] += 1 
        ip_count[packet[scapy.IP].dst] += 1 
 
sniff(prn=capture_packets, count=50)  # Capture 50 packets 
 
# Visualization 
ips = list(ip_count.keys()) 
counts = list(ip_count.values()) 
 
plt.figure(figsize=(10,5)) 
plt.bar(ips, counts, color='blue') 
plt.xticks(rotation=45) 
plt.xlabel("IP Addresses") 
plt.ylabel("Number of Packets") 
plt.title("IP Address Allocation Analysis") 
plt.show()

import ipaddress 
 
def classify_ip(ip): 
    ip_obj = ipaddress.ip_address(ip) 
    if ip_obj.is_private: 
        return "Private IP" 
    else: 
        return "Public IP" 
 
for ip in ip_count.keys(): 
    print(f"{ip}: {classify_ip(ip)}")
