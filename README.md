# "ToRead" app

- This simple project was made for SKJ python course.

# Description

The ToDo app is a Python-based application built using customtkinter for managing your tasks. It allows users
to add, remove, and keep track of their to-do items. The application provides a simple and intuitive interface for task
management.

## Dependencies

- **Client**:
    - customtkinter
    - tkcalendar
    - requests

- **Server**:
    - Flask-RESTful
    - Flask-SQLAlchemy
    - marshmallow-sqlalchemy
    - flask-marshmallow

## How to run

### With global interpreter

```shell
$ pip install -r requirements.txt  # installs packages
$ python3 server/app.py  # run server
$ python3 client/app.py  # run client
```

### With virtual environment

```shell
$ python3 -m venv venv/todo_app # create virtual environment
$ source venv/todo_app/bin/activate # activate virtual environment
(todo_app) $ pip install -r requirements.txt  # installs packages
(todo_app) $ python3 server/app.py # run server
(todo_app) $ python3 client/app.py # run client
```