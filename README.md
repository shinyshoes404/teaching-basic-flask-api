# teaching-basic-flask-api
A simple one file API example using Python and Flask

## Getting your environment setup
 Assuming Windows with these commands. Mac and Linux will be slightly different.
 - Clone this project with `git clone https://github.com/teaching-basic-flask-api`
 - Move into the root of the project
 - Create a virtual environment `python -m venv venv_basic_flask`
 - Activate your new virtual environment `. venv_basic_flask/Scripts/Activate`
 - Install flask `pip install flask`


## Starting the API
 - In the root of the project run `flask --app api run --debug`
    - This will start the API running on localhost and port 5000
    - Note: the --debug flag will cause the flask server to reload each time a change is made to the api.py file, which is nice if you want to experiment and make changes
 - You can stop the API at any time with `ctrl + c`

## cURL commands
Once the API is running on the flask server, you can interact with it using cURL.
 - Home
    - `curl localhost:5000`
 - Get static users
    - `curl localhost:5000`
 - Get users
    - `curl localhost:5000/users`
 - Create a new user
    - `curl -X POST localhost:5000/users/create -d '{"username": "your-username", "favorite_color": "your-favorite-color", "email": "your-email"}'`
