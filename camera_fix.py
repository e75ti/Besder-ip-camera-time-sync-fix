from dvrip import DVRIPCam
from time import sleep
from sys import exit

host_ip = 'XXX'	#Insert_the_ip_here

cam = DVRIPCam(host_ip, user='admin', password='')
if cam.login():
        cam.login()
        #print("conencted!")
        cam.set_time()		#synchronizes_time_with_local_server_time
        #print("time set!")
        cam.close()
        #print("closed cam!")
else:
        print("exiting!")
        exit()

#print("Camera time:", cam.get_time())

# Reboot camera
#cam.reboot()
#sleep(60) # wait while camera starts

# Login again
#cam.login()
# Sync camera time with PC time
#cam.set_time()
# Disconnect
#cam.close()
