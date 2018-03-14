import os,time,thread
class cpu():
    def status(self):
        a=0
        try:
            while a!=100:
                os.system("date > data.txt")
                os.system("mpstat -P ALL >> data.txt")
                os.system("free -m >> data.txt")
                time.sleep(2)
                a+=1
        except KeyboardInterrupt:
            sys.exit()
    def __init__(self):
        thread.start_new_thread(self.status  ,())
        try:
            os.system("python -m SimpleHTTPServer 12345")
        except KeyboardInterrupt:
            sys.exit()