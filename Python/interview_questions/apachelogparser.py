
#!/usr/local/bin/python

"""
USAGE:

apachelogparser.py apache_log_file

This script takes apache log file as an argument and then generates a report, with hostname,
bytes transferred and status

"""

from collections import defaultdict
import sys


def apache_log_parser(file):
	
	try:
		log_file = open(file, 'r')
	except:
		print("invalid file")
		print(__doc__)
		sys.exit(1)


	log_parse=defaultdict(list)

	for line in log_file:
		line=line.replace('[','').replace(']','').replace('\"','').replace('-','').split()
		log_parse["ipaddr"].append(line[0])
		log_parse["status"].append(line[-2])
		log_parse["data_transfer"].append(line[-1])

	#log_parse["ipaddr"] = set(log_parse["ipaddr"])

	for k in log_parse:
		print(k," : ", log_parse[k])
	

if __name__=="__main__":

	if not len(sys.argv) > 1:
		print (__doc__)
		sys.exit(1)
	infile = sys.argv[1]
	apache_log_parser(infile)



# line1="64.242.88.10 - - [07/Mar/2004:16:05:49 -0800] GET /twiki/bin/edit/Main/Double_bounce_sender?topicparent=Main.ConfigurationVariables HTTP/1.1 401 12846"

#print(apache_log_parser("apache_test.log"))