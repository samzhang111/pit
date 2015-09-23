from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pit',
    version='0.3.0',
    description='Python stream filter',
    long_description=long_description,
    url='https://github.com/samzhang111/pit',
    author='Sam Zhang',
    author_email='shimian.zhang@gmail.com',
    license='GNU GPL',
    classifiers=[
        'Development Status :: 3 - Alpha', 'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points={
        'console_scripts': [
            'pit=pit:main',
        ],
    },
    scripts=['pit/pit.py'],
    install_requires=['autoimp==1.0.4'])
