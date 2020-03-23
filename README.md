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
    "userobjid": object
}
```
success tells if the user was successfully added or not  
userobjid return the object ID (as a string) if successfully added

### /add_new_test
Method: POST  
Request: Test Data as JSON  
```JSON
{
	"user_id": string (object),
	"testing_date_time": datetime,
	"test_result": boolean,
	"other_data": string
}
```
Return:
```JSON
{
    "success": boolean,
    "testobjid": object
}
```
success tells if the test data was added successfully   
testobjid gives the object ID (as string) of the test if successfully added
