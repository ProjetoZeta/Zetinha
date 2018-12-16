# Virtualenv

* virtualenv venv -p python3
* source venv/bin/activate

# Requirements

Python >= 3.5
pip install -r requirements.txt

# Install postgres

sudo apt-get install postgresql

# Configure postgres

```
sudo -u postgres dropdb sbpl;
sudo -u postgres createdb sbpl;
sudo -u postgres psql -c "alter user postgres with encrypted password '121294';";
sudo -u postgres psql -c "grant all privileges on database sbpl to postgres;";
```
#Get started

## Before first time running the server

* python manage.py makemigrations
* python manage.py migrate

## Adtionally creating mock data

* python manage.py flush
* python manage populateserver

## Serve application

* python manage.py runserver
