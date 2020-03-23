# combat_covid
Covid Application Backend. Runs using Python and MongoDB
## How to talk to the backend:
Head to https://combat-covid-v1.herokuapp.com/ (temporary) until Azure is set up.  
API Calls to the above website, POST Requests, JSON Objects

### /add_new_user
Method: POST  
Request: All User Data as JSON  
Return:
```JSON
{
    "success": boolean,
    "userobjid": object
}
```
success tells if the user was successfully added or not.  
userobjid return the object ID (as a string) if successfully added.
