"""Making it easier to manage attention grabbing and compelling
Bootstrap Carousels and Bootstrap Jumbotrons as banners on home pages"""
from setuptools import setup

# Get the long description from the README file
with open('README.rst') as file:
    long_description = file.read()

setup(
    name='mezzanine-bsbanners',
    version='0.2.0',
    packages=['mezzanine_bsbanners'],
    include_package_data=True,
    license='BSD',
    description="Making it easier to manage attention grabbing and compelling, Bootstrap Carousels and Bootstrap Jumbotrons as banners on home pages",
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://p-o.co.uk/tech-articles/mezzanine-bootstrap-banners/',
    download_url='https://pypi.org/project/mezzanine-bsbanners/',
    author='Alan Hicks',
    author_email='ahicks@p-o.co.uk',
    requires=['mezzanine'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='banner carousel',
)
