import subprocess
from termcolor import colored

fname = "hostlists.txt"
fdnsnum = "/home/locpv/site-hacky/tada/dnsenum.pl"
fdnstext = "/home/locpv/site-hacky/tada/dns.txt"
ffierce = "/home/locpv/site-hacky/tada/fierce.pl"

with open(fname) as f:
	ips = f.readlines()

for ip in ips:
	ip = ip.strip()
	print colored('=======%s' %ip,'red')
	subprocess.call(['dig', ip])
	subprocess.call(['perl', fdnsnum, '--enum', '-f', fdnstext, '--update', 'a', '-r', ip])
	subprocess.call(['dnstracer', ip])
	subprocess.call([ffierce, '-dns', ip])
	subprocess.call(['nmap', '-PN', '-n', '-F', '-T4', '-sV', '-A', '--version-intensity', '5', ip])
	subprocess.call(['nmap', '--script', 'ssl-cert,ssl-enum-ciphers', '-p', '443,465,993,995', ip])
