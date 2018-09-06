import subprocess
import os

fname = "url.txt"

with open(fname) as f:
	urls = f.readlines()

for url in urls:
	subprocess.call(['sudo', 'wpscan', '--url', url.strip()])


