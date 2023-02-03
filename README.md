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