# this script generates initial arbitrary number of dandelion & sunflower info 
# To run this: python hardwareGen.py
# TODO 
# - specify serial number
# - open for user input

from random import randint
import random 
import time
import datetime
import threading

#output location 
dandOutput = "output/dandelionDeviceInfo.txt"
sunfOutput = "output/sunflowerDeviceInfo.txt"

#init dandelion
dandelion = {}
dandNum = 28
dandLocationLat = [ 36.788219,
 36.770345,
 36.755768,
 36.731283, 
 36.718075,
 36.701010,
 36.682015,
 36.767045,
 36.752742,
 36.741188,
 36.709543,
 36.682290,
 36.782170,
 36.753018,
 36.734035,
 36.714772,
 36.688898,
 36.785745,
 36.757419,
 36.737887,
 36.691100,
 36.785745,
 36.759344,
 36.716423,
 36.685319,
 36.771171,
 36.730183,
 36.683391]
dandLocationLon = [-119.586868,
-119.602661,
-119.572792,
-119.608841,
-119.566269,
-119.616737,
-119.595451,
-119.526443,
-119.549103,
-119.525070,
-119.525070,
-119.535370,
-119.462585,
-119.487648,
-119.464645,
-119.483185,
-119.487991,
-119.411774,
-119.414177,
-119.375725,
-119.417610,
-119.351692,
-119.354782,
-119.371948,
-119.368858,
-119.311867,
-119.321136,
-119.302254]


#init sunflower
sunflower = {}
sunfNum = 5
sunfLocationLat = [ 36.762645,
 36.702111,
 36.735135,
 36.768970,
 36.683116]
sunfLocationLon = [-119.550133, 
-119.504814, 
-119.414864, 
-119.281311, 
-119.275475 ]


class Dandelion: 

	def __init__(self, dandID, lat, lon, firmVersion, created_at):
		self.dandID = dandID
		self.lat = lat
		self.lon = lon
		self.firmVersion = firmVersion
		self.created_at = created_at

	def showDandID(self):
		return self.dandID #print Dandelion ID 


	def showFirmVersion(self):
		return self.firmVersion

	def showCreateDate(self):
		return self.created_at


class Sunflower:

	def __init__(self, sunflowerID, lat, lon, firmVersion, created_at):
		self.sunflowerID = sunflowerID
		self.lat = lat
		self.lon = lon
		self.firmVersion = firmVersion
		self.created_at = created_at

	def showSunflowerID(self):
		return self.sunflowerID

	def showFirmVersion(self):
		return self.firmVersion

	def showCreateDate(self):
		return self.created_at

	def showIP(self):
		return self.ip

	def showMAC(self):
		return self.mac


def generateDandelion(dandNum):
	for x in range(1,dandNum):
		dandID =  x
		lat = dandLocationLat[x]
		lon = dandLocationLon[x]
		firmVersion = 1.0
		created_at = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
		dandelion[x] = Dandelion(dandID,lat, lon,firmVersion,created_at)

		with open(dandOutput, "a") as myfile:
		    myfile.write(str(dandID)+" "+str(lat)+" "+str(lon) + " "+str(firmVersion)+" "+str(created_at)+"\n")
	print('Dandelions Generated')


def generateSunflower(sunfNum):
	for x in range(1, sunfNum):
		sunflowerID = x
		lat = sunfLocationLat[x]
		lon = sunfLocationLon[x]
		firmVersion = 1.0
		created_at = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
		sunflower[x] = Sunflower(sunflowerID,lat,lon,firmVersion,created_at)

		with open(sunfOutput, "a") as myfile:
		    myfile.write(str(sunflowerID)+" "+str(lat)+" "+str(lon)+" "+str(firmVersion)+" "+str(created_at)+"\n")
	print('Sunflowers Generated \n')


#generate device information
generateDandelion(dandNum)
generateSunflower(sunfNum)
















