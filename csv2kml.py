# kml = simple.Kml()
# Location_name = "lolz"
# coordinate_1 = "18.432314"
# coordinate_2 = "-33.90862"
# kml.newpoint(name=Location_name, coords=[(coordinate_1,coordinate_2)])  # lon, lat, optional height
# kml.save("temp.kml")

import csv
import simplekml

kml = simplekml.Kml() 

with open ("communityresources - Form Responses.csv", newline = '', encoding='utf-8') as f: 
    csvinfo = csv.DictReader(f)

    
    for rows in csvinfo: 

        
        if(rows['Do you have any resources for the community?']=="Yes"):
            for push in rows:  
                print(push)
                resourceName = push['What type of resource(s) do you have?']
                latitude = push['Where do you want to donate? (Latitude)']                 
                longitude = push['Where do you want to donate? (Longitude)']
            kml.newpoint(name = resourceName, coords=[(latitude,longitude)]) 

kml.save('localhelp.kml')



    