from flask import Flask, make_response, request
import json


# Create an instance of the Flask class. The first argument is the name of the application’s module
# or package. __name__ is a convenient shortcut for this that is appropriate for most cases. This is
# needed so that Flask knows where to look for resources such as templates and static files.
api = Flask(__name__)


@api.route("/") # routes to the root of our app
def home():
    # create a response with plain text and a status code of 200 SUCCESS
    resp = make_response("home", 200)
    
    # return the response to the calling client
    return resp


@api.route("/static-users", methods=["GET"]) # routes to /static-users and only allows a GET http method
def get_static_users():
    # create a static dictionary of our users
    users = {
                "user1": {"email": "user1@email.com", "favorite_color": "red"},
                "user2": {"email": "user2@email.com", "favorite_color": "green"},
                "user3": {"email": "user3@email.com", "favorite_color": "blue"}
            }
    
    # create a response with the users dictionary as the body and a status code of 200 SUCCESS
    # note: flask automatically converts python dictionaries to json
    resp = make_response(users, 200)

    # return the response to the calling client
    return resp



######################################
#### persisting and adding users #####
######################################

@api.route("/users", methods=["GET"]) # routes to /users and only allows a GET http method
def get_users():

    # open users json file in read mode 
    with open("./users.json", "r") as users_file:
        users = json.load(users_file) # read the json from the file and store it as a dictionary
    
    resp = make_response(users, 200) # create a response with the users read from the file and a status code of 200 SUCCESS

    return resp


@api.route("/users/create", methods=["POST"])
def create_user():
    
    req_body = request.get_json(force=True) # capture the incoming request's json body - using force=True so that the calling client doesn't have to pass in any headers
    
    # open the json file in read mode and get existing users
    with open("./users.json", "r") as users_file:
        users = json.load(users_file)   # read existing users

    users[req_body["username"]] = {"favorite_color": req_body["favorite_color"], "email": req_body["email"]} # add new user to users dict
    
    # open the users json file in write mode
    with open("./users.json", "w") as users_file:
        users_file.write(json.dumps(users)) # write the new list of user to the file

    resp = make_response("", 201) # create a response with an empty body and a 201 CREATED status code
    
    return resp
