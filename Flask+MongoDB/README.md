# Flask + MongoDB

## Objective
Create a RESTful API using Flask web developement framwork and MongoDB. Flask is a micro web framework written in Python.

## Getting started

### Prerequisites
It is recommended to create virtual environment for the purpose of seperate project environment and clean code. To create python virtual environment in Linux and Windows platform, please follow the given [link](https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/).

- Flask
- Flask-mongoengine
- BSON

### File structure
```
.
│    app.py
└─── database
    │   db.py
    │   models.py

```

### Step by step
- The schemas and path definitions are given in the following [link](https://chowdhury18.github.io/blogs/RESTfulAPI/flaskREST.html).
- Create the models.
- Add the following code to initialize the application in mongoengine.
```
# database config
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/flask-db'
}
db = initialize_db(app)
```
- Note: flask-db is the name of the collection.
- Create the RESTful application in FLask.
- To start and run the server without reloading, run the following command in terminal.
```
FLASK_APP=app.py FLASK_ENV=developement flask run
```
- The server will run at http://localhost:5000. Download [postman](https://www.postman.com/) OR use command line tool [curl](https://curl.haxx.se/) to execute the operations. The following [link](https://www.taniarascia.com/making-api-requests-postman-curl/) has the instructions to execute CRUD in both postman and curl.

# Contrainerize REST API
### Prerequisites
- Docker
- Docker-compose
- MongoDB

Install the prerequisites and run the command ```pip freeze > requirements.txt``` to list all the installed libraries in the python virtual environment. Run mongo --version, docker -v and docker-compose -v to check the libraries are installed in your machine.

### File structure
```
.
│    app.py
│    Dockerfile
│    docker-compose.yaml
│    requirements.txt
└─── database
    │   db.py
    │   models.py

```

### Step by step
- Create the flask REST API application.
- Write Dockerfile to create image for the application. Run the command to build the image:
```
docker build -t flaskbackend:v2
```
The dot (.) at the end of the docker build command to indicate the Dockerfile. To check the built image, run docker images.
- Write the docker-compose file with two services (application and database)
- Start both services:
```
docker-compose up -d  # -d for running in background
```
After running the command, mongo image will be downloaded from the dockerhub, and both flaskbackend and mongo containers will be created.
- The server will run at http://localhost:5000. Download [postman](https://www.postman.com/) OR use command line tool [curl](https://curl.haxx.se/) to execute the operations. The following [link](https://www.taniarascia.com/making-api-requests-postman-curl/) has the instructions to execute CRUD in both postman and curl.