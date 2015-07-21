# sensorDataGen.py generates random data for dandelion / sunflower and write to a text file 
# TODO: 
#  - need to generate sunflower data properly
#  - write more logic to generate sensible data 

from random import randint
import random 
import time
import threading

def timer():
	threading.Timer(5.0, dataGenerator).start()
	print('timer going')

def dataGenerator():
	date = time.asctime( time.localtime(time.time()))
	dandelionID = randint(0,20) #20 dandelions
	sunflowerMAC = randint(0,5) #5 sunflowers
	state = random.choice(["true", "false"])
	airTemp = randint(21,32)
	humidity = randint(0,100)
	soilTemp1 = randint(12,32)
	soilTemp2 = randint(12,32)
	soilTemp3 = randint(12,32)
	mois1 = randint(0,100)
	mois2 = randint(0,100)
	mois3 = randint(0,100)
	batteryLevel = randint(0,100)
	irradiance = randint(0,100)
	timer()

	#write to file 
	with open("sensorData.txt", "a") as myfile:
	    myfile.write("\n"+str(date)+","+str(dandelionID)+","+str(sunflowerMAC)+","
	    	+str(state)+","+str(airTemp)+","+str(humidity)+","+str(soilTemp1)+","
	    	+str(soilTemp2)+","+str(soilTemp3)+","+str(mois1)+","+str(mois2)+","
	    	+str(mois3)+","+str(batteryLevel)+","+str(irradiance))

timer() 