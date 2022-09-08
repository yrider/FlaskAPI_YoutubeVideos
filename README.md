# Flask REST API for Videos

Simple REST API built with flask and a SQLAlchemy database. User can create,  update, get and delete videos from database via python programs (there is no web interface).
## Table of Contents

* [Installation](#installation)
  * [Dependencies](#dependencies)
* [Getting Started](#getting-started)

## Installation

create a new directory, move to it and clone this repository:

```
$ git clone
```

Create a virtual environment and activate it:

```
$ python3 -m venv venv
$ source venv/bin/activate
```

Run the requirements.txt file:
```
$ pip install -r requirements.txt
```
You should now be able to run the flask application by running main.py. Click [here](#getting-started) for support.

### Dependencies

This project requires:
* python >= 3.8
* aniso8601 == 8.0.0
* click == 7.1.2
* Flask == 1.1.2
* Flask-RESTful == 0.3.8
* Flask-SQLAlchemy == 2.4.3
* itsdangerous == 1.1.0
* Jinja2 == 2.11.2
* MarkupSafe == 1.1.1
* pytz == 2020.1
* six == 1.15.0
* SQLAlchemy == 1.3.18
* Werkzeug == 1.0.1

## Getting Started

Before running the program, please ensure:

Your virtual environment is active.
You are in the root directory where the main.py file is located.
Run the flask application:

```
$ python3 main.py
```

As there is no web-interface for HTTP requests, please separately run (and edit) the tests/terminal_test.py file or create a similar program to use the HTTP request methods.
