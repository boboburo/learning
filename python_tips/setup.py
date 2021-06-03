from setuptools import setup, find_packages

"""Minimal setup file for package that allows for imports through 
with __init__.py file. Helpful when working with pytest. 

pip install e . from the root. 
"""

from setuptools import setup, find_packages

setup(
    name='package-name',
    version='0.0.1',  #relased:feature:minor changes:
    license='proprietary',
    description='Brian Carter Inc',

    author='Brian Carter',
    author_email='brianthomascarter@gmail.com',

    packages=find_packages(where='src'),
    package_dir={'': 'src'}  
)