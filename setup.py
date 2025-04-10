# coding: utf-8

from setuptools import setup, find_packages

NAME = "basic_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion[flask,swagger-ui,uvicorn]"]

setup(
    name=NAME,
    version=VERSION,
    description="Connexion example",
    author_email="kevin.martins@gmail.com",
    url="",
    keywords=["Swagger", "Connexion"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'basic': ['openapi/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['basic_server=basic.__main__:main']},
    long_description="""\
    Basic example to connexion
    """
)
