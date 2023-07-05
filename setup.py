from setuptools import find_packages, setup
from typing import List

__version__ = "0.0.1"

REPO_NAME = "phising_domain_detection"
AUTHOR_USER_NAME = "adarsh"
SRC_REPO = "phising_domain_detection"
AUTHOR_EMAIL = "adarshmarvel22@gmail.com"


HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for phising domain detection",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)