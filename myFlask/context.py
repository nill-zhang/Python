#!/usr/bin/env python
# by sfzhang 2017.1.2
import flask
from flask import Flask
from flask_bootstrap import Bootstrap
from flask import request_started, request_finished, request_tearing_down, \
                  appcontext_popped, appcontext_pushed, appcontext_tearing_down, \
                  before_render_template, message_flashed, template_rendered
import blinker
# from werkzeug.test import EnvironBuilder
app = Flask(__name__)
app.config.update({"SECRET_KEY": "SHAOFENG ZHANG"})


# ###################################Context Hook ############################################
def hook_output_decorator(func):
    """print current context hook func name"""
    def wrapper(*args, **kwargs):
        print("\033[34mHook: %s\033[0m" % func.__name__)
        func(*args, **kwargs)
        print("=" * 180)
    return wrapper


@app.before_first_request
@hook_output_decorator
def before_first_request():
    pass


@app.before_request
@hook_output_decorator
def before_request():
    pass


# We need to pass an parameter to the following
# three methods

@app.after_request
@hook_output_decorator
def after_request(resp):
    resp.headers["random"] = "random"
    return resp


@app.teardown_request
@hook_output_decorator
def teardown_request(e):
    pass


@app.teardown_appcontext
@hook_output_decorator
def teardown_appcontext(e):
    pass

# ###################################END#########################################


# ###################################Signals#####################################
def callback_output_decorator(func):
    """ print all the parameters passed to a receiver(callbacks) by sender"""
    def wrapper(*args, **kwargs):
        print("\033[33mSignal: %s" % (func.__name__.replace("_", " ")[:-9]).title())
        print("Parameters Passed in:")
        print(*("%s--->%s" % i for i in kwargs.items()), sep="\n")
        func(*args, **kwargs)
        print("\033[0m" + "=" * 180)

    return wrapper


@callback_output_decorator
def request_started_callback(sender, **extra):
    pass

request_started.connect(request_started_callback, app)


@request_finished.connect_via(app)
@callback_output_decorator
def request_finished_callback(sender, **extra):
    pass


@request_tearing_down.connect_via(app)
@callback_output_decorator
def request_tearing_down_callback(sender, **extra):
    pass


@appcontext_popped.connect_via(app)
@callback_output_decorator
def appcontext_popped_callback(sender, **extra):
    pass


@appcontext_pushed.connect_via(app)
@callback_output_decorator
def appcontext_pushed_callback(sender, **extra):
    pass


@appcontext_tearing_down.connect_via(app)
@callback_output_decorator
def appcontext_tearing_down_callback(sender, **extra):
    pass


@before_render_template.connect_via(app)
@callback_output_decorator
def before_render_template_callback(sender, **extra):
    pass


@template_rendered.connect_via(app)
@callback_output_decorator
def template_rendered_callback(sender, **extra):
    pass


@message_flashed.connect_via(app)
@callback_output_decorator
def message_flashed_callback(sender, **extra):
    pass


custom_signal = blinker.Namespace()
index_called = custom_signal.signal("index_called")


@index_called.connect_via(app)
@callback_output_decorator
def index_called_custom_callback(sender, **extra):
    pass

#####################################END##########################################


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
    bootstrap = Bootstrap(app)
    app.run()



