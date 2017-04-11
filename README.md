# Item-Catalog
An application that provides a list of items within a variety of categories an use Oauth uthentication system. This have been develop as part of Udacity Nanodegree Program.


## Table of content

- [Requirements](#requirements)
- [Quick Started](#quick-started)
- [Deployment](#deployment)


## Requirements
- [Python 3](https://www.python.org/downloads/release/python-353/)
- [Postgresql](https://www.postgresql.org/)
- [Vagrant](https://www.vagrantup.com/downloads.html)
- [Virtualbox](https://www.virtualbox.org/wiki/Downloads)
- [A Google Cloud Account](console.developers.google.com)
- [A Facebook Account](developers.facebook.com)


## Quick Started
Once you have all the requirements setup:

**Note:** Before seting up the environment, create a new project
in the google console and Facebook for developers to get your Product
credentials required for the use of Oauth. Also database named `item-catalog`
is created by default with a user:pass `ubuntu:123456`.

1. Clone this repository.
  * Run `git clone https://github.com/oldani/Item-Catalog.git`
in the console
2. `cd` into the repository and run `vagrant up && vagrant ssh`
3. Once vm have been created and you have ssh
  * `cd /vagrant`
  * Run `source env/bin/activate`
  * Run `pip install -r requirements.txt`
  * Edit the `env.example` file, replacing all the env vars
example values with real ones. Once done rename the file to
`.env`.
  * Run `python manage.py db upgrade`,
this will setup your db tables.
4. Once everything setup run `python manage.py runserver`
5. Go to `http://localhost:5000/`.
