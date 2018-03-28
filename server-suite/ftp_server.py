#!/usr/bin/python
#coded by saurabh_londhe
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import thread,time,os,sys
ip=""
port=888
path=sys.argv
def title():
	i=0
	s="server is ready script written by Saurabh londhe"
	while True:
		if i==len(s):
			i=0
		#"\033["+num+"m"+s+"\033[0m"
		print "\033[31m"+s[0:i]+s[i].upper()+s[i+1:]+" FTP ip ' ftp://"+str(ip)+":"+str(port)+"'\033[0m"
		i+=1
		time.sleep(0.05)
		os.system("clear")
#-------------------------FTP--------------------------------------------
def start_ftp():
	authorizer = DummyAuthorizer()
	authorizer.add_anonymous(path[1], perm="elradfmw")
	#authorizer.add_user("toretto", "toor", "/root/", perm="elradfmw")
	#authorizer.add_user("user", "pass", "/home", perm="elradfmw")
	handler = FTPHandler
	handler.authorizer = authorizer
	global ip,port
	ip=get_ip()
	server = FTPServer((ip,port), handler)
	server.serve_forever()
	return ip,port

#-------------------------GET-IP-------------------------------------------
def get_ip():
	os.system("ifconfig > data.txt")
	f=open("data.txt")
	for i in f:
		if "inet " in i:
			#print i
			s=i
	global ip
	os.system("rm -rf data.txt")
	ip=s[13:27]
	return ip.strip()
#---------------------------------------------------------------------
def start():
	get_ip()
	thread.start_new_thread(title,())
	#thread.start_new_thread(start_ftp,())
	start_ftp()
def kill_td():
	obj.kill()
	ob.kill()
start()