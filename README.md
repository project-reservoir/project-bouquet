# project-bouquet
Web portion of project reservoir 

## Work to Date (July 22, 2015)
### Logstash
  In logstash/conf, there are a few configuration files written for different purposes. 
  - dandGen.conf 
  	Parses incoming Dandelion device information. It so far parses deviceID, location, firmware version, and created date 
  - sunflowerGen.conf
  	Similar purpose to previous parser but for sunflower 
  - dandelion-json-simple.conf
  	A simple parser that reads Json formatted files.  
  - readDand.conf
    Parse dandelion sensor data. 

### Data Generators 
 Since Bouquet is not hooked up to sunflower, there are a few scripts written to custom generate data to feed into Logstash. Under /script folder: 
 - hardwareGen.py
 	Generates device information for Sunflower and Dandelion
 - sensorDataGen.py
 	Generates Dandelion sensor data on a timer. 
In the script/output/ folder,  the two .txt files are the generated result, along with sensorData.txt in the /script folder 

####How the UI look like:

(July 22, 2015) 
  http://i.imgur.com/qjeu0f3.png
  http://i.imgur.com/4DGfc5t.png
  http://i.imgur.com/ULBiLDR.png

