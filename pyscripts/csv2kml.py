""" sample how-to make a KML 
    kml = simple.Kml()
    Location_name = "lolz"
    coordinate_1 = "18.432314"
    coordinate_2 = "-33.90862"
    kml.newpoint(name=Location_name, coords=[(coordinate_1,coordinate_2)])  # lon, lat, optional height
    kml.save("temp.kml")
"""

import csv
import simplekml

kml = simplekml.Kml() 

with open ("communityresources - Form Responses.csv", newline = '', encoding='utf-8') as f: 
    csvinfo = csv.DictReader(f)
    for rows in csvinfo: 
        if(rows['What type of resource(s) do you have?']!=''):
            resourceName = rows['What type of resource(s) do you have?']
            latitude = rows['Where do you want to donate? (Latitude)']                 
            longitude = rows['Where do you want to donate? (Longitude)']
            kml.newpoint(name = resourceName, coords=[(latitude,longitude)]) 

kml.save('localresources.kml')    
