# COVID on the Block  
Repository for the sunhacks https://sunhacks2020.devpost.com/ hackathon project (Oct. 9-11, 2020)! 

Website: https://covidontheblock.org

Made (with love) by: 

- Albert Chang (achang-1) 

- Thy Do (thydo) 

- and Hwan Kim (JuanCarlos3)!

# Introduction 
Based on the sunhakcks Devpost (https://sunhacks2020.devpost.com/), we used that to decide a theme for our project. It boiled down to doing something for the *common good* and to integrate it with *cloud technology* (AWS/Google Cloud). Taking an approach similar to how *carrd.co* sites were made (e.g. BLM, crises, social movements), resources were available, but not exactly map-able nor . People would often have to scroll through long docs, Twitter/Reddit/FB/(whatever you use) threads, or pages with links overflow, often resulting in harder-to-find resources that may be important or missed. 

Enter: COVID on the Block. https://covidontheblock.org (This works for now: http://www.covidontheblock.com.s3-website-us-east-1.amazonaws.com/#) 

# Design 
Keeping minimalism in mind, we put everything someone may need during this pandemic into one central location. We mapped every single place in Maricopa to help point people to the resources they need: *foodstuffs, shelter, medical supplies, testing centers, emergency rooms, unemployment, and even **local community resources!*** This way, anyone wanting to find something can go onto our website and directly find and get the help they want and/or need. 

# Technologies Used 
Frontend: HTML, CSS 

Backend: Python (Community Resources) 

Google - Sheets (our temporary database!), Drive API (to get access to Sheets), Maps API (to show our Community Resources), Forms (user input) 

Amazon AWS: S3, Route 53, Cloudfront (website host), Lambda (automation for Sheets data entry)


# Improvements 
Our `Community Resources` tab can be improved upon by: 
- using something more practical for geolocation, such as addresses or zip codes. 
- adding descriptions and contact information (like where/when users are available, how many resources they have, etc.) 

Eventually, we hope to move our database to AWS's Aurora to scale and handle more user inputs from a custom-built form on our website. 

# Acknowledgements
Thank you to sunhacks for hosting this hackathon virtually! The organizers, mentors, MLH, and everyone who planned this hackathon for months. 
Last but not least, thanks Kevin from MLH! (does this qualify for swag ;))   
