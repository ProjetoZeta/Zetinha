


# Requirements

pip3 install -r requirements.txt

# Install postgres

sudo apt-get install postgresql-server postgresql

# Configure postgres

```
sudo -u postgres dropdb sbpl;
sudo -u postgres createdb sbpl;
sudo -u postgres psql -c "alter user postgres with encrypted password '121294';";
sudo -u postgres psql -c "grant all privileges on database sbpl to postgres;";
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
