# sensorDataGen.py generates random data for dandelion / sunflower and write to a text file 
# TODO: 
#  - need to generate sunflower data properly
#  - write more logic to generate sensible data 

from random import randint
import random 
import time
import threading


dandelion = {}
dandNum = 27

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

	def setHumidity(self,h):
		self.humidity = h

	def showSoilTemp(self, num):
		return self.soiltemp[num]
	def setSoilTemp(self, n1,n2,n3):
		self.soiltemp[0] = n1
		self.soiltemp[1] = n2
		self.soiltemp[2] = n3

	def showMois(self, num):
		return self.mois[num]

	def setMois(self, n1,n2,n3):
		self.mois[0] = n1
		self.mois[1] = n2		
		self.mois[2] = n3

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
	soiltemp1 = randint(18,20)
	soiltemp2 =  randint(18,20)
	soiltemp3 =  randint(18,20)
	mois1 = randint(15,25)
	mois2 = randint(15,25)
	mois3 = randint(15,25)
	batteryLevel = 100
	for i in range (0,dandNum):
		dandID = i
		created_at = time.asctime( time.localtime(time.time()))
		dandelion[i] = Dandelion(created_at, dandID, status, airTemp, 
			humidity, soiltemp1, soiltemp2, soiltemp3, 
			mois1, mois2, mois3, batteryLevel)
		print('Initialized: Dandelion ID:' + str(dandID) + ' BatteryLevel: ' + str(dandelion[i].showBatteryLevel()))
			#write to file 
		with open("sensorData.txt", "a") as myfile:
		    myfile.write(str(dandID) + " "
		    	+str(status)+" "+str(airTemp)+" " + str(humidity)+" "+
		    	str(soiltemp1) + " " + str(soiltemp2) + " " + str(soiltemp3)+" "+ 
		    	str(mois1) + " " + str(mois2) + " " + str(mois3)+" "+
		    	str(batteryLevel)+ "\n")

#determine which dandelion to update 
def updateDand(dandNum):
	#27 dandelions 
	num = randint(0,dandNum-1)
	return num

#generate sensor data for dandelion
def genDandSensorData(id):
	d = dandelion.get(id) #get particular dandelion
	counter = d.showCounter()
	if counter >12:
		counter = 0 #reset counter
	batteryLevel = d.showBatteryLevel()
	status = d.showStatus()
	air = d.showAirTemp()
	humidity = d.showHumidity()
	s1 = d.showSoilTemp(0)
	s2 = d.showSoilTemp(1)
	s3 = d.showSoilTemp(2)
	m1 = d.showMois(0)
	m2 = d.showMois(1)
	m3 = d.showMois(2)
	# batterlevel
	randnum = randint(0,1) #for battery decrement
	if randnum == 1:
		batteryLevel = batteryLevel - randint(1,4)
	
	# state
	if batteryLevel < 5:
		status= 'false'
	else: 
		status = 'on'

	if batteryLevel <= 0:
		batteryLevel = 100

	#all values moved by counter 
	if counter < 5: 
		air = air + randint(0,4)
		humidity = humidity + randint(0,20)
		s1 = s1 + randint(0,2)
		s2 = s2 + randint(0,2)
		s3 = s3 + randint(0,2)
		m1 = m1 + randint(0,10)
		m2 = m2 + randint(0,10)
		m3 = m3 + randint(0,10)

	elif counter in range(5,9):
		air = air + randint(-2, 2)
		humidity = humidity + randint(-10,10)
		s1 = s1 + randint(-1,1)
		s2 = s2 + randint(-1,1)
		s3 = s3 + randint(-1,1)
		m1 = m1 + randint(-5,5)
		m2 = m2 + randint(-5,5)
		m3 = m3 + randint(-5,5)
	else:
		air = air - randint(0,4)
		humidity = humidity -randint(10,20)
		s1 = s1 - randint(0,2)
		s2 = s2 - randint(0,2)
		s3 = s3 - randint(0,2)
		m1 = m1 - randint(0,10)
		m2 = m2 - randint(0,10)
		m3 = m3 - randint(0,10)


	if humidity <= 0:
		humidity = 0
	if air <= 0:
		air = 0

	#setting values 
	d.setBatteryLevel(batteryLevel)
	d.setStatus(status)
	d.setAirTemp(air)
	d.setCounter(counter+1)
	d.setHumidity(humidity)
	d.setSoilTemp(s1,s2,s3)
	d.setMois(m1,m2,m3)

	print('Counter: ' + str(counter) +
		' Dandelion' + str(id) + 
		' BatteryLevel: ' + str(batteryLevel) + 
		' Status: ' + str(status) + 
		' AirTemperature: ' + str(air) + 
		' Humidity: ' + str(humidity) +
		' Soil Temperature: ' + str(s1) + " " + str(s2) + " " + str(s3) + " " +
		' Moisture: ' + str(m1) + " " + str(m2) + " " + str(m3) + " ")

	#write to file 
	# with open("sensorData.txt", "a") as myfile:
	#     myfile.write(str(id) + " "
	#     	+str(status)+" "+str(air)+" " + str(humidity)+" "+
	#     	str(s1) + " " + str(s2) + " " + str(s3)+" "+ 
	#     	str(m1) + " " + str(m2) + " " + str(m3)+" "+
	#     	str(batteryLevel)+ "\n")

	time.sleep(10) #delay for generating next round of data 
	runGenerator()



def runGenerator():
	#generate data every 5 seconds
	dandNumber = updateDand(dandNum)
	genDandSensorData(dandNumber)	

#run class
generateDand(dandNum) 
runGenerator()
