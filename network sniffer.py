
# Import necessary modules from scapy
from scapy.all import sniff, DNSQR, DNS

# Create a set to store domains we've already seen (to avoid duplicates)
visited_domains = set()

# Define a function to handle each captured packet
def show_visited_websites(packet):
    # Check if the packet contains both DNS and DNS Query Record layers
    # Also check if it's a DNS query (qr=0 means query, qr=1 would be a response)
    if packet.haslayer(DNSQR) and packet.haslayer(DNS) and packet[DNS].qr == 0:
        # Extract the queried domain name and remove trailing dots
        domain = packet[DNSQR].qname.decode().strip(".")
        
        # Only print the domain if it's not already in our set (avoid duplicates)
        if domain not in visited_domains:
            visited_domains.add(domain)
            print(domain)

# Start sniffing packets:
# - filter: only capture UDP packets on port 53 (used for DNS)
# - prn: for each packet captured, call the show_visited_websites function
# - store=0: don't keep packets in memory (saves RAM)
sniff(filter="udp port 53", prn=show_visited_websites, store=0)


# Today i am learning while loops in python programming





              
 

        
       
       
           
       


       
    
    
    
 