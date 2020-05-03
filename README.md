# combat_covid
Combat Covid, A complete Quarantine, Effort and Citizen management system  
The Combat Covid Application - **http://combatcovid.herokuapp.com/**     
Runs on Dart, Python, HTML, CSS and JavaScript  
Tech Stack used: Flutter, MongoDB, Flask

## Meet the team: Peace_Penguins (Theme: Social Impact)
Avinash - https://github.com/avinash-vk  
Sanskriti - https://github.com/sanskritip  
Venkat - https://github.com/Venkatavaradan-R  
Srujan - https://github.com/srujandeshpande  

## Introduction:
This is project consists of 3 distinct but interlinked components leadaing to a complete Quarantine Management System  
1. **Quarantine Management Application (QMA)**  
The QMA is intended to be installed on Quarantined Individual's mobile phones. The application records user data such as Temperature, Location, Face, etc. on a regular basis to ensure that the user is safely quarantined at home. 
2. **Effort Management Application (EMA)**  
The EMA is a complete management system for quarantined citizens. It consists of a web dashboard and mobile application.
The online dashboard is used to get an overview of all the users currently using the QMA and CMA.
It allows officers to view data related to all the users along with any alerts raised by these users.
The EMA mobile application is intended to be used by field officers. Using this application, new quarantined individuals can easily be added.
The mobile application also allows for easy alert addressing and checklist additions of quarantined individuals. 
3. **Citizen Management Application (CMA)**  
The CMA is a mobile applccation to be downloaded by regular citizens. Using this application, they can recieve easy alerts from government officials regarding
safety precautions and notifications. Users are also shown a map of prior cases and regions of high people concentration to avoid.
If a citizen is feeling symptoms or has come in contact with a positive tested patient, they can request a checkup directly from the application.  

## Demo Links:  
* Effort Management Dashboard: http://combatcovid.herokuapp.com/  
* Demo of Apps Working Together: https://www.youtube.com/watch?v=3LwioGyqC5U  
* Quarantine Management Application Demo: https://www.youtube.com/watch?v=jrIny_79h9M&t=1s  
* Effort Management Dashboard Demo: https://www.youtube.com/watch?v=icGMVfdH27M&t=1s  
* Effort Management Mobile Application Demo: https://www.youtube.com/watch?v=fr9Ywrnntr8  
* Citizen Management Application Demo: https://www.youtube.com/watch?v=5Tqprt7-Mis&t=3s  
* Link to Android Applications: https://drive.google.com/drive/folders/1QmAJedbKEPpvfUOPeQEBHeCsbjSZhVjU  

## How to use:
* The QMA, EMA and CMA Android applications can be downloaded from the above link  
* The EMA online dashboard can be viewed at http://combatcovid.herokuapp.com/ 

## The filesystem:
* The folder *Frontend* contains all the code related to the mobile applications. They are written using Flutter.  
* The folders *templates* and *static* contain all code related to the EMA online dashboard.  The use HTML, CSS and JavaScript.  
* The file *app.py* controls the backend. It is written in Python and uses Flask.  
* The database for the project is MongoDB and is stored on Azure using MongoDB Atlas.  

## Azure:
Microsoft Azure was an integral part of this project. The various Azure services used are:  
* Azure App Services for hosting
* Azure Cognitive Services for face verification
* Azure Maps for map integration
* MongoDB Atlas hosted on Azure for database

##### This was created for the Mishmash 2020 and Goverment of Jharkhand Covid-19 Hackathon
