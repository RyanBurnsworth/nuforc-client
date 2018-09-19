class SightingData:
	def __init__(self):
		self.sightingData = {
			"DateTime" : '',
			"City" : '',
			"State" : '',
			"Location" : '',
			"Longitude" : '',
			"Latitude" : '', 
			"Shape" : '',
			"Duration" : '',
			"Summary" : '',
			"Posted" : ''
		}

	def getSightingDataList(self):
		return self.sightingData
