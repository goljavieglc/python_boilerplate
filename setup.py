#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
===============================
HtmlTestRunner
===============================


.. image:: https://img.shields.io/pypi/v/python_boilerplate.svg
        :target: https://pypi.python.org/pypi/python_boilerplate
.. image:: https://img.shields.io/travis/goljavi/python_boilerplate.svg
        :target: https://travis-ci.org/goljavi/python_boilerplate

Python Boilerplate contains all the boilerplate you need to create a Python package.


Links:
---------
* `Github <https://github.com/goljavi/python_boilerplate>`_
"""

from setuptools import setup, find_packages

requirements = [ ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Javier Goldschmidt",
    author_email='somossedentarios@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    install_requires=requirements,
    license="MIT license",
    long_description=__doc__,
    include_package_data=True,
    keywords='python_boilerplate',
    name='python_boilerplate',
    packages=find_packages(include=['python_boilerplate']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/goljavi/python_boilerplate',
    version='0.1.0',
    zip_safe=False,
)
