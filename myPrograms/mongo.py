#!/usr/bin/python
from flask import Flask
from flask_pymongo import PyMongo
import flask
from pymongo.errors import OperationFailure
import sys


def test_pymongo():
    app = Flask(__name__)
    app.config.update({
        #using default port 27017/tcp
        "MONGO_URI": "mongodb://sfzhang:sfzhang@192.168.65.222/test"
    })

    # Alternative:
    # app.config.update({
    #     "MONGO_HOST": "192.168.65.222",
    #     "MONGO_DBNAME": "test",
    #     "MONGO_USERNAME": "sfzhang",
    #     "MONGO_PASSWORD": "sfzhang"
    # })
    mongo = PyMongo(app)
    # make sure execute code under an active application context

    with app.app_context():
        try:
            items = mongo.db.companies.find({}, {})
            for item in items:
                print(item["founded_year"])
        except OperationFailure:
            sys.stdout.write("Can not connect to database!")

    # How to build a context using the other way

    app_ctx = app.app_context()
    app_ctx.push()
    try:
        print(flask.current_app.name)
    finally:
        app_ctx.pop()

    # from werkzeug.test import EnvironBuilder
    # re_ctx = app.request_context(EnvironBuilder("/", "http://localhost").get_environ())
    # re_ctx.push()
    # try:
    #     pass
    # finally:
    #     re_ctx.pop()

if __name__ == "__main__":
    import json
    entry = json.loads('{"name":"sfzhang", "salary":"5000", "address":"55 Oakmount Rd."}')
    print("type: %r" % type(entry))
    for i, j in entry.items():
        print("%r----->%r" % (i, j))
    jstring = json.dumps(entry)
    print("Jstring : %r" % jstring)

