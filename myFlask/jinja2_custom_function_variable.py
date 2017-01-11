#!/usr/bin/env python
# by sfzhang 2017.1.3
from flask import Flask
import flask
import time
app = Flask("FLAPP")
app.config.update({"DEBUG": True, "SECRET_KEY": "whatever"})

# The following two methods define customize jinja2 variables and
# funtions that we can use in our templates


@app.context_processor
def custom_variable():
    appname = flask.current_app.name
    return dict(appname=appname)


@app.context_processor
def custom_function():
    def get_time(datefmt="%Y-%m-%d %H:%M:%S"):
        return time.strftime(datefmt)
    return dict(get_time=get_time)


@app.route("/")
def index():
    flask.g.db = "mongodb"
    flask.session["uname"] = "sfzhang"
    return flask.render_template("custom_jinja2.html")


@app.route("/login")
def login():
    flask.g.db = "mysql"
    flask.session["uname"] = "admin"
    return flask.render_template("custom_jinja2.html")

if __name__ == "__main__":
    app.run()

