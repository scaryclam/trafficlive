import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="trafficlive",
    version="0.1",
    author="Becky Lewis",
    author_email="trafficlive@scaryclam.co.uk",
    description=("A simple API wrapper for trafficlives open API"),
    license="BSD",
    keywords="trafficlive",
    url="https://github.com/scaryclam/trafficlive",
    packages=['trafficlive'],
    long_description=read('README'),
    requires=['requests'],
)

