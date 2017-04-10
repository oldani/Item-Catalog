# Item-Catalog
An application that provides a list of items within a variety of categories an use Oauth uthentication system. This have been develop as part of Udacity Nanodegree Program.


## Table of content

- [Requirements](#requirements)
- [Quick Started](#quick-started)
- [Deployment](#deployment)


## Requirements
- [Python 3](https://www.python.org/downloads/release/python-353/)
- [Postgresql](https://www.postgresql.org/)
- [Virtualenv `optional`](https://virtualenv.pypa.io/en/stable/)
- [A Google Cloud Account](console.developers.google.com)
- [A Facebook Account](developers.facebook.com)


## Quick Started
Once you have all the requirements setup:

**Note:** Before seting up the environment, create a new project
in the google console and Facebook for developers to get your Product
credentials required for the use of Oauth. Also create a database.

1. Clone this repository.
  * Run `git clone https://github.com/oldani/Item-Catalog.git`
in the console
2. If using `virtualenv`
  * Create an env by running `virtualenv -p python3 env` and
activate it.
3. In the project repository
  * Run `pip install requirements.txt`
    For user using Linux `libpq-dev` is required for psycopg2.
  * Edit the `env.example` file, replacing all the env vars
example values with real ones. Once done rename the file to
`.env`.
  * Run `python manage.py db upgrade`,
this will setup your db tables.
4. Once everything setup run `python manage.py runserver`
5. Go to `http://localhost:5000/`.
