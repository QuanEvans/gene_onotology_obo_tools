from setuptools import setup

setup(
    name='obo_tools',
    version='0.1.0',    
    description='A package for working with OBO ontologies',
    #url='https://github.com/shuds13/pyexample',
    author='Quancheng Liu',
    author_email='quanch@umich.edu',
    py_modules=['obo_tools'],
    install_requires=[
        'obonet', 
        'networkx',
        'numpy',  
        'requests',                  
    ],
)