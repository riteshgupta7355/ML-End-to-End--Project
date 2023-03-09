from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This Function will return the list of requirements
    
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace("\n", " ") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)


setup(

name='ml-project',
version="0.0.1",
author='Ritesh Gupta',
author_email="riteshgupta7355@gmail.com",
packages= find_packages(),
install_requires=get_requirements('requirements.txt')


)