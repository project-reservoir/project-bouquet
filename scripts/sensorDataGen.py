# sensorDataGen.py generates random data for dandelion / sunflower and write to a text file 
# TODO: 
#  - need to generate sunflower data properly
#  - write more logic to generate sensible data 

from random import randint
import random 
import time
import threading


dandelion = {}
dandNum = 2

class Dandelion: 

	counter = 0;

	def __init__(self, timestamp, dandID, status, airTemp, humidity, 
		soiltemp1, soiltemp2, soiltemp3,  mois1, mois2, mois3, batteryLevel):
		self.dandID = dandID
		self.status = status
		self.airTemp = airTemp
		self.humidity = humidity
		self.soiltemp = [soiltemp1, soiltemp2, soiltemp3]
		self.mois = [mois1, mois2, mois3]
		self.batteryLevel = batteryLevel

	def showDandID(self):
		return self.dandID

	def showStatus(self):
		return self.status
	def setStatus(self, s):
		self.status = s

	def showAirTemp(self):
		return self.airTemp

	def setAirTemp(self, t):
		self.airTemp = t

	def showHumidity(self):
		return self.humidity

	def showSoilTemp(self, num):
		return self.soiltemp[num]
		
	def showMois(self, num):
		return self.mois[num]

	def showBatteryLevel(self):
		return self.batteryLevel

	def setBatteryLevel(self, bl):
		self.batteryLevel = bl

	def showCounter(self):
		return self.counter

	def setCounter(self, c):
		self.counter = c

	# to be continued 

#initialize Dandelions
def generateDand(dandNum):
	status = 'on'
	airTemp = 12
	humidity = 20
	soiltemp1 = 18
	soiltemp2 = 18
	soiltemp3 = 18
	mois1 = 20
	mois2 = 20
	mois3 = 20
	batteryLevel = 100
	for i in range (0,dandNum):
		dandID = i
		created_at = time.asctime( time.localtime(time.time()))
		dandelion[i] = Dandelion(created_at, dandID, status, airTemp, 
			humidity, soiltemp1, soiltemp2, soiltemp3, 
			mois1, mois2, mois3, batteryLevel)
		print('Initialized: Dandelion ID:' + str(dandID) + ' BatteryLevel: ' + str(dandelion[i].showBatteryLevel()))

#determine which dandelion to update 
def updateDand(dandNum):
	#27 dandelions 
	num = randint(0,dandNum-1)
	return num

#generate sensor data for dandelion
def genDandSensorData(id):
	print('Dandelion' + str(id) + ' is to be updated' )
	d = dandelion.get(id) #get particular dandelion
	counter = d.showCounter()
	if counter >12:
		counter = 0 #reset counter
	batteryLevel = d.showBatteryLevel()
	status = d.showStatus()
	air = d.showAirTemp()

	# batterlevel
	randnum = randint(0,1) #for battery decrement
	if randnum == 1:
		batteryLevel = batteryLevel - randint(1,5)
	
	# state
	if batteryLevel < 5:
		status= 'false'
	else: 
		status = 'on'

	#air temperature 
	if counter < 5: 
		air = air + randint(0,4)
	elif counter in range(5,9):
		air = air + randint(-2, 2)
	else:
		air = air - randint(0,4)

	#setting values 
	d.setBatteryLevel(batteryLevel)
	d.setStatus(status)
	d.setAirTemp(air)
	d.setCounter(counter+1)

	print('Dandelion' + str(id) + ' BatteryLevel: ' + str(batteryLevel) + ' Status: ' + str(status)
		+ 'AirTemperature: ' + str(air))



	# airTemp = randint(21,32)
	# humidity = randint(0,100)
	# soilTemp1 = randint(12,32)
	# soilTemp2 = randint(12,32)
	# soilTemp3 = randint(12,32)
	# mois1 = randint(0,100)
	# mois2 = randint(0,100)
	# mois3 = randint(0,100)
	# batteryLevel = randint(0,100)
	# irradiance = randint(0,100)

	#write to file 
	# with open("sensorData.txt", "a") as myfile:
	#     myfile.write("\n"+str(date)+","+str(dandelionID)+","+str(sunflowerMAC)+","
	#     	+str(state)+","+str(airTemp)+","+str(humidity)+","+str(soilTemp1)+","
	#     	+str(soilTemp2)+","+str(soilTemp3)+","+str(mois1)+","+str(mois2)+","
	#     	+str(mois3)+","+str(batteryLevel)+","+str(irradiance))

	time.sleep(2) #delay for generating next round of data 
	runGenerator()



def runGenerator():
	#generate data every 5 seconds
	dandNumber = updateDand(dandNum)
	genDandSensorData(dandNumber)	

#run class
generateDand(dandNum) 
runGenerator()
