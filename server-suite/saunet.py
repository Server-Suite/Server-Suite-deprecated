import os,platform
def ip():
	os.system("ifconfig > data.ip")
	f=open("data.ip")
	for line in f:
		if "netmask" in line:
			data=line.strip()
	os.system("rm data.ip")
	f.close()
	data=data.split()
	data=[data[1],data[3]]
	return data
def gateway():
	os.system("route > data.ip")
	f=open("data.ip")
	data=f.read()
	data=data.split()
	os.system("rm data.ip")
	f.close()
	return data[20]
def get_os():
		temp=platform.linux_distribution()
		ver=[temp[0],temp[1]]
		return ver
def hostname():
	host=os.popen("hostname").read().strip()
	user=os.popen("whoami").read().strip()
	data=[user,host]
	return data
def status(service):
	cmd="systemctl status "+str(service)
	status=os.popen(cmd).read()
	if "active" in status and "running" in status:
		return "active"
	elif "inactive" in status and "dead" in  status:
		return "inactive"