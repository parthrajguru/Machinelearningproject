from setuptools import setup, find_packages

HYPEN_E_DOT = '-e .'

def get_requirements(file_path):
    with open(file_path) as file:
        requirements = file.read().splitlines()

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='Machinelearningproject',
    version='0.0.1',
    author='Parth',
    author_email='parthrajguru0212@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
