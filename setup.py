# -*- coding: utf-8 -*-

from setuptools import setup


version = '1.0.9'


setup(
    name='django-uniapi',
    version=version,
    keywords='django-uniapi',
    description='Django General/Universal API',
    long_description=open('README.rst').read(),

    url='https://github.com/django-xxx/django-uniapi',

    author='Hackathon',
    author_email='kimi.huang@brightcells.com',

    packages=['django_uniapi'],
    py_modules=[],
    install_requires=['TimeConvert', 'django-response'],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: Financial :: Spreadsheet',
    ],
)
