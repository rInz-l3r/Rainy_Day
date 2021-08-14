from sanic import Sanic
from sanic.response import *
import requests
import json

app = Sanic("Auth Service")

USER_SERVICE = "http://localhost:8080/"

# user validation endpoint
@app.post("/login")
async def login(request):
    ''' login endpoint checks for valid user by hitting the user service '''
    print("Hitting User Service")
    r = requests.post(USER_SERVICE + "users/valid", data=request.body)
    if r.status_code == 200:
        return empty(status=200)
    else:
        return empty(status=401)

# user registration endpoint
@app.post("/register")
async def register(request):
    ''' register endpoint attempts to register a new user using the user service.'''
    r = requests.post(USER_SERVICE + "users/create", data=request.body)
    if r.status_code == 201:
        return empty(status=201)
    else:
        return empty(status=400)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8082, debug=True)