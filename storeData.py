import urllib
import urllib2
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
from sightingData import SightingData
from config import Config

# stores each sighting record from NUFORC.org's database on our server
class StoreData:
	def __init__(self):
		self.config = Config()
		self.counter = 0
		self.totalCount=0

		sightingData = SightingData()
		self.sightingDataList = sightingData.getSightingDataList()

	# parses each sighting record and stores data in a dictionary
	# once dictionary is populated the record is sent to the database
	def parseSightingsData(self, dataObjs):
		geolocator = Nominatim(user_agent=self.config.getName())
		city = ""
		state ="" 	

		# Each block of sighting data from the NUFORC website contains 7 elements
		# GeoPy is used to obtain the longitude, latitude and thorough address from each block
		for dataObj in dataObjs:
			if (self.counter==0):
				self.sightingDataList["DateTime"] =  dataObj.text.strip()
			elif (self.counter==1):
				self.sightingDataList["City"] = dataObj.text.strip()
				city = dataObj.text.strip()
			elif (self.counter==2):
				state = dataObj.text.strip()
				self.sightingDataList["State"] = state
				
				# geopy thinks CA is Canada when transforming to an address
				if state == "CA":
					state = "California"

				location = geolocator.geocode(city + ", " + state)
				if (location != None):
					try:
						self.sightingDataList["Longitude"] = str(location.longitude)
						self.sightingDataList["Latitude"] = str(location.latitude)
						self.sightingDataList["Location"] = str(location.address)
					except UnicodeEncodeError:
						self.sightingDataList["Location"] = ""
			elif (self.counter==3):
				self.sightingDataList["Shape"] = dataObj.text.strip()
			elif (self.counter==4):
				self.sightingDataList["Duration"] = dataObj.text.strip()
			elif (self.counter==5):
				self.sightingDataList["Summary"] = dataObj.text.strip()
			elif (self.counter==6):
				self.sightingDataList["Posted"] = dataObj.text.strip()
				self.counter=-1
				self.totalCount += 1

				print "[*] Storing Sighting Record Number: " + str(self.totalCount)
				self.storeSightingsData()

			self.counter += 1

	# generate a url encoded query from the dictionary
	def createQueryURL(self):
		return  urllib.urlencode(self.sightingDataList)
				
	# send the record to the server to be stored
	def storeSightingsData(self):
		FULL_URL = self.config.getServerURL() +  self.createQueryURL()

		if (self.filterSightingData()):
			urllib2.urlopen(FULL_URL).read()

	# filter out records with no longitude, latitude, summary or summary is just "MADO"
	def filterSightingData(self):
		if self.sightingDataList["Longitude"] == "":
			return False
		elif self.sightingDataList["Latitude"] == "":
			return False
		elif "MADO" in self.sightingDataList["Summary"]:
			return False
		elif self.sightingDataList["Summary"] == "":
			return False
		return True
