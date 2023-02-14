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
## 2. Prerequisites
***
For this project, Django 4.1.5, Django Rest Framework 3.14.0, GitHub and Python 3.10
are required.
***
## 3. Installation
***
In order to install Django Rest Framework, you need first to install Django. 
Before to install Django, make sure your virtual environment is activated. If your 
virtual environment is not activated run the following command "env/bin/activate" in 
the directory you intend to start the project (in the terminal of your IDE). In the 
directory, you intend to start your project, install Django by running the following 
command in the terminal of your IDE: pip install django. Once Django is installed,
create a file named requirements.txt and add Django(and his version) and Django Rest 
Framework(and his latest release) in the requirements.txt file. Afterwards, go to 
the terminal of your IDE(still in the directory you started your Django project) and 
run the following command: pip install -r requirements.txt.
***
## 4. Starting the project
***
Once you have successfully installed Django and Django Rest Framework, you can 
clone the project by using git clone or git pull with the following address:
https://github.com/Kmenguete/OpenClassrooms_project12.git. When you pulled the
project in your local machine, you can start improving this CRM ;). If you are 
a frontend developer and want to work with the API of the CRM see the following 
link: https://documenter.getpostman.com/view/23193108/2s935vn1Df