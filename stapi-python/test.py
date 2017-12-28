import urllib.request
import json

class AstronomicalObject:
	def __init__(self, uid):
		self.fetchedPage = urllib.request.urlopen("http://stapi.co/api/v1/rest/astronomicalObject?uid=" + str(uid))
		self.jsonData = json.loads(str(self.fetchedPage.readlines()[0].decode("UTF-8")))
		for key, value in self.jsonData["astronomicalObject"].items():
			if type(value) is not dict:
				setattr(self, key, value)
		# print(dir(self))
		
loracus = AstronomicalObject("ASMA0000012319")
print(dir(loracus))