# insta-task
Steps to set up the environment and run server

Command to install virtualenv - pip3 install virtualenv
Create a virtualenv - virtualenv env
Activate virtualenv - source env/bin/activate
Installing dependancies - pip install -r requirements.txt
After installing all the requirements create a database and chamge the database configurations n setings.py
Apply migrations commands - python manage.py migrate
Command to start server - python manage.py runserver



******************************************************************************************************************
API to add users-
url - http://127.0.0.1:8000/InstaUser/
method - POST
request body - 
{
	"first_name" : "sfdffd",
	"last_name" : "shfhjdsbf",
	"phone": 32434,
	"email": "sasds",
	"is_admin": false
}


curl command - 
curl -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/InstaUser/ -d '{ "first_name": "David", "last_name": "Jones", "phone": "+15101234567", "email":"test@test.com", "is_admin": 0}'

******************************************************************************************************************


API to edit user - 
url - http://127.0.0.1:8000/InstaUser/
method - PUT
request body - 
{
	 "id": 4,
	 
      "first_name": "sachin" // send fields which should be updated
}

curl command -
curl -X PUT -H "Content-Type:application/json" http://127.0.0.1:8000/InstaUser/ -d '{ "id": 1, "first_name": "David", "last_name": "Jones", "phone": "+15101234567", "email":"test@test.com", "is_admin": 0}'

******************************************************************************************************************

API to get user list
url - http://127.0.0.1:8000/InstaUser/
method - GET

curl command - 
curl -X GET -H "Content-Type:application/json" http://127.0.0.1:8000/InstaUser/

******************************************************************************************************************

API to delete user
url - http://127.0.0.1:8000/InstaUser/
method - DELETE
request body - 
{
  "id": <userID>
}

curl command - 
curl -X DELETE -H "Content-Type:application/json" http://127.0.0.1:8000/InstaUser/ -d '{"id":8}'
