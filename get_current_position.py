import urllib2
import json
from  LatLongUTMconversion import * 

def get_iss_position():
	req = urllib2.Request("http://api.open-notify.org/iss-now.json")
	response = urllib2.urlopen(req)
	obj = json.loads(response.read())
	return obj['iss_position']['latitude'], obj['iss_position']['longitude']


lat, lng = get_iss_position()
lat = float(lat)
lng = float(lng)
#print lat,lng
(z, e, n) = LLtoUTM(23,lat, lng)
print "ISS position => " + z
