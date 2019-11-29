# REST API for Emoji Key Retrieval

> API using Python Flask, SQL Alchemy and Marshmallow

## Quick Start

install pipenv: https://pipenv-es.readthedocs.io/es/stable/#install-pipenv-today

``` bash
# Activate venv
$ pipenv shell

# Install dependencies
$ pipenv install

# Create DB
$ python3
>> from app import db
>> db.create_all()
>> exit()

# Run Server (http://localhst:5000)
python3 app.py
```

## Endpoints

* POST    /create       -> params name=string       -> creates an 'account' in the database
* POST    /getname      -> params emoji_key=string  -> retrieves account with corresponding private key
* GET     /accounts                                 -> gets a list of all accounts