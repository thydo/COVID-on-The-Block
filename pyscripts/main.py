import gspread
from simplekml import Kml

gc = gspread.service_account(filename = "credentials.json")
sh = gc.open_by_key('12zEDmifmfdcECMwoQdldpZAe7Asshow7cUzRyWF-uRI')
worksheet = sh.sheet1
res = worksheet.get_all_values()

kml = Kml(name='resources')
for n in res[1:]: #skip the first index and ignore the Nos
    if (n[1]!='No'):
        kml.newpoint(name=n[2],coords=[(n[3],n[4])])

kml.save("KmlClass.kml")  # Saving

print(res)
