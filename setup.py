from setuptools import find_packages, setup
from typing import List


ignore='-e .'
def get_requirements(file_path:str)->List[str]:
    '''this function returns list fo libraries needed'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        #above line as when reading file \n comes\
        if ignore in requirements:
            requirements.remove(ignore)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='AR',
    author_email="atifr144@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)