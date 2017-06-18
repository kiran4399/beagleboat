import os,datetime,time


k=int(input())

if (k==5):
	idd = 1
#	name=datetime.datetime.now().strftime("%d-%B-%Y")+time.strftime("%I:%M:%S")+str(idd)".jpg"
	while (1):
		name=datetime.datetime.now().strftime("%d-%B-%Y")+time.strftime("%I:%M:%S")+".jpg"
		imgname = name+".jpg"
		os.system("fswebcam  webcam/"+imgname)
		time.sleep(1)
		idd+=1

