import requests

systemarr = {1: "zeno", 2: "socrates", 3: "plato", 4: "petra", 5: "gus", 6: "Solis", 7: "stella", 8: "rusty", 9: "wally"}
UIarr = {"a": "all", "b": "jupyter", "c": "hue", "d": "systemManagement", "e": "metrics", "f": "oozie", "g": "hadoopApplicationTimelineServer", "h": "mesos", "i": "spark", "j": "marathon", "k": "YARNResourceManager", "l": "hadoopJobHistoryServer", "m": "HDFSNameNode"}

def status_code(req, strng):

	rcode = req.status_code
	try:
		if (rcode == 200):
			print strng + " :\033[1;32m online \033[1;m" + str(rcode)
		elif (rcode == 404): 
			print strng + " :\033[1;31m offline \033[1;m" + str(rcode)
	 	#else:
	 	#	print strng + ":\033[1;33m some other issues \33[1;m" + str(rcode)
	 	print "-------------------------------------------------"
	except:
		print "failed to connect"

def checklist(System, UI):

	if UI != "all":
		r_head = requests.head("http://" + System + "-login1.us.cray.com/" + UI)
	 	#r = r_head.status_code
	 	status_code(r_head, UI)
	else:		
		for key in UIarr:
			UI = UIarr[key]
			if UI != "all":
			 	r_head = requests.head("http://" + System + "-login1.us.cray.com/" + UI)
			 	status_code(r_head, UI)


def main():


	print "System List"
	print "-----------------"
	print " 1: Zeno"
	print " 2: Socrates"
	print " 3: Plato"
	print " 4: Petra"
	print " 5: Gus"
	print " 6: Solis"
	print " 7: Stella"
	print " 8: Rusty"
	print " 9: Wally"
	print "------------------"

	systeminput = raw_input("Please enter a number from the list above to select the system: ")
	System = systemarr[int(systeminput)]

	print "UI Inventory"
	print "---------------------------------------------------"
	print " a: all "
	print " b: Jupyter"
	print " c: Hue"
	print " d: System Management"
	print " e: Grafana"
	print " f: Oozie"
	print " g: Hadoop Timeline Server"
	print " h: Mesos"
	print " i: Spark"
	print " j: Marathon"
	print " k: Yarn"
	print " l: Hadoop Job History Server"
	print " m: HDFS Namenode"
	print "---------------------------------------------------"



	UIinput = raw_input("Please select UI from the list: ")
	UI = UIarr[UIinput]
	print UI


	print ""
	print ""
	print System + " Staus of UIs " 

	checklist(System, UI)

if __name__ == "__main__":
	main()
