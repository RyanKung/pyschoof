# coding:utf8

import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
_CWD = os.path.dirname(__file__)

NAME = 'pyschoof'
DESCRIPTION = "Python implementation of Schoof's algorithm for counting the points on elliptic curves over finite fields"
AUTHOR = 'Peter Dinges, Ryan Kung'
EMAIL = 'pdinges@acm.org, ryankung@ieee.org'


setup(
    name=NAME,
    description=DESCRIPTION,
    long_description=open(os.path.join(here, 'README.md')).read(),
    version='0.1',
    packages=find_packages(exclude=['examples', '_test', 'doc']),
    package_dir={'': '.'},
    author=AUTHOR,
    author_email=EMAIL,
    license=open(os.path.join(here, 'LICENSE')).read(),
    platforms=['any'],
    url="",
    classifiers=["Intended Audience :: Developers",
                 "Programming Language :: Python",
                 "Topic :: Software Development :: Libraries :: Python Modules"],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'pyschoof=pyschoof.__main__:reduced_schoof',
            'pyschoofnaive=pyschoof.__main__:naive_schoof'
        ]
    }
)
