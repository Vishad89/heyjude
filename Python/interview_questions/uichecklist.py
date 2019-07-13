import requests

def main():

	systemarr = {1: "zeno", 2: "socrates", 3: "plato", 4: "petra", 5: "gus", 6: "Solis", 7: "stella", 8: "rusty", 9: "wally"}
	UIarr = {"a": "all", "b": "jupyter", "c": "hue", "d": "systemManagement", "e": "metrics", "f": "oozie", "g": "hadoopApplicationTimelineServer", "h": "mesos", "i": "spark", "j": "marathon", "k": "YARNResourceManager", "l": "hadoopJobHistoryServer", "m": "HDFSNameNode"}


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
	print "**************************"

	checklist(System, UI)

def checklist(System, UI):

	if UI != "all":
		r = requests.head("http://" + System + "-login1.us.cray.com/" + UI)
	 	if (r.status_code == 200):
	 		print UI + "\033[1;32m : online \033[1;m"
	 	elif (r.status_code == 404): 
	 		print UI + "\033[1;31m : offline \033[1;m" 
	 	else:
	 		print UI + "\033[1;33m some other issues \33[1;m"
	else:		
		for key in UIarr:
			UI = UIarr[key]
			if UI != "all":
			 	r = requests.head("http://" + System + "-login1.us.cray.com/" + UI)
			 	if (r.status_code == 200):
			 		print UI + "\033[1;32m : online \033[1;m"
			 	elif (r.status_code == 404): 
	 				print UI + "\033[1;31m : offline \033[1;m"  
	 			else:
	 				print UI + "\033[1;33m some other issues \33[1;m"
