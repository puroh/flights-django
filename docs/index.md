# flights-django

[![Build Status](https://travis-ci.org/puroh/flights-django.svg?branch=master)](https://travis-ci.org/puroh/flights-django)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

Flights a round the world. Check out the project's [documentation](http://puroh.github.io/flights-django/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)

# Initialize the project

Start the dev server for local development:

```bash
docker-compose up
```

Create a superuser to login to the admin:

```bash
docker-compose run --rm web ./manage.py createsuperuser
```

# Load data in Data base

For charged the data in the data base, first run this code for load data legs

```bash
docker-compose run --rm web ./manage.py loaddata legs.json
```

And them load itineraries data

```bash
docker-compose run --rm web ./manage.py loaddata itineraries.json
```