from setuptools import find_packages, setup

__version__ = "0.0.1"

REPO_NAME = "phising_domain_detection"
AUTHOR_USER_NAME = "adarsh"
SRC_REPO = "phising_domain_detection"
AUTHOR_EMAIL = "adarshmarvel22@gmail.com"

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for phising domain detection",
    packages=find_packages(),
    install_requires=[],
)