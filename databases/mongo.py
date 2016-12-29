#!/usr/bin/python
from flask import Flask
from flask_pymongo import PyMongo
import flask_pymongo
import sys
app = Flask(__name__)
app.config.update({
    "MONGO_URI": "mongodb://192.168.65.222:27017/companies",
    "MONGO_USERNAME": "sfzhang",
    "MONGO_PASSWORD": "password"
})

mongo = PyMongo(app)
with app.app_context():
    try:
        mongo.db.companies.find_one()
    except pymongo.errors.OperationFailure:
        sys.stdout.write("Can not connect to database!")