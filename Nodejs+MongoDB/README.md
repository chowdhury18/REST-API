# Nodejs + MongoDB

## Objective
Create a RESTful API using NodeJS and MongoDB. Node.js is an open-source, cross-platform, JavaScript runtime environment that executes JavaScript code outside a web browser.

## Getting started

### Prerequisites
- Nodejs
- MongoDB

First, check out the environment setup to ensure everything works perfectly. Run npm -v and mongo --version to check the libraries are installed in your machine.

### File structure
```
.
│    server.js
└─── api
    └─── controllers   
    |    │   professorController.js
    |    │   researchGroupController.js
    |    │   studentController.js
    └─── models
    |    │   professor.js
    |    │   researchGroup.js
    |    │   student.js
    └─── routes
         │   professorRoutes.js
         │   researchGroupRoutes.js
         │   studentRoutes.js
```

### Step by step
- The schemas and path definitions are given in the following [link](https://chowdhury18.github.io/blogs/RESTfulAPI/nodejsREST.html).
- Create package.json.
```
npm init
```
Package.json is a file that gives the necessary information to npm which allows it to identify the project as well as handle the project's dependencies. Fill out some information regarding the application.

- Create a server (e.g., server.js)
```
npm install express --save  #create the node server
npm install -save-dev nodemon  #track the change and run server automatically
```
- Change starting point to **nodemon server.js**.
- Setting up the schema.
```
npm install mongoose --save  #interact with a MongoDB (Database) instance
```
- Write the model definition, route definition and controller definition.
- Write the server definition where database connection **db** indicates the name of the collection.
- Start and run the server without reloading: 
Check the mongo daemon is running background. To start the daemon, run ```mongod```. To interact with the mongo shell, run ```mongo shell```. Start the server running:
```
npm start
```
- The server will run at http://localhost:3000. Download [postman](https://www.postman.com/) OR use command line tool [curl](https://curl.haxx.se/) to execute the operations. The following [link](https://www.taniarascia.com/making-api-requests-postman-curl/) has the instructions to execute CRUD in both postman and curl.
