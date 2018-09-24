class Config:
	def __init__(self):
		self.NUFORC_UPDATE_URL = "http://www.nuforc.org/webreports/ndxpost.html"
		self.BASE_NUFORC_URL = "http://www.nuforc.org/webreports/ndxp"
		
		# Link To Your PHP/MySQL script
		self.SERVER_URL = "http://www.YOURDOMAINNAME.com/ufosightings/storeSightingRecord.php?"

		# Filename where the lasted date updated is stored
		self.LAST_UPDATED = "lastRead.txt"

		# Name of the NUFORC Bot
		self.NAME = "ALIENA"
		
	def getUpdateURL(self):
		return self.NUFORC_UPDATE_URL


	def getBaseURL(self):
		return self.BASE_NUFORC_URL

	def getServerURL(self):
		return self.SERVER_URL

	def getLastUpdated(self):
		return self.LAST_UPDATED

	def getName(self):
		return self.NAME
