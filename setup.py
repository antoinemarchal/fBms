# -*- coding: utf-8 -*-                                                                                                                                                                                                                                              
from setuptools import setup, find_packages

with open("Readme.md") as f:
        readme = f.read()
	
with open("LICENSE") as f:
	license = f.read()

setup(
    name='fBms',
    version='0.1.9',
    description='python interface package for ROHSA software',
    long_description=readme,
    classifiers=[
        'Development status :: 1 - Alpha',
        'License :: CC-By-SA2.0',
        'Programming Language :: Python',
        'Topic :: Data Analysis'
    ],
    author='Antoine Marchal',
    author_email='antoine.marchal@ias.u-psud.fr',
    url='https://github.com/antoinemarchal/fBms',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
            'numpy',
    ],
    include_package_data=True
)
