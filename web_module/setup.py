#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import bootstrap3

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = bootstrap3.__version__

if sys.argv[-1] == 'publish':
    os.system('cd docs && make html')
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

setup(
    name='mars-web-module',
    version=version,
    description="""Mars web_module with Django Bootstrap""",
    long_description=readme + '\n\n' + history,
    author='liuhanlong',
    author_email='liuhanlong3304@126.com',
    url='https://git.oschina.net/ethan-coding/mars.git,https://github.com/ethan-lau/mars.git',
    packages=[
        'mars',
    ],
    include_package_data=True,
    install_requires=[
        'django-bootstrap3',
    ],
    license="Apache License 2.0",
    zip_safe=False,
    keywords='mars',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)
