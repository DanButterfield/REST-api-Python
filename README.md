# PYTHON REST API with Flask Example Project

## A fully functioning REST API built in Python designed to understand the basics of APIs

This project is an example of a simple API built along with YouTube Tutorials from Tech With Tim
to allow me to have a better understanding of APIs and databases, the video can be found 
[here](https://www.youtube.com/watch?v=GMppyAPbLYk ).

### Key Terms:
| Term       | Description                       |
|------------|-----------------------------------|
| **REST**   | Representational State Transfer   |
| **API**    | Application Programming Interface |
| **GET**    | A method to retrieve Data         |
| **PUT** *  | A method to write updated Data    |
| **DELETE** | A method to Delete Data           |
| **POST** * | A method to write **new** data    |

The difference between Post and Put:
* POST is used to create a new resource. 
* PUT typically is used to update an existing resource.
* If a resources exists PUT updates it, if not PUT can create it.
* POST is not idempotent. 
## What is an REST API?
An API is a set of protocols for building and integrating application software. Sometimes referred to as a contract between
an information provider and a user. If you want to interact with a computer or system to retrieve information or preform a 
function an API can help you communicate what you want to the system for it to fulfill the requests.

REST is  a style for providing standards between computer systems on the web. Making it easier for devices to communicate
with each other. An API following the REST styles are called REST APIs, generally REST is a guideline to manage communications
on a complex network.


For Example:
1 Program developed in Python, and one in Java. An API would allow functionality in the Java application
to make requests to the Python application which would then give a response back to the Java application, via JSON 
(JavaScript Object Notation)

## Benefits of Using REST APIs


* One of the most important reasons for not going straight from an application straight to a database is because of security.
Having sensitive information on an application is a bad idea because the user can go straight to the database and do malicious 
things here.
* Another reason is versatility, two different front ends can now share the same back-end. Changing data on one device 
will also change it on another device. 
* Another reason is if you want to change the back-end the front-end will not be affected without requiring any updates 
to the front-end. Can also make certain end-points public meaning you don't have to worry about authentication or 
authorisation so anyone can make a new app with improvements to still be able to communicate with the API.

### References:
* Tech With Tim (2020) Python REST API Tutorial - Building a flask REST API. https://www.youtube.com/watch?v=GMppyAPbLYk.
* What is a REST API? (no date). https://www.redhat.com/en/topics/api/what-is-a-rest-api.
* What is RESTful API? - RESTful API Explained - AWS (no date). https://aws.amazon.com/what-is/restful-api/.




