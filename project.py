#importing modules
import phonenumbers
import opencage
import folium
#user defined module
from phonenum import number
from phonenumbers import geocoder

# to find the approxiamate location
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber,"en")
print(location)
from phonenumbers import carrier
# To find service provider
service_pro = phonenumbers.parse(number)
#selecting language for output
print(carrier.name_for_number(service_pro,"en"))

from opencage.geocoder import OpenCageGeocode
#key from opencagedata.com
key = 'b53702f927de494b8d8e29eff838c38e'
geocoder= OpenCageGeocode(key)
#converting location to string
query = str(location)
results =  geocoder.geocode(query)
#print(results)
#extracting latitudnal and longitudinal coordinates
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)
#finding location on maps 
#set zoom value to 9 when the site is opened
myMap= folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)
#creating new file where location of the number will be stored
myMap.save("location.html")