#!/usr/bin/env python
# by sfzhang 2017.1.2
import flask
app = flask.Flask(__name__)


# the first arguments of these custom functions are
# those before the pipe literal in jinja2 templates

# two alternatives rather than decorating:
# app.jinja_env.filters["rand_sample"] = random_sample
# app.add_template_filter(random_sample, "rand_sample")
@app.template_filter("rand_sample")
def random_sample(lst, count):
    """A Custom Jinja2 filter function"""
    import random
    return random.sample(lst, count)


# two alternatives rather than decorating:
# app.jinja_env.tests["is_number"] = is_number
# app.add_template_filter(is_number, "is_number")
@app.template_test("is_number")
def is_number(target):
    """A Custom Jinja2 test function"""
    import numbers
    return isinstance(target, numbers.Number)


@app.route("/")
def index():
    return flask.render_template("jinja2_custom_filter_test.html")

if __name__ == "__main__":
    app.run()
