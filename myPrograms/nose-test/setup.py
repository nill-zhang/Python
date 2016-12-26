try:
from setuptools import setup
except ImportError:
from distutils.core import setup

config = { 
    "description" : "nosetest example"
    "author" : "shaofeng zhang"
    "url" : "http://github.com/nill-zhang/python_projects/nose-test.git"
    "download_url" : ""
    "author_email" : "andy.ledway3@gmail.com"
    "version" : "1.0.0" 
    "install_requires": ["nose"]
    "packages": ["example"]
    "scripts" : [],
    "name" : "project name"
}

setup(**config)
