import sys,os,deb_server_list,rpm_server_list
from PyQt4 import QtGui as qt
class server_list:
	def __init__(self):
		s=sys.argv
		rpm={"fedora","centos"}
		deb={"kali","ubuntu"}
		if s[1].lower() in rpm:
			ob=rpm_server_list.rpm_server_list()
			ob.show()
			#os.system("python rpm_server_list.py")
		elif s[1].lower() in deb:
			os.system("python deb_server_list.py")
o=server_list()
