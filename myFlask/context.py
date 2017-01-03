#!/usr/bin/env python
# by sfzhang 2017.1.2
import flask
from flask import Flask
from flask import request_started, request_finished, request_tearing_down, \
                  appcontext_popped, appcontext_pushed, appcontext_tearing_down, \
                  before_render_template, message_flashed, template_rendered
import blinker
# from werkzeug.test import EnvironBuilder
app = Flask(__name__)

# ###################################Context Hook ############################################


@app.before_first_request
def before_first_request():
    print("before_first_request %s" % flask.g)


@app.before_request
def before_request():
    print("before_request %s" % flask.g)


# We need to pass an parameter to the following
# three methods

@app.after_request
def after_request(resp):
    print("after_request %s" % flask.g)
    resp.headers["random"] = "random"
    return resp


@app.teardown_request
def teardown_request(e):
    print("teardown_request: %s" % flask.g)


@app.teardown_appcontext
def teardown_appcontext(e):
    print("teardown_appcontext: %s" % flask.g)


################################################################################


# ###################################Signals#####################################

def request_started_callback(sender, **extra):
    print("Signal: Request Started")
    print("Parameters Passed in:")
    print(("%s--->%s" % i for i in extra.items()), sep="\n")

request_started.connect(request_started_callback, app)


@request_finished.connect_via(app)
def request_finished_callback(sender, **extra):
    print("Signal: Request Finished")
    print("Parameters Passed in:")
    print(("%s--->%s" % i for i in extra.items()), sep="\n")


@request_tearing_down.connect_via(app)
def request_tearing_down_callback(sender, **extra):
    print("Signal: Request Tearing Down")
    print("Parameters Passed in:")
    print(("%s--->%s" % i for i in extra.items()), sep="\n")


@appcontext_popped.connect_via(app)
def appcontext_popped_callback(sender, **extra):
    print("Signal: Appcontext Popped")
    print("Parameters Passed in:")
    print(("%s--->%s" % i for i in extra.items()), sep="\n")


@appcontext_pushed.connect_via(app)
def appcontext_pushed_callback(sender, **extra):
    print("Signal Appcontext Pushed")
    print("Parameters Passed in:")
    print(("%s--->%s" % i for i in extra.items()), sep="\n")


@appcontext_tearing_down.connect_via(app)
def appcontext_tearing_down(sender, **extra):
    print("Signal: Appcontext Tearing Down")
    print("Parameters Passed in:")
    print(("%s--->%s" % i for i in extra.items()), sep="\n")


@before_render_template.connect_via(app)
def before_render_template_callback(sender, **extra):
    print("Signal: Before Render Template")
    print("Parameters Passed in:")
    print(("%s--->%s" % i for i in extra.items()), sep="\n")


@template_rendered.connect_via(app)
def template_rendered_callback(sender, **extra):
    print("Signal: Template Rendered")
    print("Parameters Passed in:")
    print(("%s--->%s" % i for i in extra.items()), sep="\n")


@message_flashed.connect_via(app)
def message_flashed_callback(sender, **extra):
    print("Signal: Message Flashed")
    print("Parameters Passed in:")
    print(("%s--->%s" % i for i in extra.items()), sep="\n")


custom_signal = blinker.Namespace()
index_called = custom_signal.signal("index_called")


@index_called.connect_via(app)
def index_called_custom_callback(sender, **extra):
    print("Custom Signal: Index Called")
    print("Parameters Passed in:")
    print(("%s--->%s" % i for i in extra.items()), sep="\n")

###############################################################################
@app.route("/")
def index():
    print("Handling Request")
    index_called.send(flask.current_app._get_current_object(), method=flask.request.method)
    flask.flash("Hi there, welcome to my homepage")
    return flask.render_template("context_signal.html")

# print("Before Execute")
# with app.app_context():
#     print("Before Building Request")
#     #with app.request_context(EnvironBuilder("/", "http://127.0.0.1:5000").get_environ()):
#     with app.test_request_context("/", "http://127.0.0.1:5000"):
#         print("Request URL %s" % flask.request.url)
#     print("Finished Request")
# print("Finished Application")


if __name__ == "__main__":
    app.run()



