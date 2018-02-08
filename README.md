# Requirements

pip3 install -r requirements.txt

# Install postgres

sudo apt-get install postgresql-server postgresql

# Configure postgres

1. Create database:
```
sudo -u postgres createdb sbpl
```
2. Load the db script:
```
sudo -u postgres psql -d sbpl -a -f bd/schema_v1.sql
```
3. Access postgres console
```
sudo -u postgres psql sbpl
```
4. On the postgres console, change the postgres password
```sql
ALTER USER postgres WITH PASSWORD '121294';\q
```

#Get started

## Before first time running the server

* python3 manage.py makemigrations
* python3 manage.py migrate

## Serve application

* python3 manage.py runserver
