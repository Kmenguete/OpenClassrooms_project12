# Table of content
***
### 1. About the CRM
### 2. Prerequisites
### 3. Installation
### 4. Starting the project
***
## 1. About the CRM
***
Epic Events is an event management company which is highly reputed for events it 
organizes. The company used to work with an external service provider. Unfortunately,
the Customer Relationship Management(CRM) system used by this external service provider
has been hacked. Consequently, Epic Events was no longer able to work and lost a lot
of clients. Consequently, it was very urgent for them to develop their own CRM. My goal
in this project is then to create a secure CRM system that use Django ORM, Django Rest 
Framework and Postgresql.

The CRM consists of three kind of users:

-admin users

-sales contact users

-support contact users

#### 1. The admin users
***
The admin users has access to the Django admin site. Their role is to create users
that will use the CRM and grant them permissions according their role(sales contact 
or support contact). The admin users has also to manage the entire CRM by creating,
reading, updating and deleting(CRUD) every user and data in the CRM.
***
#### 2. The sales contact users
***
The role of the sales contact is to find new clients and add them to the CRM. If the
client wish to organize an event, the sales contact can create a contract associated
to this client and create an event associated to the contract and the client.
***
#### 3. The support contact users
***
The role of the support contact user start when the sales contact gives him the 
responsibility to manage the event. When the sales contact creates an event, he/she
has the possibility to choose which support contact user will have the responsibility
to manage the event. Once the support user has been chosen to manage the event, he/she 
get access of every data concerning the client that asked for the event, the contract,
the client signed for and the event that should be organized. The support contact will 
have then, the possibility to contact the client and interact with them to organize
and manage the event. According to the evolution of the event, the support contact user
will have the possibility to update the event until it ends.
***