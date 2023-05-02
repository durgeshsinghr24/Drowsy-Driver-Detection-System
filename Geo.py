import requests
import json

send_url = "api_key"
geo_req = requests.get(send_url)
geo_json = json.loads(geo_req.text)
latitude = geo_json['latitude']
longitude = geo_json['longitude']
print("Live location link:- "+"https://www.google.com/maps/place/"+str(latitude)+','+str(longitude))
