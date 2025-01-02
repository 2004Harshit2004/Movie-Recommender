from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file=file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('/n',"") for req in requirements]
    return requirements


setup(
    name='MovieRecommenderSystem',
    version='0.0.1',
    author='Harshit Goswami',
    author_email='fjvb',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()

)

