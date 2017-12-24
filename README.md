#Requirements

pip3 install -r requirements.txt

# Install postgres

sudo apt-get install postgresql-server postgresql

# Altere os dados do seu banco na pasta sisbp/settings.py

    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'sbpl',
    'USER': 'seuUsuario',
    'PASSWORD': 'suaSenha',
    'HOST': 'localhost',
    'PORT': '5432',
    
#Get started

## Before first time running the server

* python3 manage.py makemigrations
* python3 manage.py migrate

## Serve application

* python3 manage.py runserver
