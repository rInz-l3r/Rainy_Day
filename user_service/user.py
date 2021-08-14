from sanic import Sanic
from sanic.response import *

app = Sanic("Auth Service")

customers = ["John"]

@app.post("/users/valid")
async def checkUser(request):
    ''' Check if name exists in the JSON, if so, if user exists, authorize, if
    not, send 401 status code '''
    if request.json.get('name'):
        if request.json['name'] in customers:
            return empty(status=200)
        else:
            return empty(status=401)
    else:
        return empty(status=400)



@app.post("/users/create")
async def checkUser(request):
    ''' Check if name exists in the JSON, if so, if user doesnt already exist
    add the user, send back a bad request status code.'''
    if request.json.get('name'):
        if request.json['name'] not in customers:
            customers.append(request.json['name'])
            print(customers)
            return empty(status=201)
    else:
        return empty(status=400)

    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)