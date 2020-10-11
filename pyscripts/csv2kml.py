""" 
@author: achang-1 
"""

# pip install csv 
# pip install simplekml 
import csv
import simplekml

kml = simplekml.Kml() 
# open and read the .csv file of responses with .DictReader()  
with open ("communityresources - Form Responses.csv", newline = '', encoding='utf-8') as f: 
    csvinfo = csv.DictReader(f)
    
    # break file into rows 
    for rows in csvinfo: 
        # checks if there are resources 
        if(rows['What type of resource(s) do you have?']!=''):
            resourceName = rows['What type of resource(s) do you have?']
            latitude = rows['Where do you want to donate? (Latitude)']                 
            longitude = rows['Where do you want to donate? (Longitude)']
            #creates a new point in the KML file 
            kml.newpoint(name = resourceName, coords=[(latitude,longitude)]) 

#save file as a .kml to be integrated into the website
kml.save('localresources.kml')    
