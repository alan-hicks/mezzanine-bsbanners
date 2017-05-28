"""Making it easier to manage attention grabbing and compelling
Bootstrap Carousels and Bootstrap Jumbotrons as banners on home pages"""
import os
from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

DESCRIPTION="""
Making it easier to manage attention grabbing and compelling
Bootstrap Carousels and Bootstrap Jumbotrons as banners on home pages
"""

setup(
    name='mezzanine-bsbanners',
    version='0.1.8',
    packages=['mezzanine_bsbanners'],
    include_package_data=True,
    license='BSD',
    description=DESCRIPTION,
    long_description=long_description,
    url='https://p-o.co.uk/tech-articles/mezzanine-bootstrap-banners/',
    download_url='https://pypi.python.org/pypi/mezzanine-bsbanners',
    author='Alan Hicks',
    author_email='ahicks@p-o.co.uk',
    requires=['mezzanine'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='banner, carousel',
)
