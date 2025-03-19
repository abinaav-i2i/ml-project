from setuptools import find_packages, setup
from typing import List


HYPEN_E = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements.
    Gets the requirements from the setup and appends to the empty list
    req.replace, replaces the '\n' field since in requirements.txt file next lines containing the libraries are read by next lines in html
    name='Project Name'
    version='Version of the project'
    auther, auther_email='Detail of the project-creator
    packages='Finds the package mentioned for the project'
    install_requires='Dependency library for the project' 
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E in requirements:
            requirements.remove(HYPEN_E)
        # elif HYPEN_E not in requirements:
        #     return ('-e . not in requirements')
        # else:
        #     return ('error......')
    
    return requirements


setup(
    name='ml-project',
    version='0.0.1',
    author='Abinaav',
    author_email='abinaav.elango@i2i.com',
    packages=find_packages(),
    install_requires=['pandas', 'numpy', 'seaborn']
)
