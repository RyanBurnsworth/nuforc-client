import urllib2
from storeData import StoreData
from bs4 import BeautifulSoup

# scrapes the data from the webpage's table
class Scraper:
	sData = StoreData()
	def __init__(self, baseURL):
		self.scrapeURL(baseURL)
		self.sData = StoreData()

	def scrapeURL(self, baseURL):
		page = urllib2.urlopen(baseURL)
		soup = BeautifulSoup(page, 'html.parser')
		data = []

		# we will only scrape the rows that are highlighted on the website
		data = soup.find_all('td', attrs={'bgcolor': '#FFFFCC'})
		
		print "[*] Total Number Of Sightings Scraped: " + str(len(data))

		for d in data:
			self.sData.parseSightingsData(d)
