# selfprojectdjango

# Description
This is a basic warehouse management project, which is created by using ORM models , PostgreSQL and Python Django framework. 


# Version applied in this project
Python: 3.8
Django: 4.12
PostgreSQL: 14.13


# User who use this repository
## Admin
Admin can edit, delete, make any modification of records from the database.
They can also choose to list out the warehouse whether its storage quota is full or not.
## Registered User 
Registered User can view the orders, including when and where to rent
## Unregistered User
Unregistered user can only view the ,but cannot access the 

# Overview of the models

# How to apply to your database?

## Please input the following commands in your command terminal (Ubuntu)
curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg\n

sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/jammy pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'

apt list --upgradable
sudo apt install pgadmin4
sudo -u postgres psql

It is assumed that you have installed pgadmin4 App.

Please input the following in terminal:
sudo -u postgres psql -U postgres
Then you will be asked to provide your Ubuntu password.
Next type "CREATE DATABASE ...... OWNER POSTGRES " in the terminal.
Typing "\q" whether the database is existed on the table or not.

You are advised to make connection and changes in the DATABASE array from the path "newprojecttrial/settings.py".

For Example:
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': '..........',
       'USER': 'dbadmin',
       'PASSWORD':'abc123!',
       'HOST': 'localhost'
   }
}   

Finally, "python manage.py makemigrations" and "python manage.py migrate" will help you develop the information structure on the database.

You should type "pip freeze > requirements.txt" to install the python package.

Then you run the server by typing "python manage.py runserver".

# URL Path Planning

## Our Map
| Url      | App | REST Method | Description |
| -------- | ---- | ----------- | --- |
| admin    | None   | GET       | Admin Page    |
| about    | Page    | GET        | About Page    |
| error    | Page | GET | Error Page
| service | Page | GET| Service Page
| warehouses | warehouse   |    GET         | Overview of all warehouse    |
| warehouses/<region:str> | warehouse   | GET | Show warehouses from that district |
| warehouses/?page=<number:int> | warehouse | GET | Show warehouses in pages |
| warehouse/<id:int> | warehouse   |    POST         |  Show independent warehouse record  |
| user | user | |
| user/dashboard | user | GET | Show his record
| user/login | user |POST | User Login
| user/logout | | |
