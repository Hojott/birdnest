#!/usr/bin/env python
from threading import Thread

from app import flask_app
from db import control_database

def main():
    flask = Thread(target=flask_app, name="flask")
    flask.start()

    database = Thread(target=control_database, name="database")
    database.start()

if __name__ == "__main__":
    main()
