# Nodejs + MongoDB

## Objective
Write an openapi 3.0 specification for Flask RESTful application.

## Getting started
The Flask RESTful application deals with course management system where students can execute CRUD operation to manage their courses. To successfully build the Flask RESTful application, please follow "Flask + MongoDB". The code can be downloaded from the following [link]().

### File structure
```
.
│    app.py
└─── database
|   |   openapi.yaml
└─── database
    │   db.py
    │   models.py
```

### Openapi 3.0 specification
The OpenAPI Specification (OAS) defines a standard, language-agnostic interface to RESTful APIs which allows both humans and computers to discover and understand the capabilities of the service without access to source code, documentation, or through network traffic inspection. For more details, follow the link.

To write the openapi specification, you can use [Swagger Editor](https://editor.swagger.io/) or Visual Studio Code and [Swagger UI](https://swagger.io/tools/swagger-ui/). This article prefers to write the specification using VS Code and Swagger UI. The docker image of Swagger UI is downloaded from dockerhub.

### Step by step
- The schemas and path definitions are given in the following [link](https://chowdhury18.github.io/blogs/RESTfulAPI/openapiFlaskREST.html).
- Write the openapi specification.
- Start and run both the services: 
```
# Flask Application:
FLASK_APP=app.py FLASK_ENV=developement flask run

# Swagger UI:
docker run --name swaggerUI --rm -p 8080:8080 -e SWAGGER_JSON=/foo/openapi.yaml -v $PWD/swagger:/foo swaggerapi/swagger-ui
```
- The application server will run at http://localhost:5000 and the Swagger UI will run at http://localhost:8080.
