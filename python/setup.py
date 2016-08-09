from setuptools import setup, find_packages

setup(
    name="spider",
    version="0.10",
    description="My test module",
    author="Ethan Lau",
    url="http://liuhanlong.top",
    license="LGPL",
    packages=find_packages(include="spider"),
    install_requires=[
        'MySQL-python'
        
    ]
)
