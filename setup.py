from setuptools import find_packages, setup

setup(
    name="generative-ai-projects",
    version="0.0.0",
    author="Syed Adil Ejaz",
    author_email="ejaz.adil93@gmail.com",
    packages=find_packages(),#This will look for __init__.py files and include those directories as packages in the distribution.
    install_requires=[]
)