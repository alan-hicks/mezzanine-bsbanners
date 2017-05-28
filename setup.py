import os
from setuptools import setup

README=open(os.path.join(os.path.dirname(__file__), 'docs/README.rst')).read()

DESCRIPTION="""
Making it easier to manage attention grabbing and compelling
Bootstrap Carousels and Bootstrap Jumbotrons as banners on home pages
"""

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='mezzanine-bsbanners',
    version='0.1.6',
    packages=['mezzanine_bsbanners'],
    include_package_data=True,
    license='BSD',
    description=DESCRIPTION,
    long_description=README,
    url='http://p-o.co.uk/tech-articles/mezzanine-bootstrap-banners/',
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
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
