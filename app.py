from scapy.all import *

A = '192.168.0.101' # spoofed source IP address
B = '192.168.0.102' # destination IP address
C = 10000 # source port
D = 20000 # destination port
payload = "yada yada yada" # packet payload

spoofed_packet = IP(src=A, dst=B) / TCP(sport=C, dport=D) / payload
send(spoofed_packet)