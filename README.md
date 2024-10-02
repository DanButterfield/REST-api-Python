# REST-api-Python

## What is an REST API?
REST stands for - Representational State Transfer. Communicating over the internet. Similar to making requests to a 
website


API stands for - Application Programming Interface
Which is a way software can interact with each other, if built different

For Example:
1 Program developed in Python, and one in Java. An API would allow functionality in the Java application
to make requests to the Python application which would then give a response back to the Java application, via JSON 
(JavaScript Object Notation)

## Why use an API?

One of the most important reasons for not going straight from an application straight to a database is because of security.
Having sensitive information on an application is a bad idea because the user can go straight to the database and do malicious 
things here. The other big reason is versatility, two different front ends can now share the same back-end. Changing data 
on one device will also change it on another device, for example. Another reason is if you want to change the back-end 
the front-end will not be affected without requiring any updates to the front-end. Can also make certain end-points public
meaning you don't have to worry about authentication or authorisation so anyone can make a new app with improvements to still
be able to communicate with the API. 

GET - Retrieve data 

POST - Write **new** data

DELETE - Deleting data

PUT - Write **updated** data


Post is used to add a resource, Whereas PUT is used to replace a resource.
PUT is idempotent. 






