from checkLatest import CheckLatest
from scraper import Scraper

class NUFORCBOT:
	def __init__(self):
		self.checkLatest = CheckLatest()

	def startNUFORCBOT(self):
		print "[*] Starting NUFORC BOT ...\n\n"
		print "[*] Checking For Update...\n\n"
		
		if not self.checkLatest.shouldUpdate():
			print "[*] Currently Up to Date!"
		else:
			print "[*] Needs Update"
			print "[*] Downloading latest data"
			
			latestURL = self.checkLatest.getLatestURL()
			print "[*] Latest URL: " + latestURL
			scraper = Scraper(latestURL)

nuforcbot = NUFORCBOT()
nuforcbot.startNUFORCBOT()
 
		


