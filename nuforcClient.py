from checkLatest import CheckLatest
from scraper import Scraper

class NUFORC_Client:
	def __init__(self):
		self.checkLatest = CheckLatest()

	def startNUFORC_Client(self):
		print "[*] Starting NUFORC Client ...\n\n"
		print "[*] Checking For Update...\n\n"
		
		if not self.checkLatest.shouldUpdate():
			print "[*] Currently Up to Date!"
		else:
			print "[*] Needs Update"
			print "[*] Downloading latest data"
			
			latestURL = self.checkLatest.getLatestURL()
			print "[*] Latest URL: " + latestURL
			scraper = Scraper(latestURL)

nuforcClient = NUFORC_Client()
nuforcClient.startNUFORC_Client()
 
		


