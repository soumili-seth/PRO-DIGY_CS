import scapy.all as scapy
from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.layers.http import HTTP

def packet_callback(packet):
    
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        
        if packet.haslayer(TCP):
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif packet.haslayer(UDP):
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
        elif packet.haslayer(ICMP):
            protocol = "ICMP"
            src_port = ""
            dst_port = ""
        else:
            protocol = "Other"
            src_port = ""
            dst_port = ""
        
        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")
        print(f"Protocol: {protocol}")
        print(f"Source Port: {src_port}")
        print(f"Destination Port: {dst_port}")
        
        if packet.haslayer(HTTP):
            http_layer = packet.getlayer(HTTP)
            print(f"HTTP Method: {http_layer.fields['Method']}")
            print(f"HTTP Path: {http_layer.fields['Path']}")
        
        print("---------------------------")

def main():
    
    sniff_thread = scapy.Thread(target=scapy.sniff, kwargs={"prn": packet_callback, "store": False})
    sniff_thread.start()
    
    while True:
        print("1. Stop Sniffing")
        choice = input("Enter choice: ")
        
        if choice == "1":
            sniff_thread.stop()
            break

if __name__ == "__main__":
    main()