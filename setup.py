from setuptools import setup,find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path : str) -> List:
    
    """
    take filepath of requirements.txt file and return list of requirements
    """
    with open(file_path) as file_object:
        requirements = [req.replace('\n','') for req in file_object.readlines()]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements


setup(name = 'concrete_project',
      version = '0.0.1',
      author = 'msarathrahul',
      author_email = 'msarathrahul@gmail.com',
      packages = find_packages(),
      install_requires = get_requirements('requirements.txt'))