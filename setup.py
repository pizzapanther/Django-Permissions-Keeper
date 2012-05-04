import sys

from setuptools import setup, find_packages

setup(
    name = "permkeep",
    version = '12.05.1',
    description = "Easy way to keep group permissions in sync between Development and Production environments.",
    url = "https://github.com/pizzapanther/Django-Permissions-Keeper",
    author = "Paul Bailey",
    author_email = "paul.m.bailey@gmail.com",
    license = "BSD",
    packages = ['permkeep', 'permkeep.management', 'permkeep.management.commands'],
    include_package_data = True,
)
