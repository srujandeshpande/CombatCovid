# combat_covid
The Combat Covid Application - http://combatcovid.herokuapp.com/   
Runs on Dart, Python, HTML, CSS and JavaScript  
## Meet the team:
Avinash - https://github.com/avinash-vk  
Sanskriti - https://github.com/sanskritip  
Venkat R - https://github.com/Venkatavaradan-R  
Srujan - https://github.com/srujandeshpande  


## How to talk to the backend:

The API Calls are listed as follows  [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/2ab0b8dff3424f432704)

### /cognitive_face/<path:filename>   
Method: GET/POST  
Request: Empty  
Return: Displays the image at url  

### /api/qma_face   
Method: POST  
Request: Image, phone number  
Return: Authenticates image  

### /
Method: GET/POST  
Request: Empty  
Return: EMA Login Page  

### /ema_logout  
Method: GET/POST  
Request: Empty  
Return: EMA Login Page  
Also removes the current user from Session  

### /ema_login
Method: POST  
Request: Form data from EMA Login HTML Page  
```
{
    "phone_number": number,
    "password": password
}
```
Return: Shows the corresponding dashboard according to user level  

### /ema_dashboard
Method: GET/POST  
Request: Empty  
Return: Dashboard if logged in, else login page  

### /ema_add_new_user_page
Method: GET/POST  
Request: Empty  
Return: Add new user page  

### /ema_new_user_data
Method: POST  
Request: Message  
Return: Add new user page  

### /api/hardcoded_data
Method: GET/POST  
Request: Empty  
Return:
```JSON
{
    "_id": {
        "$oid": "5e79fe0d1c9d440000ab3594"
    },
    "gps_frequency": "30 Minutes",
    "picture_frequency": "6 Hours",
    "temperature_frequency": "2 Hours"
}
```
returns all the required frequency data  


### /api/ema_app_login
Method: POST  
Request: phone_number and password
```JSON
{
    "phone_number": number,
    "password": string
}
```
Return:
```JSON
{
    "success": boolean,
    "ema_role": string
}
```
success tells if the ema user logged in or not  

### /api/cma_add_location

### /api/cma_login
Method: POST  
Request: phone_number and password  
```JSON
{
    "phone_number": number,
    "password": string
}
```
Return:
```JSON
{
    "success": boolean
}
```
success tells if the user was successfully logged in or not  

### /api/qma_login
Method: POST  
Request: phone_number and password  
```JSON
{
    "phone_number": number,
    "password": string
}
```
Return:
```JSON
{
    "success": boolean
}
```
success tells if the user was successfully logged in or not  

### /api/cma_add_new_user
Method: POST  
Request: Takes name, phone number, date,
```JSON
{
    data
}
```
Return:
```JSON
{
    "success": boolean,
    "userobjid": object (string)
}
```
success tells if the user was successfully added or not  
userobjid return the object ID (as a string) if successfully added


### /api/add_new_user_qma
Method: POST  
Request: Takes name, phone number, date,
```JSON
{
    "first_name": string,
    "last_name": string,
    "currently_under_quarantine": boolean,
    "date_time_quarantined": datetime,
    "phone_number": number,
}
```
Return:
```JSON
{
    "success": boolean,
    "userobjid": object (string),
    "password": string
}
```
success tells if the user was successfully added or not  
userobjid return the object ID (as a string) if successfully added
password is password for user


### /api/add_new_user_data_qma
Method: POST  
Request: Rest of the User Data as JSON  
```JSON
{
    "phone_number": number,
    "dob": date,
    "email_address": string,
    "home_coordinates": string,
    "address": string,
    "city": string,
    "state": string,
    "pincode": number
}
```
Return:
```JSON
{
    "success": boolean
}
```
success tells if the user was successfully added or not  
userobjid return the object ID (as a string) if successfully added

### /api/add_new_checklist
Method: POST  
Request: Test Data as JSON  
```JSON
{
    data taken from checklist
}
```
Return:
```JSON
{
    "success": boolean,
    "checklistobjid": object (string)
}
```
success tells if the test data was added successfully   
checklistobjid gives the object ID (as string) of the checklist added  

### /api/add_new_test
Method: POST  
Request: Test Data as JSON  
```JSON
{
    "phone_number": string,
    "date_time": datetime,
    "test_result": boolean,
    "other_data": string
}
```
Return:
```JSON
{
    "success": boolean,
    "testobjid": object (string)
}
```
success tells if the test data was added successfully   
testobjid gives the object ID (as string) of the test if successfully added  

### /api/add_close_contact
Method: POST  
Request: Contact Data as JSON  
```JSON
{
    "user_id": object (string),
    "contact_name": string,
    "contact_phone": number,
    "contact_user_id": string,
    "contact_other_info": string
}
```
Return:
```JSON
{
    "success": boolean,
    "ccobjid": object (string)
}
```
success tells if the close contact data was added successfully   
ccobjid gives the object ID (as string) of the record added  

### /api/add_new_distress_call

### /api/add_new_temperature
Method: POST  
Request: Temperature Data as JSON  
```JSON
{
    "user_id": object (string),
    "date_time": datetime,
    "temperature": number,
    "additional_info": string
}

```
Return:
```JSON
{
    "success": boolean,
    "tempobjid": object (string)
}
```
success tells if the temperature data was added successfully   
tempobjid gives the object ID (as string) of the record added  

### /add_new_chc
Method: POST  
Request: CHC Data as JSON  
```JSON
{
    "name": string,
    "phone_number": number,
    "district": string,
    "state": string
}

```
Return:
```JSON
{
    "success": true,
    "chcobjid": object (string)
}
```
```JSON
{
    "success": false,
    "error": string
}
```
success tells if the CHC was added successfully   
chcobjid gives the CHC ID (as string) if added  

### /add_new_phc
Method: POST  
Request: PHC Data as JSON  
```JSON
{
    "chc_id":string,
    "chc_phone_number":number,
    "name": string,
    "phone_number": number,
    "district": string,
    "state": string
}

```
Return:
```JSON
{
    "success": true,
    "phcobjid": object (string)
}
```
```JSON
{
    "success": false,
    "error": string
}
```
success tells if the PHC was added successfully   
phcobjid gives the PHC ID (as string) if added  
