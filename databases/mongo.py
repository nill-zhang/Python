#!/usr/bin/python
from flask import Flask
from flask_pymongo import PyMongo
from pymongo.errors import OperationFailure
from pprint import pprint
import sys
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
        items = mongo.db.companies.find()
        for item in items:
            print(item["founded_year"])
    except OperationFailure:
        sys.stdout.write("Can not connect to database!")