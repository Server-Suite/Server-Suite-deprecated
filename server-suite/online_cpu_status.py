import os,psutil
flag=True
cnt=0
initial_down = psutil.net_io_counters().bytes_recv
initial_up = psutil.net_io_counters().bytes_sent
while flag:
	now_down = psutil.net_io_counters().bytes_recv
	now_up = psutil.net_io_counters().bytes_sent
	download_speed = (now_down - initial_down)/1000
	upload_speed = (now_up - initial_up)/1000
	speed=str(download_speed)+"kb/"+str(upload_speed)+"kb"
	initial_down = now_down
	initial_up = now_up
	try:
		s=psutil.cpu_percent(interval=2,percpu=True)
		all_per=(s[0]+s[1]+s[2]+s[3])/4
		if cnt%60==0:
			mem =str(psutil.virtual_memory()).split("=")[3].split(",")[0]
			btry_status=os.popen("cat /sys/class/power_supply/BAT0/uevent").read().split("POWER_SUPPLY_CAPACITY=")[1].split("\n")[0]
		cnt+=1
		print s
		html="""
		

<html>
<head>
<meta http-equiv="refresh" content="1">
<title>System CPU usage</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="css/bootstrap.min.css">
<style>
div#saur{
	float: left;
}
</style>
</head>
<body style="background-color:black;">
<center><img src='images/logo-white.png' height="100" width="100">
<br>
<font size=5 face="calibri" color="white">Server-Suite</font>
</center>
<center>
<div class="progress" style="width:850px;">
  		<div class="progress-bar progress-bar-success progress-bar-striped" role="progressbar"
  			aria-valuenow="40" aria-valuemin="0" aria-valuemax="100" style="width:"""+str(all_per)+"""%">
    		"""+str(all_per)+"""% core 0
  		</div>
	</div>
<div id="header" style="width:800px;">
    <div id="saur">
   	<font>core 0</font>
    <div class="progress" style="width:350px;">
  		<div class="progress-bar progress-bar-success progress-bar-striped" role="progressbar"
  			aria-valuenow="40" aria-valuemin="0" aria-valuemax="100" style="width:"""+str(s[0])+"""%">
    		"""+str(s[0])+"""% core 0
  		</div>
	</div>
	<font>core 1</font>
	<div class="progress" style="width:350px;">
  		<div class="progress-bar progress-bar-success progress-bar-striped" role="progressbar"
  			aria-valuenow="40" aria-valuemin="0" aria-valuemax="100" style="width:"""+str(s[1])+"""%">
    		"""+str(s[1])+"""% core 1
  		</div>
	</div>
</div>

	<font>core 2</font>
	<div class="progress" style="width:350px;">
  		<div class="progress-bar progress-bar-success progress-bar-striped" role="progressbar"
  			aria-valuenow="40" aria-valuemin="0" aria-valuemax="100" style="width:"""+str(s[2])+"""%">
    		"""+str(s[2])+"""% core 2
  		</div>
	</div>
	<font>core 3</font>
	<div class="progress" style="width:350px;">
  		<div class="progress-bar progress-bar-success progress-bar-striped" role="progressbar"
  			aria-valuenow="40" aria-valuemin="0" aria-valuemax="100" style="width:"""+str(s[3])+"""%">
    		"""+str(s[3])+"""% core 3
  		</div>
	</div>


</div>

</body>
</html>"""
		with open("index.html","w") as f:
			f.write(html)
	except:
		flag=False

