#!/usr/bin/env python
'discord-logger setup script.'

import os
from setuptools import setup


def read(fname):
    'Utility function to read files.'
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


LONG_DESCRIPTION = read('README.md').splitlines()
DESCRIPTION = LONG_DESCRIPTION[1]
REQUIRES = read('requirements.txt').splitlines()

setup(
    name='discord-logger',
    version='0.0.0',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    keywords="discord data dump export message server channel dms script log logger logging",
    author='Andrea Pascal',
    author_email='andrea@anodium.net',
    url='https://github.com/anodium/discord-logger',
    packages=['discord-logger'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Communications',
        'Topic :: Communications :: Chat',
        'Topic :: Internet',
        'Topic :: Internet :: Log Analysis',
        'Topic :: System',
        'Topic :: System :: Archiving',
        'Topic :: System :: Archiving :: Backup',
        'Topic :: System :: Logging',
        'Topic :: Utilities'
    ],
    requires=REQUIRES,
    license='MIT'
)
