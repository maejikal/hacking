import subprocess
import optparse

def change_mac(interface, new):
	print("[+] Changing MAC Address for " + interface + " to " + new)

	subprocess.call(['ifconfig', interface, 'down'])
	subprocess.call(['ifconfig', interface, 'hw', 'ether', new])
	subprocess.call(['ifconfig', interface, 'up'])

def get_args():

	parser = optparse.OptionParser()

	parser.add_option("-i", "--interface", dest='interface', help='Interface to change its MAC Address')
	parser.add_option("-m", "--mac", dest='new', help='New MAC Address')
	(options, arguments) = parser.parse_args()
	
	if not options.interface:
		parser.error("[-] Please specify an interface, use --help for more info.")
	elif not options.new:
		parser.error("[-] Please specify a new mac, use --help for more info.")
	return options

options = get_args()

change_mac(options.interface, options.new)
# capturing the ifconfig result of running *ifconfig eth0*
res = subprocess.check_output(['ifconfig', options.interface]) # res is a byte object
print(res.decode())