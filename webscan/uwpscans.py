import subprocess
import os


def wepscan():
	fname = "urls.txt"
	outFile = open("outputfile.txt",'w')

	with open(fname) as f:
		urls = f.readlines()
	for url in urls:
		subprocess.call(['sudo', 'wpscan', '--url', url.strip(), '--enumerate', 'u', '--follow-redirection'])

wepscan()
	
