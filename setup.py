# -*- coding: utf-8 -*-

from setuptools import setup


version = '1.0.10'


setup(
    name='django-uniapi',
    version=version,
    keywords='django-uniapi',
    description='Django General/Universal API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    url='https://github.com/django-xxx/django-uniapi',

    author='Hackathon',
    author_email='kimi.huang@brightcells.com',

    packages=['django_uniapi'],
    py_modules=[],
    install_requires=['TimeConvert', 'django-response', 'django-six'],

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
