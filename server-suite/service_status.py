import os
def get_status():
	service=["ftp","ssh","apache","http"]
	data=os.popen("service --status-all").read().split("\n")
	for i in service:
		#print data
		for j in data:
			if i in j:
				print i+"\t"+j	
get_status()