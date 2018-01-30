# Requirements

pip3 install -r requirements.txt

# Install postgres

sudo apt-get install postgresql-server postgresql

# Configure postgres

1. Inside the main project directory, access postgres terminal through this command:
```
sudo -u postgres psql;
```
2. Change the postgres password
```sql
ALTER USER postgres PASSWORD '123456';ALTER ROLE;
```
3. Once on postgres terminal, let's create the database.
```sql
CREATE DATABASE sbpl;
```
4. Everything is in place. Finally setup the database structure.
```
\c sbpl;
\i sisbp/bd/schema_v1.sql;
\q
```

# Altere os dados do seu banco na pasta sisbp/settings.py

    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'sbpl',
    'USER': 'seuUsuario',
    'PASSWORD': '123456',
    'HOST': 'localhost',
    'PORT': '5432',
    
#Get started

## Before first time running the server

* python3 manage.py makemigrations
* python3 manage.py migrate

## Serve application

* python3 manage.py runserver
