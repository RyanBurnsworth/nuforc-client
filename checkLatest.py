import urllib2
import os
from bs4 import BeautifulSoup
from config import Config

# checks NUFORC.org to see if there are new records available
class CheckLatest:
	def __init__(self):
		self.config = Config()
		self.latestDate = ""

	# returns true if an update is available, false is up to date
	def shouldUpdate(self):		
		if not self.compareTimeStamps(self.getLatest(), self.getLastRead()):
			self.latestDate = self.getLatest()
			self.updateLastRead(self.latestDate)
			return True
		else:
			return False
	
	# check NUFORC.org for latest
	def getLatest(self):
		page = urllib2.urlopen(self.config.getUpdateURL())
		soup = BeautifulSoup(page, 'html.parser')

		# only records of interest use td on this page so we can scrape all of them
		latest = soup.find('td').text.strip()
		return latest
	
	# check our local last update
	def getLastRead(self):
		# check if file exists before attempting to read
		if os.path.isfile(self.config.getLastUpdated()):
			lastReadFile = open(self.config.getLastUpdated(), "r")
		else:
			return ""

		lastUpdate = lastReadFile.read()
		lastReadFile.close()
		return lastUpdate

	# update our local last update storage
	def updateLastRead(self, lastRead):
		lastReadFile = open("lastRead.txt", "w")
		lastReadFile.write(str(lastRead))
		lastReadFile.close()

	# compare local and remote latest updates
	def compareTimeStamps(self, timeStamp1, timeStamp2):
		if timeStamp1 == timeStamp2:
			return True
		else:
			return False

	# return the url using the correct date format of the latest records
	def getLatestURL(self):
		return self.config.getBaseURL() + self.latestDate[8:] + self.latestDate[:2] + self.latestDate[3:5] + ".html"
