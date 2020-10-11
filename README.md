# COVID on the Block  
Repository for the [sunhacks](https://sunhacks2020.devpost.com/) hackathon project (Oct. 9-11, 2020)! 

Website: https://covidontheblock.org (This works for now: http://dbllznd2wlj1v.cloudfront.net) 

Made (with love) by: 

- Albert Chang ([achang-1](https://github.com/achang-1)) 
  - Front-end 
  - Created .csv to .kml script in Python
  - Author of the README.me 
  - First hackathon!

- Thy Do ([thydo](https://github.com/thydo))
  - Front-end
  - Streamlined Sheets to XML file via Python script 
  - Also first hackathon! 

- and Hwan Kim ([JuanCarlos3](https://github.com/JuanCarlos3))!
  - AWS overlord 
  - Community resources integration into AWS 
  - Also first hackathon! 

# Introduction 
Based on the sunhakcks [Devpost](https://sunhacks2020.devpost.com/), we used that to decide a theme for our project. It boiled down to doing something for the *common good* and to integrate it with *cloud technology* (AWS/Google Cloud). Taking an approach similar to how *carrd.co* sites were made (e.g. BLM, crises, social movements), resources were available, but not exactly map-able nor . People would often have to scroll through long docs, Twitter/Reddit/FB/(whatever you use) threads, or pages with links overflow, often resulting in harder-to-find resources that may be important or missed. 

Enter: [COVID on the Block.](https://covidontheblock.org) (This works for [now](http://dbllznd2wlj1v.cloudfront.net) until it's setup) 

# [Design](https://docs.google.com/document/d/1633ha0vAzMU699krRV_VgbRfDuGwovxLZ3KoVy5aeiw/edit?usp=sharing) 
Keeping minimalism in mind, we put everything someone may need during this pandemic into one central location. We mapped every single place in Maricopa to help point people to the resources they need: *foodstuffs, shelter, medical supplies, testing centers, emergency rooms, unemployment, and even **local community resources!*** This way, anyone wanting to find something can go onto our website and directly find and get the help they want and/or need. 

### Community Resources 

# How we built it 
We downloaded a HTML template and modified it to our categories. Each resource category is an image with an embed link which takes the user to the resource they need. The maps are then manually created and embedded for each category (when applicable). For the user input, we created a Google Form that collects user's resource(s) and preferred location via coordinates. The data is then converted into a XML file, which is then populated into Google Maps, embedded into the website. The website is then hosted on AWS, and we even got a domain name (coming soon)! 

# Technologies Used 
Frontend: HTML, CSS 

Backend: Python (Community Resources) 

Google - Sheets (our temporary database!), Forms (user input), Drive API (to get access to Sheets), Maps API (to show our Community Resources)

Amazon AWS: S3, Route 53, Cloudfront (website host), Lambda (automation for Sheets data entry)


# Improvements and What's Next 
Our `Community Resources` tab can be improved upon by: 
- using something more practical for geolocation, such as addresses or zip codes. 
- adding descriptions and contact information (like where/when users are available, how many resources they have, etc.) 
- privacy and verification features (security reasons) 
- community ratings for approval/disapproval

Eventually, we hope to move our database to AWS's Aurora to scale and handle more user inputs from a custom-built form on our website. 

For now, our data is populated for Maricopa County (AZ), but we plan to scale this and take it to the next level. We hope to populate helpful resources to people in not only the United States, but also the rest of the world! We want to have users add new places onto the map as well (will be approved), which will help map the plot. 

We also want to add multiple languages to our website to accomodate everyone possible. We want to start with adding Spanish and Mandarin Chinese (the three most popular in the U.S.), and eventually, more languages for the rest of the world!  

# Acknowledgements
Thank you to sunhacks for hosting this hackathon virtually! The organizers, mentors, MLH, and everyone who planned this hackathon.  
Last but not least, thanks Kevin from MLH! (does this qualify for swag ;)) ~and Red Bull for keeping me awake~  
