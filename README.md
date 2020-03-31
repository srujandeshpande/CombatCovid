# combat_covid
Combat Covid, A complete Quarantine, Effort and Citizen management system  
The Combat Covid Application - **https://combat-covid.azurewebsites.net/**     
Runs on Dart, Python, HTML, CSS and JavaScript  

## Meet the team:
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

## How to use:
* The QMA, EMA and CMA android applications can be downloaded from the APK folder  
* The EMA online dashboard can be viewed at https://combat-covid.azurewebsites.net/ 

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
