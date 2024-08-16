from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

# Function to process each captured packet
def process_packet(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        # Determine the protocol
        if protocol == 6:
            proto_name = "TCP"
        elif protocol == 17:
            proto_name = "UDP"
        elif protocol == 1:
            proto_name = "ICMP"
        else:
            proto_name = "Other"

        # Display relevant information
        print(f"Source IP: {ip_src}")
        print(f"Destination IP: {ip_dst}")
        print(f"Protocol: {proto_name}")

        # Check if there's a payload and display the first 50 bytes
        if packet.haslayer(Raw):
            print(f"Payload: {packet[Raw].load[:50]}")
        print("=" * 50)

# Function to start the packet sniffer
def start_sniffer(interface):
    print(f"Starting packet sniffer on {interface}...")
    sniff(iface=interface, prn=process_packet, store=False)

# Main function
if __name__ == "__main__":
    # Specify the network interface you want to sniff on (e.g., 'eth0', 'wlan0')
    network_interface = input("Enter the network interface that you want to sniff:   ")
    start_sniffer(network_interface)