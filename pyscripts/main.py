import gspread
from simplekml import Kml

gc = gspread.service_account(filename = "credentials.json")
sh = gc.open_by_key('12zEDmifmfdcECMwoQdldpZAe7Asshow7cUzRyWF-uRI')
worksheet = sh.sheet1
res = worksheet.get_all_values()

kml = Kml(name='resources')
kml.newpoint(name="Kirstenbosch", coords=[(18.432314,-33.988862)])  # A simple Point
kml.newpoint(name="Kirsdfh", coords=[(18.8,-33.988862)])  # A simple Point
kml.save("KmlClass.kml")  # Saving