# API

An API is an akronym for Application Programming Interface. It is a set of clearly defined methods of communication between various software components. A good API makes it easier to develop a program by providing all the building blocks. A programmer then puts the blocks together.

## REST

REST is an akronym for Representational State Transfer. It is an architectural style for providing standards between computer systems on the web, making it easier for systems to communicate with each other. REST-compliant systems, often called RESTful systems, are characterized by how they are stateless and separate the concerns of client and server. We will learn more about REST in the next section.

## RESTful API

A RESTful API is an API that conforms to the REST architectural style and constraints. RESTful APIs are designed to be stateless, which makes RESTful APIs less complex than SOAP APIs. RESTful APIs are also designed to have a uniform interface, which makes RESTful APIs easier to use than SOAP APIs.

## RESTful API Design

RESTful APIs are designed around resources, which are any kind of object, data, or service that can be accessed by the client. RESTful APIs use HTTP requests to perform four operations, which are sometimes referred to as CRUD (Create, Read, Update, Delete) operations:

- Create - Creates a new resource
- Read - Reads a resource
- Update - Updates an existing resource
- Delete - Deletes a resource

RESTful APIs use a stateless request model. This means that each request contains all of the information necessary for a connector to understand the request. This information can consist of headers, query parameters, body content, URLs, and more. This means that neither the client nor the server need to remember any previous state before instructing the next request. This makes RESTful APIs less complex than SOAP APIs.

RESTful APIs use a uniform interface. This means that the request methods (GET, POST, PUT, PATCH, DELETE, etc.) and response codes (200, 201, 400, 401, 403, 404, 500, etc.) are the same for all resources. This makes RESTful APIs easier to use than SOAP APIs.

## RESTful API Example

Let's look at an example of a RESTful API. Let's say we have a database of users. We want to create a RESTful API that allows us to perform CRUD operations on the users in the database. We want to be able to create a new user, read a user, update a user, and delete a user. We want to be able to do this for all users in the database, or for a specific user in the database.

We can use the following HTTP methods to perform CRUD operations on the users in the database:

- Create - POST
- Read - GET
- Update - PUT
- Delete - DELETE

We can use the following URLs to perform CRUD operations on the users in the database:

- Create - /users
- Read - /users
- Update - /users
- Delete - /users

In SQL, we can use the following queries to perform CRUD operations on the users in the database:

- Create - INSERT INTO users (name, email) VALUES ('John Doe', 'Jane Doe')
- Read - SELECT * FROM users
- Update - UPDATE users SET name = 'John Doe', email = 'Jane Doe' WHERE id = 1
- Delete - DELETE FROM users WHERE id = 1
