try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = { 
    "description" : "my skeleton project",
    "author" : "shaofeng zhang",
    "url" : "http://github.com/nill-zhang/NAME/",
    "download_url" : "",
    "author_email" : "andy.ledway3@gmail.com",
    "version" : "1.0.0",
    "install_requires": ["nose"],
    "packages": ["NAME"],
    "scripts" : ["setup.py"],
    "name" : "project name",
}

setup(**config)
