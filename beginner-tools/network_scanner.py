import argparse
import scapy.all as scapy

def scan(ip):
	req = scapy.ARP(pdst = ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	req_broadcast = broadcast/req
	answered = scapy.srp(req_broadcast, timeout=1, verbose=False)[0]
	print("IP Address\t\tMAC Address")
	print("-----------------------------------------")
	clients = []
	for i in answered:
		clients.append({"ip":i[1].psrc, "mac": i[1].hwsrc})
	
	for client in clients:
		print(client['ip'] + "\t\t" + client['mac'])
	
	
def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-t', '--target', dest='ip', help='Target IP address of scan')
	options = parser.parse_args()
	
	if not options.ip:
		parser.error("[-] Please specify the target IP address")
	return options
	

options = get_args()

scan(options.ip)