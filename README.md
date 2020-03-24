# combat_covid
Covid Application Backend. Runs using Python and MongoDB
## How to talk to the backend:
Head to https://combat-covid-v1.herokuapp.com/ (temporary) until Azure is set up.  
API Calls to the above website, POST Requests, JSON Objects

### /add_new_user
Method: POST  
Request: All User Data as JSON  
```JSON
{
    "first_name": string,
    "last_name": string,
    "dob": date,
    "currently_under_quarantine": boolean,
    "date_time_quarantined": datetime,
    "date_time_unquarantined": datetime,
    "phone_number": number,
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
    "success": boolean,
    "userobjid": object (string)
}
```
success tells if the user was successfully added or not  
userobjid return the object ID (as a string) if successfully added

### /add_new_test
Method: POST  
Request: Test Data as JSON  
```JSON
{
    "user_id": object (string),
    "testing_date_time": datetime,
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

### /add_close_contact
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

### /add_new_temperature
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
    "success": boolean,
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
